
import mysql.connector


def conexao():
    conexao = mysql.connector.connect(user='root',
                                      password='',
                                      host='127.0.0.1',
                                      database='db_farmacia')

    print('Conexão:', conexao)
    cursor = conexao.cursor()

    sql = 'CREATE DATABASE if not exists db_farmacia'
    cursor.execute(sql)


    sql = """
        CREATE TABLE IF NOT EXISTS remedios(
        codigo INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(40) UNIQUE NOT NULL,
        preco DECIMAL(9,2) NOT NULL,
        data_de_validade DATE NOT NULL,
        prescricao VARCHAR(3) NULL,
        PRIMARY KEY(codigo)
        )   """
    cursor.execute(sql)
    conexao.close()


def registros():
    conexao = mysql.connector.connect(user='root',
                                      password='',
                                      host='127.0.0.1',
                                      database='db_farmacia')
    cursor = conexao.cursor()
    sql = '''select *
            from remedios'''
    cursor.execute(sql)

    registros = cursor.fetchall()
    for codigo, nome, preco, data_de_validade, prescricao in registros:
        print('Código: ', codigo)
        print('Nome: ', nome)
        print('Preço: ', preco)
        print('Data de validade: ', data_de_validade)
        print('Prescrição médica: ', prescricao)
    conexao.close()


def insert():
    conexao = mysql.connector.connect(user='root',
                                      password='',
                                      host='127.0.0.1',
                                      database='db_farmacia')
    cursor = conexao.cursor()
    sql = '''
        insert into remedios
        (nome, preco, data_de_validade, prescricao)
        values (%s, %s, %s, %s)
    '''

    nome = (input('Nome do remédio: '))
    preco = float(input('Preço do remédio: '))
    data_de_validade = input('Data de vencimento (AAAA-MM-DD): ')
    prescricao = input('Precisa de prescrição médica: ')
    info = (nome, preco, data_de_validade, prescricao)
    print(info)
    cursor.execute(sql, info)
    conexao.commit()
    conexao.close()


def alteracao():
    conexao = mysql.connector.connect(user='root',
                                      password='',
                                      host='127.0.0.1',
                                      database='db_farmacia')
    cursor = conexao.cursor()
    sql = '''
            update remedios
            set preco = %s
            where nome = %s
        '''
    preco = input('Novo preço do remédio: ')
    nome = input('Nome do remédio que deseja alterar o valor: ')
    cursor.execute(sql, (preco, nome))
    print('- Registros Atualizados :', cursor.rowcount)
    conexao.commit()
    registros()
    conexao.close()


def delete():
    conexao = mysql.connector.connect(user='root',
                                      password='',
                                      host='127.0.0.1',
                                      database='db_farmacia')
    cursor = conexao.cursor()
    registros()
    print()
    sql = '''
                delete
                from remedios
                where nome = %s
            '''
    nome = input('Nome do remédio a ser deletado: ')
    cursor.execute(sql, (nome,))
    conexao.commit()
    conexao.close()


def menu():
    while True:
        print('''
            1. Inserção de remédios.
            2. Registro de dados.
            3. Apagar registro. 
            4. Editar dados da tabela.
            5. Finalizar.
            ''')
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            insert()

        if opcao == 2:
            registros()

        if opcao == 3:
            delete()

        if opcao == 4:
            alteracao()

        if opcao == 5:
            break
            exit()

conexao()
menu()


