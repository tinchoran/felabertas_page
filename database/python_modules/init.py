import os

# - CLASES
class jugador():
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.goles = 0
        self.edad = 0
        self.partidos = 0
        self.id = 0

def inicializacion():
    global file, file_wd, wd
    # - APERTURA DE ARCHIVOS
    wd = os.getcwd()
    file_wd = wd + "/data/plantel.dat"

    if not os.path.exists(file_wd):
        file = open(file_wd, "w+b")
    else:
        file = open(file_wd, "r+b")



