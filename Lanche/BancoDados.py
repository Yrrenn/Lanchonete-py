class BancoDados:

    ARQUIVO = "BD.txt"

    @staticmethod
    def salvar(pedido):

        with open(BancoDados.ARQUIVO, "a", encoding="utf-8") as bd:

            bd.write(f"Cliente: {pedido.cliente}\n")

            bd.write("Pedido:\n")

            for produto in pedido.produtos:

                bd.write(f"- {produto.nome} - R$ {produto.preco:.2f}\n")

            bd.write(f"Total: R$ {pedido.calcular_total():.2f}\n")

            bd.write("--------------------------------\n")