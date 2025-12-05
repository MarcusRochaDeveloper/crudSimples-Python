import mysql.connector
from mysql.connector import Error

def criar_conexao(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="taskflow_db"
        )
        print("Conexao com o banco de dados realizada com sucesso")
    except Error as e:
        print(f"O erro '{e}' ocorreu")
    return connection

class Usuario:
    def __init__(self, connection, nome, email, senha):
        self.connection = connection
        self.nome = nome
        self.email = email
        self.senha = senha

    def salvar(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE email = %s", (self.email,))
        if cursor.fetchone():
            print("Usuario com este email ja existe.")
            return

        sql = "INSERT INTO usuarios (nome, email, senha_hash) VALUES (%s, %s, %s)"
        val = (self.nome, self.email, self.senha)
        try:
            cursor.execute(sql, val)
            self.connection.commit()
            print(cursor.rowcount, "registro inserido.")
        except Error as e:
            print(f"Erro ao inserir usuario: {e}")

class Tarefa:
    def __init__(self, connection, usuario_id, titulo, descricao, status):
        self.connection = connection
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descricao = descricao
        
        valid_status = ['PENDENTE', 'EM_ANDAMENTO', 'CONCLUIDA', 'CANCELADA']
        self.status = status if status in valid_status else 'PENDENTE'

    def salvar(self):
        sql = "INSERT INTO tarefas (usuario_id, titulo, descricao, status) VALUES (%s, %s, %s, %s)"
        val = (self.usuario_id, self.titulo, self.descricao, self.status)
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql, val)
            self.connection.commit()
            print(cursor.rowcount, "tarefa inserida.")
        except Error as e:
            print(f"Erro ao inserir tarefa: {e}")

def listar_tarefas(connection):
    cursor = connection.cursor()
    sql = "SELECT t.id, t.titulo, t.status, u.nome FROM tarefas t JOIN usuarios u ON t.usuario_id = u.id"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for row in resultados:
        print(f"ID: {row[0]} | Titulo: {row[1]} | Status: {row[2]} | Usuario: {row[3]}")

def listar_usuarios(connection):
    cursor = connection.cursor()
    sql = "SELECT id, nome, email FROM usuarios"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for row in resultados:
        print(f"ID: {row[0]} | Nome: {row[1]} | Email: {row[2]}")

def editar_tarefa(connection):
    id_tarefa = input("Digite o ID da tarefa para editar: ")
    novo_status = input("Digite o novo status (PENDENTE/EM_ANDAMENTO/CONCLUIDA/CANCELADA): ")
    sql = "SELECT id FROM tarefas WHERE id = %s"
    val = (id_tarefa,)
    cursor = connection.cursor()
    cursor.execute(sql, val)
    if cursor.fetchone() is None:
        print("Tarefa com este ID nao existe.")
        return
    sql = "UPDATE tarefas SET status = %s WHERE id = %s"
    val = (novo_status, id_tarefa)
    cursor = connection.cursor()
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(cursor.rowcount, "tarefa atualizada.")
    except Error as e:
        print(f"Erro ao atualizar: {e}")

def editar_usuario(connection):
    email_atual = input("Digite o email do usuario para editar: ")
    novo_nome = input("Digite o novo nome: ")
    
    if not novo_nome.strip():
        print("Nome nao pode ser vazio.")
        return
    
    sql = "SELECT id FROM usuarios WHERE email = %s"
    val = (email_atual,)
    cursor = connection.cursor()
    cursor.execute(sql, val)
    if cursor.fetchone() is None:
        print("Usuario com este email nao existe.")
        return
    sql = "UPDATE usuarios SET nome = %s WHERE email = %s"
    val = (novo_nome, email_atual)
    cursor = connection.cursor()
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(cursor.rowcount, "usuario atualizado.")
    except Error as e:
        print(f"Erro ao atualizar: {e}")

def deletar_tarefa(connection):
    id_tarefa = input("Digite o ID da tarefa para deletar: ")
    
    if not id_tarefa.isdigit():
        print("ID invalido.")
        return
    elif int(id_tarefa) <= 0:
        print("ID deve ser um numero positivo.")
        return
    
    sql = "DELETE FROM tarefas WHERE id = %s"
    val = (id_tarefa,)
    cursor = connection.cursor()
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(cursor.rowcount, "tarefa deletada.")
    except Error as e:
        print(f"Erro ao deletar: {e}")

def deletar_usuario(connection):
    id_usuario = input("Digite o ID do usuario para deletar: ")
    sql = "DELETE FROM usuarios WHERE id = %s"
    val = (id_usuario,)
    cursor = connection.cursor()
    try:
        cursor.execute(sql, val)
        connection.commit()
        print(cursor.rowcount, "usuario deletado.")
    except Error as e:
        print(f"Erro ao deletar: {e}")

def exibir_menu():
    print("\n========== MENU ==========")
    print("1 - Criar Usuario")
    print("2 - Criar Tarefa")
    print("3 - Editar Tarefa")
    print("4 - Editar Usuario")
    print("5 - Ver Tarefas")
    print("6 - Ver Usuarios")
    print("7 - Deletar Tarefa")
    print("8 - Deletar Usuario")
    print("0 - Sair")

def principal():
    conexao = criar_conexao("localhost", "root", "123456", "taskflow_db")
    
    if conexao is None:
        return

    while True:
        exibir_menu()
        escolha = input("Digite sua escolha: ")
        
        if escolha == '1':
            nome = input("Digite o nome: ")
            email = input("Digite o email: ")
            senha = input("Digite a senha hash: ")
            novo_usuario = Usuario(conexao, nome, email, senha)
            novo_usuario.salvar()
            
        elif escolha == '2':
            listar_usuarios(conexao)
            try:
                usuario_id = int(input("Digite o ID do usuario dono da tarefa: "))
                titulo = input("Digite o titulo da tarefa: ")
                descricao = input("Digite a descricao da tarefa: ")
                status = input("Digite o status (PENDENTE/EM_ANDAMENTO/CONCLUIDA): ")
                nova_tarefa = Tarefa(conexao, usuario_id, titulo, descricao, status)
                nova_tarefa.salvar()
            except ValueError:
                print("ID de usuario invalido.")
                
        elif escolha == '3':
            editar_tarefa(conexao)
            
        elif escolha == '4':
            editar_usuario(conexao)
            
        elif escolha == '5':
            listar_tarefas(conexao)
            
        elif escolha == '6':
            listar_usuarios(conexao)
            
        elif escolha == '7':
            deletar_tarefa(conexao)
            
        elif escolha == '8':
            deletar_usuario(conexao)
            
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opcao invalida.")

    if conexao.is_connected():
        conexao.close()
        print("Conexao fechada.")

if __name__ == "__main__":
    principal()