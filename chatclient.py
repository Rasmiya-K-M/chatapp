import socket
from tkinter import *

def send(list_box,entry):
    message=entry.get()
    list_box.insert('end',message)
    entry.delete(0,END)
    s.send(bytes(message, "utf-8"))
    receive(list_box)
def receive(list_box):
    message = s.recv(50)
    list_box.insert('end',"Server:"+message.decode("utf-8"))
root=Tk()
entry = Entry()
entry.pack(side=BOTTOM)
list_box = Listbox(root)
list_box.pack()
button=Button(root,text='Send',command=lambda :send(list_box,entry))
button.pack(side=BOTTOM)
rbutton=Button(root,text='Receive',command=lambda :receive(list_box))
rbutton.pack(side=BOTTOM)
root.title('Client')
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.connect((HOST_NAME,PORT))
root.mainloop()

