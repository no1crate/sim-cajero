import database as db
import pyautogui as gui
from random import choices as chcs
from string import digits as dgts
loged = False
rl = gui.confirm("¿Que quieres hacer?", buttons=["Registrarme", "Iniciar sesion"])
if(rl == "Registrarme"):
    username = gui.prompt("¿Cual va a ser tu nombre de usuario?")
    if db.verifyElement(username, "users"):
        gui.alert("El nombre de usuario " + username + " esta ocupado!")
    else:
        password = gui.password("¿Cual va a ser tu contraseña?")
        db.addElement(username, username, "users")
        db.addElement(username, password, "passwords")
        db.addElement(username, "0", "cash")
        gui.alert("Registrad@ correctamente!")
        logrd = True
elif(rl == "Iniciar sesion"):
    username = gui.prompt("¿Cual es tu nombre de usuario?")
    if(db.verifyElement(username, "users")):
        password = gui.password("¿Cual es tu contraseña?")
        if(db.verifyContent(username, password, "passwords")):
            gui.alert("Iniciaste sesion correctamente!")
            loged = True

while loged:
    cash = int(db.getElement(username, "cash"))
    a = gui.confirm("$" + str(cash) + "\n¿Que quieres hacer " + username + "?", buttons=["Hacer una transferencia", "Cerrar sesion"])
    if(a == "Hacer una transferencia"):
        userAddMoney = gui.prompt("¿Cual es el nombre de usuario de la persona?")
        if(db.verifyElement(userAddMoney, "users")):
            removeCash = int(gui.prompt("¿Cuanto quieres transferir?"))
            if(removeCash > cash):
                gui.alert("Pon un numero menor o igual a " + cash)
            else:
                cash -= removeCash
                db.modifyContent(username, str(cash), "cash")
                cashFromUser = int(db.getElement(userAddMoney, "cash"))
                cashFromUser += removeCash
                db.modifyContent(userAddMoney, str(cashFromUser), "cash")
                gui.alert("Transferencia completada con exito!")
    elif(a == "Cerrar sesion"):
        loged = False
        gui.alert("Adios " + username + "!")
