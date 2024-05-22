import pymysql;
    
db_host='db-aplicationweb.c3uks48eg8sc.us-east-1.rds.amazonaws.com'
db_user='e_serrano'
db_passw='Libertad18*'
db_name='db_users'
   
def connectionSQL():
        try:
            connection= pymysql.connect(
                host= db_host,
                user= db_user,
                password=db_passw,
                database=db_name
            )
            print("Conexion exitosa a DB")
            return connection
        except Exception as err:
                print("Error conectando a DB", err)
                return None
        
    
def insert_records(id,name,lastname,birthday):
        query="INSERT INTO users (id,name,lastname,birthday) VALUES ("+id+",'"+name+"','"+lastname+"','"+birthday+"')"
        try:
            connection=connectionSQL()
            if connection !=None:
                cursor= connection.cursor()
                cursor.execute(query)
                connection.commit()
                print("Usuario Agregado")
            else:
                    print("Error en la conexion")
                    
        except Exception as err:
            print("Error creando usuario",err)
            
def consult_records(id):
            query= "SELECT * FROM users Where id="+ id
            try:
                connection = connectionSQL()
                cursor = connection.cursor()
                if connection != None:
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
                else:
                    print("Error en la conexion")
                    return None
            except Exception as err:
                print("Error consultando usario", err)
                return None