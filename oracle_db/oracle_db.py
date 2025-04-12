import cx_Oracle

# Função para conectar ao banco de dados Oracle
def connect_to_oracle():
    try:
        # Substitua pelos seus detalhes de conexão
        connection = cx_Oracle.connect(
            user='seu_usuario', 
            password='sua_senha', 
            dsn='seu_dsn'  # O DSN pode ser algo como 'localhost:1521/sid_ou_service'
        )
        print("Conexão bem-sucedida ao banco de dados!")
        return connection
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Função para verificar a existência de uma tabela
def check_table_exists(connection, table_name):
    cursor = connection.cursor()
    query = f"SELECT COUNT(*) FROM all_tables WHERE table_name = '{table_name.upper()}'"
    cursor.execute(query)
    result = cursor.fetchone()
    cursor.close()
    return result[0] > 0

# Função para executar o script SQL
def execute_sql_script(connection, script):
    cursor = connection.cursor()
    try:
        cursor.execute(script)
        connection.commit()  # Commit para garantir que as mudanças sejam aplicadas
        print("Script executado com sucesso!")
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao executar o script: {e}")
    finally:
        cursor.close()

# Função principal para verificar se as tabelas existem antes de criá-las
def main():
    # Conectar ao banco de dados
    connection = connect_to_oracle()
    if connection is None:
        return
    
    # Script SQL para criar as tabelas (o código que você forneceu anteriormente)
    sql_script = 'script_logistica_oracle/script_logistic_oracle.sql'

    # Lista de tabelas para verificar antes de tentar criar
    tables = ['VehicleLoadType', 'VehicleLoad', 'Driver', 'Location', 'ResponsiblePerson', 
              'GrainType', 'Load', 'LoadGrainType', 'WeatherForecast', 'Movement', 
              'MovementForecast', 'StockHistory']

    # Verificar se as tabelas existem e, se não, criar
    for table in tables:
        if not check_table_exists(connection, table):
            print(f"Tabela {table} não encontrada. Criando...")
            execute_sql_script(connection, sql_script)  # Executa o script SQL completo
        else:
            print(f"Tabela {table} já existe. Pulando criação.")

    # Fechar a conexão após a execução
    connection.close()

if __name__ == '__main__':
    main()
