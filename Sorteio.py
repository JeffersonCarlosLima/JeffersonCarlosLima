from tkinter import *
import random

def gera():
    x = random.randrange(1,1000)
    numero["text"] = x
    #print("exibir", x)
janela = Tk()
janela.title('Sorteio')
teste = Label(janela, text="Sorteio de 1 a 1000")
teste.grid(column=0, row=0, pady=15, padx=15)
teste1 = Label(janela,text="Clique no botão para sortear um número")
teste1.grid(column=0, row=1, pady=15, padx=15)
botao = Button(janela, text="Gerar número", command=gera)
botao.grid(column=0, row=2, pady=15, padx=15)
numero = Label(janela, text="Clique no botão para gerar o número")
numero.grid(column=0, row=3, pady=15, padx=15)
janela.mainloop()


