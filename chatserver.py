import socket
from tkinter import *

def send(list_box,entry):
    message=entry.get()
    list_box.insert('end',"Server:"+message)
    entry.delete(0,END)
    client.send(bytes(message, "utf-8"))
def receive(list_box):
    cmessage = client.recv(50)
    list_box.insert('end',"Client:"+cmessage.decode("utf-8"))
root=Tk()
entry=Entry()
entry.pack(side=BOTTOM)
list_box=Listbox(root)
list_box.pack()
button=Button(root,text='Send',command=lambda :send(list_box,entry))
button.pack(side=BOTTOM)
rbutton=Button(root,text='Receive',command=lambda :receive(list_box))
rbutton.pack(side=BOTTOM)
root.title('Server')
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.bind((HOST_NAME,PORT))
s.listen(4)
client,address=s.accept()
root.mainloop()