import unittest
from unittest.mock import patch, MagicMock
import cx_Oracle

# Supondo que o seu script esteja em um arquivo chamado 'db_setup.py', com as funções que você forneceu
import oracle_db.oracle_db as db_setup


class TestDatabaseFunctions(unittest.TestCase):

    @patch('cx_Oracle.connect')
    def test_connect_to_oracle_success(self, mock_connect):
        # Simula uma conexão bem-sucedida
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection
        
        connection = db_setup.connect_to_oracle()
        self.assertEqual(connection, mock_connection)
        mock_connect.assert_called_once()

    @patch('cx_Oracle.connect')
    def test_connect_to_oracle_failure(self, mock_connect):
        # Simula falha de conexão
        mock_connect.side_effect = cx_Oracle.DatabaseError("Erro na conexão")
        
        connection = db_setup.connect_to_oracle()
        self.assertIsNone(connection)

    @patch('cx_Oracle.connect')
    def test_check_table_exists_true(self, mock_connect):
        # Simula que a tabela existe
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = [1]
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        
        table_name = 'VehicleLoad'
        result = db_setup.check_table_exists(mock_connection, table_name)
        
        self.assertTrue(result)
        mock_cursor.execute.assert_called_once_with(
            "SELECT COUNT(*) FROM all_tables WHERE table_name = 'VEHICLELOAD'"
        )

    @patch('cx_Oracle.connect')
    def test_check_table_exists_false(self, mock_connect):
        # Simula que a tabela não existe
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = [0]
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        
        table_name = 'VehicleLoad'
        result = db_setup.check_table_exists(mock_connection, table_name)
        
        self.assertFalse(result)
        mock_cursor.execute.assert_called_once_with(
            "SELECT COUNT(*) FROM all_tables WHERE table_name = 'VEHICLELOAD'"
        )

    @patch('cx_Oracle.connect')
    def test_execute_sql_script_success(self, mock_connect):
        # Simula execução bem-sucedida de script SQL
        mock_cursor = MagicMock()
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        
        sql_script = "CREATE TABLE TestTable (id INT)"
        db_setup.execute_sql_script(mock_connection, sql_script)
        
        mock_cursor.execute.assert_called_once_with(sql_script)
        mock_connection.commit.assert_called_once()

    @patch('cx_Oracle.connect')
    def test_execute_sql_script_failure(self, mock_connect):
        # Simula falha na execução do script SQL
        mock_cursor = MagicMock()
        mock_cursor.execute.side_effect = cx_Oracle.DatabaseError("Erro ao executar SQL")
        mock_connection = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        
        sql_script = "CREATE TABLE TestTable (id INT)"
        db_setup.execute_sql_script(mock_connection, sql_script)
        
        mock_cursor.execute.assert_called_once_with(sql_script)
        mock_connection.commit.assert_not_called()

    @patch('cx_Oracle.connect')
    def test_main_function(self, mock_connect):
        # Simula o teste da função principal
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        # Vamos supor que as tabelas 'VehicleLoadType' e 'GrainType' existam
        # e 'WeatherForecast' não existe. Nesse caso, a função deve tentar
        # criar a tabela 'WeatherForecast'
        
        # Mock para checar as tabelas
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        
        mock_cursor.fetchone.return_value = [1]  # Simula que a tabela 'VehicleLoadType' já existe
        db_setup.check_table_exists = MagicMock(return_value=True)
        mock_cursor.fetchone.return_value = [0]  # Simula que a tabela 'WeatherForecast' não existe
        
        tables_to_create = ['VehicleLoadType', 'WeatherForecast']
        
        db_setup.main()  # Chama a função principal
        
        # Verifica se o código tentou criar a tabela 'WeatherForecast'
        db_setup.execute_sql_script.assert_called_once_with(mock_connection, db_setup.sql_script)

if __name__ == '__main__':
    unittest.main()
