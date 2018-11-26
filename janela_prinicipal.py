#Importando as bibliotecas
from tkinter import *
from tkinter import messagebox
from janela_carros import Janela_Carros
from janela_compradores import Janela_Compradores
from janela_vendedores import Janela_Vendedores

class Janela_Principal(Tk):
    def __init__(self, controle):
        #Atributos
        self.controle = controle
        #Executar o metodo da classe mâe
        super().__init__()
        #Ajustar Tamanho
        self.geometry('300x100+200+200')
        #Colocando um titulo
        self.title('Janela da Concessionária')


        #Widget para fechar tela
        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)

        #Widgets da Concessionária
        self.btn_carros = Button(self, width=10, text='Carros', command=self.criar_janela_carros)
        self.btn_vendedores = Button(self, width=10, text='Vendedores', command=self.criar_janela_vendedores)
        self.btn_compradores = Button(self, width=10, text='Compradores', command=self.criar_janela_compradores)


        #Posicionando os widgets
        self.btn_close.place(x=220, y=75)

        self.btn_carros.place(x=0, y=0)
        self.btn_compradores.place(x=110, y=0)
        self.btn_vendedores.place(x=220, y=0)

    #Metodo para fechar a janela
    def destroy(self):
        #Janela de confirmação
        if messagebox.askokcancel('Confirmação', 'Deseja sair?'):
            super().destroy()

    #Método para o btn_ok
    def btn_ok_click(self):
        #Recuperar a lista de compra
        lista_compra = self.controle.get_lista_compra
        #Percorrer a lista
        for item in lista_compra:
            messagebox.showinfo('Item', item.to_string)

    #Método para click no item de menu
    def menu_click(self):
        messagebox.showinfo('Menu', 'Clicou no item de menu!')

    def criar_janela_carros(self):
        Janela_Carros(self)

    def criar_janela_compradores(self):
        Janela_Compradores(self)

    def criar_janela_vendedores(self):
        Janela_Vendedores(self)