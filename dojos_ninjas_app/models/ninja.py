from dojos_ninjas_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at =data['updated_at']


    @classmethod
    def crearninja(cls, data):
        consulta = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(edad)s, %(dojo_id)s);"
        resultado = connectToMySQL('schema_dojos_ninjas').query_db(consulta, data)
        return resultado


    @classmethod
    def obtener_un_ninja(cls,data):
        consulta = "SELECT * FROM ninjas WHERE id = %(id)s;"
        resultado = connectToMySQL('schema_dojos_ninjas').query_db(consulta, data)
        print(resultado, 'RESULTADO DE OBTENER UN NINJA')
        return cls(resultado[0])

