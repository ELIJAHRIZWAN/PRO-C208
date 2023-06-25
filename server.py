import socket 
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def setup():
    print("\n\t\t\t\t\tIP MESSENGER\n")

    # Getting global values
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADRESS, PORT))

    # Listening incomming connections
    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()


setup_thread = Thread(target=setup)
setup_thread.start()


def acceptConnections():
    global SERVER
    global clients

    while True:
        client, addr = SERVER.accept()
        print(client.addr)

        window=Tk()
    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')
        
selectlabel = Label(window, text= "Select Song",bg='LightSkyBlue', font = ("Calibri",0))
selectlabel.place(x=2, y=1)

listbox = Listbox(window,height = 10, width = 39,activestyle = 'dotbox',bg='LigthSkyBlue',borderwidth=2, font = ("Calibri",10))
listbox.place(x=10,y=18)

scrollbar1 = Scrollbar(listbox)
scrollbar1.place(relheight = 1, relx = 1)
scrollbar1.config(command = listbox.yview)

PlayButton=Button(winow,text="Play", width=10, bf=1,bg='SkyBlue',font = ("Calibri",10))
PlayButton.place(x=30,y=200)

Stop=Button(window,text="Stop",bd=1,width=10,bd=1, bg='SkyBlue', font = ("Calibri",10))
Stop.place(x=200,y=200)

Upload=Button(window,text="Upload",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10))
Upload.place(x=30,y=250)

Download=Button(window,text="Dowload",width=10,bd=1,bg='SkyBlue', font = ("Calibri",10))
Download.place(x=200,y=250)

infoLabel = Label(window, text="",fg="blue", font = ("Calibri",10))
infoLabel.place(x=4, y=280)

window.mainloop()