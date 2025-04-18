import oracledb  # Certifique-se de ter instalado: pip install oracledb

# Função para conectar ao banco de dados Oracle
def connect_to_oracle():
    try:
        connection = oracledb.connect(
    user='c##francismar',
    password='senha123',
    dsn='localhost:1521/ORCLCDB',
)
        print("✅ Conexão bem-sucedida ao banco de dados!")
        return connection
    except oracledb.DatabaseError as e:
        print(f"❌ Erro ao conectar ao banco de dados: {e}")
        return None

# Função para verificar a existência de uma tabela no Oracle
def check_table_exists(connection, table_name):
    cursor = connection.cursor()
    query = """
        SELECT COUNT(*)
        FROM all_tables
        WHERE table_name = :1 AND owner = USER
    """
    cursor.execute(query, [table_name.upper()])
    result = cursor.fetchone()
    cursor.close()
    return result[0] > 0

# Função para executar comandos SQL contidos em um arquivo .sql
def execute_sql_script(connection, script_path):
    try:
        with open(script_path, 'r') as file:
            sql_script = file.read()

        statements = [stmt.strip() for stmt in sql_script.split(';') if stmt.strip()]
        cursor = connection.cursor()

        for stmt in statements:
            cursor.execute(stmt)
        connection.commit()

        print("✅ Script SQL executado com sucesso!")
    except oracledb.DatabaseError as e:
        print(f"❌ Erro ao executar o script SQL: {e}")
    except FileNotFoundError:
        print(f"❌ Arquivo '{script_path}' não encontrado.")
    finally:
        cursor.close()

# Função principal
def main():
    # Caminho do arquivo SQL
    script_path = 'script_logistica_oracle/script_logistic_oracle.sql'

    # Lista das tabelas esperadas no banco
    expected_tables = [
        'VehicleLoadType', 'VehicleLoad', 'Driver', 'Location', 'ResponsiblePerson',
        'GrainType', 'Load', 'LoadGrainType', 'WeatherForecast', 'Movement',
        'MovementForecast', 'StockHistory'
    ]

    # Conectar ao banco
    connection = connect_to_oracle()
    if connection is None:
        return

    # Verificar se todas as tabelas existem
    all_exist = all(check_table_exists(connection, table) for table in expected_tables)

    if all_exist:
        print("✅ Todas as tabelas já existem. Nenhuma ação necessária.")
    else:
        print("⚠️ Algumas tabelas não foram encontradas. Executando script SQL...")
        execute_sql_script(connection, script_path)

    # Fechar conexão
    connection.close()
    print("🔒 Conexão encerrada.")

# Ponto de entrada do script
if __name__ == '__main__':
    main()
