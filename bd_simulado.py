import os
from carro import Carro
from vendedor import Vendedor
from comprador import Comprador


class BD_Simulado:
    def __init__(self):
        self.carros = []
        self.vendedor = []
        self.comprador = []
        self.venda = []

    def carregar_carros(self):
        if os.path.exists('Carros.txt'):
            file = open('Carros.txt', 'r')
            for c in file.readlines():
                c = c.strip().lstrip('(').rstrip(')').split(',')
                carro = Carro(c[0].strip().strip('"').strip("'"),
                              c[1].strip().strip('"').strip("'"),
                              c[2].strip().strip('"').strip("'"),
                              c[3].strip().strip('"').strip("'"),
                              c[4].strip().strip('"').strip("'"),
                              c[5].strip().strip('"').strip("'"))
                self.carros.append(carro)
        else:
            file = open('Carros.txt', 'w')
        file.close()

    def carregar_vendedores(self):
        if os.path.exists('Vendedores.txt'):
            file = open('Vendedores.txt', 'r')
            for c in file.readlines():
                c = c.strip().lstrip('(').rstrip(')').split(',')
                vend = Vendedor(c[0].strip().strip('"').strip("'"),
                              c[1].strip().strip('"').strip("'"),
                              c[2].strip().strip('"').strip("'"))
                self.vendedor.append(vend)
        else:
            file = open('Vendedores.txt', 'w')
        file.close()

    def carregar_compradores(self):
        if os.path.exists('Compradores.txt'):
            file = open('Compradores.txt', 'r')
            for c in file.readlines():
                c = c.strip().lstrip('(').rstrip(')').split(',')
                comp = Comprador(c[0].strip().strip('"').strip("'"),
                              c[1].strip().strip('"').strip("'"))
                self.comprador.append(comp)
        else:
            file = open('Compradores.txt', 'w')
        file.close()

    def add_carro(self, carro):
        self.carros.append(carro)

    def add_vendedor(self, vendedor):
        self.vendedor.append(vendedor)

    def add_comprador(self, comprador):
        self.comprador.append(comprador)

    def save_carros(self):
        file = open('Carros.txt', 'w')
        for c in self.carros:
            file.write(str(c.get_dados()))
            file.write('\n')
        file.close()

    def save_vendedor(self):
        file = open('Vendedores.txt', 'w')
        for c in self.vendedor:
            file.write(str(c.get_dados()))
            file.write('\n')
        file.close()

    def save_comprador(self):
        file = open('Compradores.txt', 'w')
        for c in self.comprador:
            file.write(str(c.get_dados()))
            file.write('\n')
        file.close()

    def mostrar_carros(self):
        return self.carros

    def mostrar_vendedores(self):
        return self.vendedor

    def mostrar_compradores(self):
        return self.comprador

    def remove_vendedor(self, v):
        rmvd = v
        self.vendedor.remove(v)
        return rmvd

    def remove_comprador(self, c):
        rmvd = c
        self.comprador.remove(c)
        return rmvd

    def remove_carro(self, c):
        rmvd = c
        self.carros.remove(c)
        return rmvd