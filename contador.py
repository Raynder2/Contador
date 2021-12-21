from tkinter import *
import tkinter.font as font
from tkinter import messagebox

app = Tk()
app.title("Contador")
app.geometry("575x375")
app.iconbitmap('K:/Administrativo/SetorPessoal/Raynder/Bot/imgs/contador.ico')

def alterar_linha(arquivo,index):
    with open(arquivo,'r') as f:
        texto=f.readlines()
    with open(arquivo,'w') as f:
        cont = 0
        for i in texto:
            if cont == index:
                resposta = int(i)+1
                print('aqui'+str(resposta)+'aqui')
                f.write(str(resposta)+'\n')
                messagebox.showinfo("NOVO CODIGO GERADO", resposta)
            else:
                f.write(i)
            cont = cont + 1

def gerarDeclaracao():
    if(messagebox.askquestion("Confirmação", "Você deseja gerar uma nova declaração?",icon ='info') == 'yes'):
        alterar_linha('bd.txt', 0)

def gerarFuncional():
    if(messagebox.askquestion("Confirmação", "Você deseja gerar uma nova inf funcional?",icon ='info') == 'yes'):
        alterar_linha('bd.txt', 1)

def gerarDespacho():
    if(messagebox.askquestion("Confirmação", "Você deseja gerar um novo despacho?",icon ='info') == 'yes'):
        alterar_linha('bd.txt', 2)

myFont = font.Font(size=30)

C = Canvas(app, bg="blue", height=250, width=300)
filename = PhotoImage(file = "Paisagem.png")
background_label = Label(app, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

font1 = font.Font(name='TkCaptionFont', exists=True)
font1.config(family='courier new', size=20)

C.pack()

button = Button(text='Declaração', bg='#0052cc', fg='#ffffff' , command=gerarDeclaracao)#bg fundo fg font
button['font'] = myFont
button.place(x=25, y=25, width=250, height=150)

button2 = Button(text='Inf Funcional', bg='#C22426', fg='#ffffff' , command=gerarFuncional)#bg fundo fg font
button2['font'] = myFont
button2.place(x=300, y=25, width=250, height=150)

button3 = Button(text='Despacho', bg='#145D3B', fg='#ffffff' , command=gerarDespacho)#bg fundo fg font
button3['font'] = myFont
button3.place(x=165, y=200, width=250, height=150)

app.mainloop()