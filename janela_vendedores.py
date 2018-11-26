#Importando as bibliotecas
from tkinter import *
from tkinter import messagebox

class Janela_Vendedores(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('200x200+200+200')
        self.title('Segunda Janela')
        self.transient(parent)
        self.grab_set()

        #Widgets
        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)

        # Posicionando os widgets
        self.btn_close.place(x=0, y=175)

        # Metodo para fechar a janela
        def destroy(self):
            # Janela de confirmação
            if messagebox.askokcancel('Confirmação', 'Deseja sair?'):
                super().destroy()