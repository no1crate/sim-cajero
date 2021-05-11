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
        db.addElement(username, "", "history")
        gui.alert("Registrad@ correctamente!")
        loged = True
elif(rl == "Iniciar sesion"):
    username = gui.prompt("¿Cual es tu nombre de usuario?")
    if(db.verifyElement(username, "users")):
        password = gui.password("¿Cual es tu contraseña?")
        if(db.verifyContent(username, password, "passwords")):
            gui.alert("Iniciaste sesion correctamente!")
            loged = True

while loged:
    cash = int(db.getElement(username, "cash"))
    a = gui.confirm("$" + str(cash) + "\n¿Que quieres hacer " + username + "?", buttons=["Hacer una transferencia", "Movimientos", "Cerrar sesion"])
    if(a == "Hacer una transferencia"):
        userAddMoney = gui.prompt("¿Cual es el nombre de usuario de la persona?")
        if(userAddMoney != username):
            if(db.verifyElement(userAddMoney, "users")):
                removeCash = gui.prompt("¿Cuanto quieres transferir?")
                removeCash = removeCash.replace('-', '')
                removeCash = int(removeCash)
                if(removeCash > cash):
                    gui.alert("Pon un numero menor o igual a " + cash)
                else:
                    transferPassword = gui.password("Ingresa tu contraseña para confirmar:")
                    if(db.verifyContent(username, transferPassword, "passwords")):
                        cash -= removeCash
                        db.modifyContent(username, str(cash), "cash")
                        cashFromUser = int(db.getElement(userAddMoney, "cash"))
                        cashFromUser += removeCash
                        db.modifyContent(userAddMoney, str(cashFromUser), "cash")
                        if(len(db.getElement(userAddMoney, "history")) != 0):
                            db.modifyContent(userAddMoney, db.getElement(userAddMoney, "history") + "Recibido " + str(removeCash) + " de " + username, "history")
                        else:
                            db.modifyContent(userAddMoney, db.getElement(userAddMoney, "history") + "\nRecibido " + str(removeCash) + " de " + username, "history")
                        if(len(db.getElement(username, "history")) != 0):
                            db.modifyContent(username, db.getElement(username, "history") + "Enviado " + str(removeCash) + " a " + userAddMoney, "history")
                        else:
                            db.modifyContent(username, db.getElement(username, "history") + "\nEnviado " + str(removeCash) + " a " + userAddMoney, "history")
                        gui.alert("Transferencia completada con exito!")
    elif(a == "Movimientos"):
        if(len(db.getElement(username, "history")) == 0):
            gui.alert("No tienes movimientos!")
        else:
            gui.alert(db.getElement(username, "history"))
    elif(a == "Cerrar sesion"):
        loged = False
        gui.alert("Adios " + username + "!")
