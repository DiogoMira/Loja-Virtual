class ProdutoInexistenteError(Exception):
    pass

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = float(preco)

    def __str__(self):
        return f"{self.nome} - €{self.preco:.2f}"

class Carrinho:
    def __init__(self):
        self.itens = {}

    def adicionar(self, produto, quantidade):
        if quantidade <= 0:
            raise ValueError("Quantidade deve ser positiva.")
        if produto in self.itens:
            self.itens[produto] += quantidade
        else:
            self.itens[produto] = quantidade

    def total(self):
        return sum(produto.preco * qtd for produto, qtd in self.itens.items())

    def mostrar(self):
        if not self.itens:
            print("Carrinho vazio.")
        else:
            for produto, qtd in self.itens.items():
                print(f"{produto.nome} x{qtd} = €{produto.preco * qtd:.2f}")
            print(f"Total: €{self.total():.2f}")

    def comprar(self):
        if not self.itens:
            raise ValueError("Carrinho vazio.")
        total_compra = self.total()
        self.itens.clear()
        return total_compra

def listar_produtos(produtos):
    for i, p in enumerate(produtos):
        print(f"{i + 1}. {p}")

def main():
    produtos = [
        Produto("Musculoso", 500),
        Produto("Calcesas", 10000),
        Produto("Carlos Barroso Gingeira", 1279)
    ]

    carrinho = Carrinho()

    while True:
        print("\n1. Listar Produtos")
        print("2. Adicionar ao Carrinho")
        print("3. Ver Carrinho")
        print("4. Comprar")
        print("0. Sair")

        try:
            opcao = input("Escolha: ")

            if opcao == "1":
                listar_produtos(produtos)

            elif opcao == "2":
                listar_produtos(produtos)
                idx = int(input("Número do produto: ")) - 1
                if idx < 0 or idx >= len(produtos):
                    raise ProdutoInexistenteError("Produto não encontrado.")
                qtd = int(input("Quantidade: "))
                carrinho.adicionar(produtos[idx], qtd)
                print(f"{produtos[idx].nome} adicionado!")

            elif opcao == "3":
                carrinho.mostrar()

            elif opcao == "4":
                if not carrinho.itens:
                    print("Carrinho vazio. Adicione produtos antes de comprar.")
                else:
                    total_compra = carrinho.comprar()
                    print(f"Compra realizada! Total: {total_compra:.2f}€")

            elif opcao == "0":
                print("Encerrando.")
                break

            else:
                print("Opção inválida.")

        except ValueError as ve:
            print(f"Erro: {ve}")
        except ProdutoInexistenteError as pe:
            print(f"Erro: {pe}")
        except Exception as e:
            print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()
