class mixinsData(object):
    def __init__(self,user="pato",password="contra",port="123",host="localhost",db="mysql"):
            self.user = user
            self.password = password
            self.port = port
            self.host = host
            self.db = db

    def get_username(self):
        return self.user
    def get_password(self):
        return self.password
    def get_port(self):
        return self.port
    def get_host(self):
        return self.host
    def get_db(self):
        return self.db

usuario = str(input("nombre de usuario?: "))
password = str(input("contrasena?: "))
obj = mixinsData(user = usuario, password = password)
print(obj.user)
print (obj.password)
print(obj.get_username())
