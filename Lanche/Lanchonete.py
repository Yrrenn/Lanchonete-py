from Produto import Produto
from Pedido import Pedido
from BancoDados import BancoDados


class Lanchonete:

    def __init__(self):

        self.cardapio = [

            Produto("Hambúrguer",20),

            Produto("X-Salada",25),

            Produto("Batata Frita",12),

            Produto("Refrigerante",8),

            Produto("Suco",10)

        ]


    def mostrar_cardapio(self):

        print("\n========== CARDÁPIO ==========")

        for i, produto in enumerate(self.cardapio):

            print(f"{i+1} - {produto.nome} - R$ {produto.preco:.2f}")

        print("0 - Finalizar")


    def fazer_pedido(self):

        cliente = input("Nome do cliente: ")

        pedido = Pedido(cliente)

        while True:

            self.mostrar_cardapio()

            opcao = int(input("Escolha: "))

            if opcao == 0:

                break

            elif 1 <= opcao <= len(self.cardapio):

                pedido.adicionar_produto(self.cardapio[opcao-1])

                print("Produto adicionado!")

            else:

                print("Opção inválida!")

        BancoDados.salvar(pedido)

        print(f"\nTotal: R$ {pedido.calcular_total():.2f}")

        print("Pedido salvo!")