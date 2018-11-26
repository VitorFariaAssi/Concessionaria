#Importando as bibliotecas
from tkinter import *
from tkinter import messagebox
from carro import Carro

#Classe Segunda Janela
class Janela_Carros(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('200x200+200+200')
        self.title('Janela de Carros')
        self.transient(parent)
        self.grab_set()

        #Widgets
        self.btn_close = Button(self, width=10, text='Sair', command=self.destroy)
        self.btn_add = Button(self, width=10, text='Adicionar Carro', command=self.adicionar_carro)

        # Posicionando os widgets
        self.btn_close.place(x=0, y=175)
        self.btn_add.place(x=175, y=175)

        # Metodo para fechar a janela
        def destroy(self):
            # Janela de confirmação
            if messagebox.askokcancel('Confirmação', 'Deseja sair?'):
                super().destroy()

    def adicionar_carro(self):
        modelo = self.entry_mod_var.get()
        marca = self.entry_marca_var.get()
        ano = self.entry_ano_var.get()
        preco = self.entry_preco_var.get()
        estado = self.entry_estado_var.get()
        placa = self.entry_placa_var.get()
        c = Carro(modelo, marca, ano, estado, preco, placa)
        self.control.bd.add_carro(c)
        messagebox.showinfo('Carro', f'{placa} foi adicionado.')

    def remover_carro(self):
        placa = self.entry_placa_var.get()
        remov = None
        if messagebox.askyesno('Excluir', 'Deseja excluir o carro?') is False:
            return None
        for c in self.control.bd.show_carro():
            if c.get_placa() == placa:
                remov = self.control.bd.remove_carro()
                messagebox.showinfo('Concluído', 'O carro de placa' ,f'{placa} foi removido.')
        if remov is None:
            messagebox.showerror('Erro!!!', 'Não tem carro com esses dados')




