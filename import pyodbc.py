import pyodbc


print(pyodbc.drivers())#Printa os drives instalados.

def Anotacoes():
                #Se o banco tiver senha
    # connection_data = ("Driver={SQLire3 ODBC Driver};"
    #                    "server=localhost;"
    #                    "Database=chinook.db"
    #                    "UID=Login;"
    #                    "PWD=Senha")


                # Driver= que é utilizado para conectar
                # Servidor= onde está armazenado o Banco de dado (ex: link se for online ou onde estiver)
                            #localhost: é minha maquina
    # connection_data = ("Driver={SQL Server};"
    #                    "server=localhost;"
    #                    "ContosoRetailDW.dbo")

                                        #Nome tabela
                    #utilizando o Pandas para ler o arquivo em SQL
    #produtosDF = pd.read_sql_query("SELECT * FROM ContosoRetail.dbo.DimProduct", connection)
                                                    #Base de dados, tabela que será consultada e a conexão
    
        #connection.commit()
                #Salva a situação em que o banco de dados se encontra

                    #Armazena todos os valores do DB
    #cursor.fatchall()    #values
    #cursor.description() #colunas
    # print(valores[:10])#printa as 10 primeiras linhas do DB

                        #Armazena todos os valores do DB
    # valores = cursor.fetchall()
    # print(valores[:10])#printa as 10 primeiras linhas do DB
    pass

    #

#   C

def createInDB():


    connection_data = ("""
                        Driver={SQLire3 ODBC Driver};
                        server=localhost;
                        Database=chinook.db""")
    

    connection = pyodbc.connect(connection_data)
                    #Efetua a conexão

    cursor = connection.cursor()#Serve para manipular os dados no DB

                    #faz execução do comando
    #cursor.execute("SELECT * FROM Salaries")
    cursor.execute("""
                    INSERT INTO albums (Title, ArtistID)
                    VALUES
                    ('Lira doidão', 4)
                    """)#Insere uma informação no banco de dados.

    connection.commit()
                #Salva a situação em que o banco de dados se encontra

    cursor.close()
    connection.close()

#   R

def readInDB():
    import pandas as pd
    connection_data = ("""
                        Driver={SQLire3 ODBC Driver};
                        server=localhost;
                        Database=chinook.db""")
    

    connection = pyodbc.connect(connection_data)
                    #Efetua a conexão

    cursor = connection.cursor()#Serve para manipular os dados no DB

                    #faz execução do comando
    #cursor.execute("SELECT * FROM Salaries")
    cursor.execute("""
                    SELECT * FROM customers 
                    """)#Insere uma informação no banco de dados.
    
    values_cursor = cursor.fetchall() #É uma lista. Podemos usar todos os métodos de lista
    print(values_cursor[:10])#printa as 10 primeiras linhas do DB

    description_DB = cursor.description #pega as colunas do DB transforma em uma tupla
    columns = [tupla[0] for tupla in description_DB] #Pega o primeiro item da tupla
    clientSheet = pd.DataFrame.from_records(values_cursor, columns=columns) 
                    #columns=["ID", "Nome"]
                    #armazena as informações do cursor em um DF

                                            #Nome tabela
                    #utilizando o Pandas para ler o arquivo em SQL
    produtosDF = pd.read_sql_query("SELECT * FROM ContosoRetail.dbo.DimProduct", connection)
                                                    #Base de dados, tabela que será consultada e a conexão
    cursor.close()
    connection.close()
    
def readPandasInDB():
    """Exclusivamente para SQLite3, não ler outro anco de dados
    Serve só para ler um o DB. Não efetua outros comandos."""
    import pandas as pd
    import sqlite3
    connection_pd_sql = sqlite3.connect("""chinook.db""")
    clientSheet_pd = pd.read_sql("SELECT * FROM customers", connection_pd_sql)
    print(clientSheet_pd)
    connection_pd_sql.close()

#   U

def updateInDB():

    data_connection =  ("""Driver={SQLite3 ODBC Driver};
                            Server=localhoste;
                            Database=chinook.db""")
    
    connection = pyodbc.connect(data_connection)
    
    cursor = connection.cursor()

    cursor.execute("""UPDATE customers SET Email='adriano@hotmail.com.br' WHERE Email='Luiz@gembraer.com.br'
                    """)

    cursor.commit()
    cursor.close()
    connection.close()

#   D

def deleteInDB():
    
    data_connection = ("""Driver={SQLite3 ODBC Driver};
                            Server=localhoste;
                            Database=chinook.db""")
    
    connection = pyodbc.connect(data_connection)

    cursor = connection.cursor()

    cursor.execute("""DELETE FROM albums WHERE AlbumId=2""")

    cursor.commit()
    cursor.close()
    connection.close()
    

def exercicioCrud():

    import pandas as pd
    import sqlite3
                        #importar com pandas
    # connection = sqlite3.connect("salarios.sqlite")
    # sheetSalaries_pd = pd.read_sql("SELECT * FROM Salaries", connection)


    # connection.close()

    data_connection = ("""Driver={SQLite3 ODBC Driver};
                            Server=localhost;
                            Database=salarios.sqlite3""")
    
    connection = pyodbc.connect(data_connection)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Salaries")
    values = cursor.fatchall()
    description =  cursor.description #descrição das colunas(nome, tipo etc)

    columns = [tupla[0] for tupla in description] #pega o primeiro item da tupla descrição
    sheetSalariesDf = pd.DataFrame.from_records(values, columns=columns)

    #Garantir que tem só São Francisco
    sheetSalariesDf = sheetSalariesDf.loc[sheetSalariesDf["Agency"] == "San Francisco", :]
                                            #Traz as linhas que tiver san francisco na coluna Agency
    
    # Qual foi a evolução do salário médio  ao longo dos anos
    sheetSM = sheetSalariesDf.groupby("Year").mean()

    #print(sheetSM[["TotalPay", "TotalPayBenefits"]])

    #Quantos funcionários tivemos ao longo dos anos?
    sheetQTYEmploee = sheetSalariesDf.groupby("Year").mean()
    sheetQTYEmploee = sheetQTYEmploee[["ID"]]
    sheetQTYEmploee = sheetQTYEmploee.rename(columns={"ID:QTYEmploee"})

    #Qual foi a evolução do total gasto com salário ao longo dos anos
    def formatar(valor):
        return 'R$:,.2f'.format(valor)
    sheetTotalSalaries = sheetSalariesDf.groupby("Year").sum()
    sheetTotalSalaries = sheetTotalSalaries[["TotalPay", "TotalPayBenefits"]]
    sheetTotalSalaries["TotalPay"] = sheetTotalSalaries["TotalPay"].apply(formatar)
    sheetTotalSalaries["TotalPayBenefits"] = sheetTotalSalaries["TotalPayBenefits"].apply(formatar)


    
    connection.close()
    cursor.close()

  
