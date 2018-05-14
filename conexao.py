import time
import MySQLdb

class Conexao: 
    def __init__(self,dbname): #Armazena a conexao em um atributo
        self.con= MySQLdb.connect("localhost","root","",dbname)

    def query(self,query,parametros): #use para inserir,deletar e atualizar dados do mysql
        trans= self.con.cursor()
        trans.execute(query,parametros)
        self.con.commit()
        self.con.close()

    def leitura(self,query,parametros): #efetura leitura e retorna a lista com as infos
        
        cursor= self.con.cursor()
        cursor.execute(query % parametros)
        return cursor
       
