class Pedido:

    def __init__(self, cliente):

        self.cliente = cliente

        self.produtos = []


    def adicionar_produto(self, produto):

        self.produtos.append(produto)


    def calcular_total(self):

        total = 0

        for produto in self.produtos:

            total += produto.preco

        return total