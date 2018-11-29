from tkinter import *
from tkinter import messagebox
from venda import Venda
from carro import Carro

class Janela_Venda(Toplevel):
    def __init__(self, parent, controle):
        super().__init__(parent)
        self.controle = controle
        self.geometry('250x250+200+200')
        self.title('Janela de Venda')
        self.transient(parent)
        self.grab_set()

        l = 0
        c = 0
        for carro in self.controle.bd.carros:
            self.botao_carro = Button(self, width=10, textvariable=carro.placa).grid(row=l, column=c)
            c += 1
            if c == 3:
                c = 0
                l += 1