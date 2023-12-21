import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    dataBase="dbyoutube"
    )

cursor = connection.cursor()

def createDB():
    productName = "Água"
    productValue = 2.50
    comando = f"INSERT INTO vendas (nome_produto, valor) 
                VALUES ('{productName}', {productValue})"
    
    cursor.execute(comando)
    connection.commit()

def readDB():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)

def UpdateDB():
    value = 6
    productName = "Água"

    comando = f"""
        UPDATE vendas
        SET valor = {value} 
        WHERE nome_produto = '{productName}'
        """
    cursor.execute(comando)
    connection.commit()

def DeleteDB():
    productName = "Água"
    comando = f"""
        DELETE FROM vendas 
        WHERE nome_produto = '{productName}'
        """
    cursor.execute(comando)
    connection.commit()

cursor.close()
connection.close()