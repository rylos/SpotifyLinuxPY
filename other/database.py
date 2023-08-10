import mysql.connector

# Parametri di connessione al database MySQL
db_connection = mysql.connector.connect(
    host="localhost",
    user="sayori",
    password="nintendo23",
    database="natzuki"
)

def create_table():
    try:
        cursor = db_connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_choices (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nickname VARCHAR(255),
            choice VARCHAR(255),
            error_message TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
        cursor.execute(create_table_query)
        db_connection.commit()
        cursor.close()
    except mysql.connector.Error as err:
        print("Errore durante la creazione della tabella:", err)

create_table()