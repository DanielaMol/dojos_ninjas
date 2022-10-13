from dojos_ninjas_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #METODO PARA CREAR
    @classmethod
    def creardojo(cls, data):
        consulta = "INSERT INTO dojos (name) VALUES (%(name)s);"
        resultado = connectToMySQL('schema_dojos_ninjas').query_db(consulta, data)
        return resultado


    #METODOS DE LECTURA
    @classmethod
    def todos_dojos(cls):
        consulta = "SELECT * FROM dojos;"
        resultado = connectToMySQL('schema_dojos_ninjas').query_db(consulta)
        dojos = []
        for diccionario in resultado:
            dojos.append(cls(diccionario))
        return dojos
    

    @classmethod
    def obtener_un_dojo(cls, data):
        consulta = "SELECT * FROM dojos WHERE id = %(id)s;"
        resultado = connectToMySQL('schema_dojos_ninjas').query_db(consulta, data)
        return cls(resultado[0])


    @classmethod
    def obtener_ninjas_del_dojo(cls, data):
        consulta = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        resultado = connectToMySQL('schema_dojos_ninjas').query_db(consulta, data)
        return resultado