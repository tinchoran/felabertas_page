import os, pickle, json, io
from python_modules import init

init.inicializacion()

player = init.jugador()

wd = os.getcwd() + "/data"

json_wd = wd + "/plantel.json"
json_file = open(json_wd, "w")

json_file.write("[")

firstPlayer = True      #flag

fileTam = os.path.getsize(init.file_wd)
init.file.seek(0,0)
while fileTam > init.file.tell():
    player = pickle.load(init.file)
    player.nombre = player.nombre.strip()
    player.apellido = player.apellido.strip()
    player.edad = int(player.edad)
    player.goles = int(player.goles)
    player.partidos = int(player.partidos)
    player_json = {
        "nombre": player.nombre,
        "apellido": player.apellido,
        "edad": player.edad,
        "goles": player.goles,
        "partidos": player.partidos
    }
    if not firstPlayer:
        json_file.write(",")
    json.dump(player_json, json_file)
    firstPlayer = False

json_file.write("]")
init.file.close()
json_file.close()