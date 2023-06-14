import pickle, io, os.path, os
from python_modules import common,menues
from python_modules import init
from python_modules import funcionalidad as fun

init.inicializacion()

fun.reasignar_ID()


# - MAIN
print("Bienvenido al gestor de jugadores de Felabertas FC")
menues.principal()
op = input(" - ")
while (op != "1" and op!="2" and op!= "3" and op!= "4" and op!= "5" and op!="0"):
    common.borrado()
    common.op_incorrecta()
    menues.principal()
    op = input(" - ")
while op != "0":
    if op == "1":
        common.borrado()
        fun.modify_menu()
        common.borrado()
    elif op == "2":
        common.borrado()
        fun.alta_menu()
        common.borrado()
    elif op == "3":
        common.borrado()
        fun.baja_menu()
        common.borrado()
    elif op == "4":
        common.borrado()
        fun.sort_file_byGoals()
        common.borrado()
    elif op == "5":
        common.borrado()
        fun.sort_file_byMatchs()
        common.borrado()
    menues.principal()
    op = input(" - ")
    while (op != "1" and op!="2" and op!= "3" and op!="4" and op!="5" and op!="0"):
        common.borrado()
        common.op_incorrecta()
        menues.principal()
        op = input(" - ")
        
fun.reasignar_ID()

init.file.close()