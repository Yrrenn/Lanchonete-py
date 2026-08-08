from Lanchonete import Lanchonete


class Menu:

    def __init__(self):

        self.lanchonete = Lanchonete()


    def iniciar(self):

        while True:

            print("\n========== LANCHONETE ==========")

            print("1 - Fazer Pedido")

            print("2 - Ver Cardápio")

            print("3 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":

                self.lanchonete.fazer_pedido()

            elif opcao == "2":

                self.lanchonete.mostrar_cardapio()

            elif opcao == "3":

                print("Até logo!")

                break

            else:

                print("Opção inválida!")