#Funciones auxiliares para no llenar con valores 'NONE'
def variable_llenada(variable):
    if variable == "": 
        return False
    return True #se llenó

def lista_llenada(lista):
    for elem in lista:
        if elem == "": 
            return False
    return True #se llenó

#Definicion de Usuario e info local de usuarios 
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'


users = []
id = 4
users.append(User(id=1, username='Anthony', password='password'))
users.append(User(id=2, username='Becca', password='secret'))
users.append(User(id=3, username='Carlos', password='somethingsimple'))

def validate_on_username(name ):
    for x in users:
        if(x.username == name): return False