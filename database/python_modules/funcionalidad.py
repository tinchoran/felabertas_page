from python_modules import menues,common, init
import pickle, io, os, time
from unidecode import unidecode

# - FORMATEO

def format_reg(): # - TAMAÑO DEL REGISTRO --> 172 bytes
    global record
    record.nombre = record.nombre.ljust(12, " ")            # - NOMBRE - 12 chars
    record.apellido = record.apellido.ljust(20, " ")        # - APELLIDO - 20 chars
    record.goles = str(record.goles)
    record.goles = record.goles.ljust(3, " ")               # - GOLES - 3 chars
    record.edad = str(record.edad)                          
    record.edad = record.edad.ljust(2, " ")                 # - EDAD - 2 chars
    record.partidos = str(record.partidos)
    record.partidos = record.partidos.ljust(3, " ")         # - PARTIDOS - 3 chars
    record.id = str(record.id)
    record.id = record.id.ljust(2, " ")                           # - ID - 2 chars


def reasignar_ID():
    global file, file_wd, record
    tam = os.path.getsize(init.file_wd)
    if tam > 0:
        record = init.jugador()
        init.file.seek(0,0)
        pickle.load(init.file)
        tamreg = int(init.file.tell())
        init.file.seek(0, 0)
        while tam > init.file.tell():
            puntero = int(init.file.tell() / tamreg)
            record = pickle.load(init.file)
            record.id = int(record.id)
            record.id = puntero + 1
            format_reg()
            init.file.seek(puntero * tamreg, 0)
            pickle.dump(record, init.file)
            init.file.flush()
        


# - LISTADO
def listado():
    global file, file_wd
    regaux = init.jugador()
    tam = os.path.getsize(init.file_wd)
    init.file.seek(0, 0)
    print("---------------------------------------------------------------------------")
    print("|  ID   |   NOMBRE    ", "|     APELLIDO        ", "| EDAD ", "| GOLES ","| PARTIDOS |")
    while tam > init.file.tell():
        regaux = pickle.load(init.file)
        time.sleep(0.05)
        print("---------------------------------------------------------------------------")
        print("| ",regaux.id,    "  |",regaux.nombre, "|",regaux.apellido, "|",regaux.edad,"   |", regaux.goles,"   |   ", regaux.partidos, "  |")
    print("---------------------------------------------------------------------------")  
        
    
    
# - MODIFY    
def obtener_regCant():
    global record, file, file_wd
    tam = os.path.getsize(init.file_wd)
    init.file.seek(0, 0)
    pickle.load(init.file)
    tamreg = init.file.tell()
    cantreg = int(int(tam) / int(tamreg))
    return cantreg
    

def modify_menu():
    global record
    listado()
    menues.modify()
    opm = input(" - ")
    while (opm != "1" and opm != "2"):
        common.borrado()
        listado()
        common.op_incorrecta()
        menues.modify()
        opm = input()
    while opm != "2":
        tam = os.path.getsize(init.file_wd)
        
        if tam > 0:
            common.borrado()
            listado()
            print("---------------------------------------")
            print("Especifique ID del jugador a modificar")
            print("---------------------------------------")
            opID = int(input(" - "))
            cantreg = obtener_regCant()
            while opID < 1 or opID > cantreg:
                common.borrado()
                listado()
                print("---------------------------------------")
                print("Seleccione una opción válida")
                print("---------------------------------------")
                opID = int(input(" - "))
            common.borrado()
            init.file.seek(0, 0)
            pickle.load(init.file)
            tamreg = init.file.tell()
            posicion_reg = int(tamreg)* (opID - 1)
            init.file.seek(int(posicion_reg), 0)
            record = pickle.load(init.file)
            common.borrado()
            menues.sub_modify(record)
            opc = input("... ")
            while opc != "1" and opc!="2" and opc!="3" and opc != "4":
                common.borrado()
                common.op_incorrecta()
                menues.sub_modify(record)
                opc = input("... ")
            while opc != "4":
                opc = int(opc)
                common.borrado()
                if(opc == 1):
                    print(" - GOLES: ", record.goles)
                    print("")
                    record.goles = input("Ingrese el nuevo valor... ")
                if(opc == 2):
                    print(" - PARTIDOS: ", record.partidos)
                    print("")
                    record.partidos = input("Ingrese el nuevo valor... ")
                if(opc == 3):
                    print(" - EDAD: ", record.edad)
                    print("")
                    record.edad = input("Ingrese el nuevo valor... ")
                    
                format_reg()
                init.file.seek(int(posicion_reg), 0)
                pickle.dump(record, init.file)
                init.file.flush()
                
                common.borrado()
                print("Jugador modificado exitosamente!")
                menues.sub_modify(record)
                opc = input("... ")
                while opc != "1" and opc!="2" and opc!="3" and opc != "4":
                    common.borrado()
                    common.op_incorrecta()
                    menues.sub_modify(record)
                    opc = input("... ")
            
        else:
            common.borrado()
            print("La base de datos está vacía")
        print("---------------------------------------------------------------------------")
        menues.modify()
        opm = input(" - ")
 
 
 
# - ALTA   

def alta_obtenerID():
    global file, file_wd,record
    tam = os.path.getsize(init.file_wd)
    if tam > 0:
        init.file.seek(-165, 2)
        record = init.jugador()
        record = pickle.load(init.file)
        alta_obtenerID = int(record.id) + 1
    else:
        alta_obtenerID = 1
    return alta_obtenerID
    

def alta_menu():
    global file, file_wd, record
    menues.alta()
    opm = input(" - ")
    while (opm != "1" and opm != "2"):
        common.borrado()
        common.op_incorrecta()
        menues.alta()
        opm = input()
    while opm != "2":
        common.borrado()
        newID = alta_obtenerID()
        record = init.jugador()
        print(" - ALTA DE JUGADORES - ")
        print("")
        print("")
        record.id = newID
        print(" - NOMBRE -")
        record.nombre = input("...")
        record.nombre = unidecode(record.nombre)
        print("")
        print(" - APELLIDO -")
        record.apellido = input("...")
        record.apellido = unidecode(record.apellido)
        print("")
        print(" - EDAD -")
        record.edad = input("...")
        print("")
        print(" - GOLES -")
        record.goles = input("...")
        print("")
        print(" - PARTIDOS JUGADOS -")
        record.partidos = input("...")
        common.borrado()
        print(" - ALTA DE JUGADORES - ")
        print("")
        print("")
        print("- DATOS INGRESADOS -")
        print("-Nombre:  ", record.nombre)
        print("-Apellido ",record.apellido)
        print("Edad:  ",record.edad)
        print("Goles:  ",record.goles)
        print("Partidos: ",record.partidos)
        opc = input("¿Son estos datos correctos? (S/N)")
        while opc != "s" and opc != "n" and opc != "N" and opc != "S":
            common.op_incorrecta()
            opc = input("S/N")
        if(opc == "S" or opc == "s"):
            format_reg()
            init.file.seek(0, 2)
            pickle.dump(record, init.file)
            init.file.flush()
            common.borrado()
        elif(opc == "N" or opc == "n"):
            common.borrado()
            print(" - ALTA CANCELADA -")
        menues.alta()
        opm = input(" - ")
        while (opm != "1" and opm != "2"):
            common.borrado()
            common.op_incorrecta()
            menues.alta()
            opm = input()
            
    
# - BAJA
        
def baja_menu():
    global file, file_wd, record
    '''
    menues.baja()
    opm = input(" - ")
    while (opm != "1" and opm != "2"):
        common.borrado()
        common.op_incorrecta()
        menues.baja()
        opm = input()
    while opm != "2":
        listado()
        print("---------------------------------------")
        print("Especifique ID del jugador a eliminar")
        print("---------------------------------------")
        opID = int(input(" - "))
        cantreg = obtener_regCant()
        while opID < 1 or opID > cantreg:
            common.borrado()
            listado()
            print("---------------------------------------")
            print("Seleccione una opción válida")
            print("---------------------------------------")
            opID = int(input(" - "))
        common.borrado()
        init.file.seek(0, 0)
        pickle.load(init.file)
        tamreg = init.file.tell()
        posicion_reg = int(tamreg)* (opID - 1)
        init.file.seek(int(posicion_reg), 0)
        
        
        common.borrado()
        print("")
        print("Jugador dado de baja exitosamente")
        print("")
        menues.baja()
        opm = input(" - ")
        while (opm != "1" and opm != "2"):
            common.borrado()
            common.op_incorrecta()
            menues.baja()
            opm = input()
    '''
    print("Esta sección no está disponible.")
    print("")
    input("Envíe cualquier caracter para continuar... ")
    
    
# - ORDENAMIENTO DEL ARCHIVO (SORT)

def sort_file_byGoals():
    global file, file_wd, record, regaux
    record = init.jugador()
    regaux = init.jugador()
    init.file.seek(0,0)
    pickle.load(init.file)
    tamreg = int(init.file.tell())
    init.file.seek(0, 0)
    tam = os.path.getsize(init.file_wd)
    if tam > init.file.tell():
        cantreg = obtener_regCant()
        for i in range(0, cantreg - 1):
            for j in range(i+1, cantreg):
                init.file.seek(tamreg*i, 0)
                record = pickle.load(init.file)
                init.file.seek(tamreg*j, 0)
                regaux = pickle.load(init.file)
                if(int(record.goles) <= int(regaux.goles)):
                    init.file.seek(tamreg*i, 0)
                    pickle.dump(regaux, init.file)
                    init.file.flush()
                    init.file.seek(tamreg*j, 0)
                    pickle.dump(record, init.file)
                    init.file.flush()
    reasignar_ID()
    print("Archivo exitosamente ordenado de forma descendete por goles.")
    input("Envíe cualquier caracter para continuar... ")
        
def sort_file_byMatchs():
    global file, file_wd, record, regaux
    record = init.jugador()
    regaux = init.jugador()
    init.file.seek(0,0)
    pickle.load(init.file)
    tamreg = int(init.file.tell())
    init.file.seek(0, 0)
    tam = os.path.getsize(init.file_wd)
    if tam > init.file.tell():
        cantreg = obtener_regCant()
        for i in range(0, cantreg - 1):
            for j in range(i+1, cantreg):
                init.file.seek(tamreg*i, 0)
                record = pickle.load(init.file)
                init.file.seek(tamreg*j, 0)
                regaux = pickle.load(init.file)
                if(int(record.partidos) <= int(regaux.partidos)):
                    init.file.seek(tamreg*i, 0)
                    pickle.dump(regaux, init.file)
                    init.file.flush()
                    init.file.seek(tamreg*j, 0)
                    pickle.dump(record, init.file)
                    init.file.flush()
    reasignar_ID()
    print("Archivo exitosamente ordenado de forma descendete por partidos jugados.")
    input("Envíe cualquier caracter para continuar... ")