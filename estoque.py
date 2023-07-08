import json
from produtos import Produtos
from menus import Menu



class Estoque():
    

#ADICIONAR PRODUTOS

    def adicionar_supridor():
            produtos = []  

            while True:
                nomeadd, precoadd, tipoadd, descricaoadd, composicaoadd, quantadd, idadeb = Menu.adiconar_novo()
                produto = Produtos(nomeadd, precoadd, tipoadd, descricaoadd, composicaoadd, quantadd, idadeb)
                produtos.append(produto.dict())

                op = input("Deseja adicionar mais produtos? (S/N): ")
                if op.upper() != 'S':
                    break

            with open('db.json', 'r') as db:
                dados = json.load(db)
            dados.extend(produtos)
            with open('db.json', 'w') as db:
                json.dump(dados, db, indent=4)



 # LISTAR PRODUTOS

    @staticmethod
    def listar():
        with open('db.json', 'r') as db:
            dados = json.load(db)

        for produto in dados:
            print(f"Nome: {produto['nome']}")
            print(f"Preço: {produto['preco']}")
            print(f"Tipo: {produto['tipo']}")
            print(f"Descrição: {produto['descricao']}")
            print(f"Composição: {produto['composicao']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Idade: {produto['idade']}")
            print("." * 50)
            

    # EXCLUIR PRODUTOS
    
    @staticmethod
    def excluir():

        nomedel = Menu.excluir_sel()
        with open('db.json', 'r') as db:
            dados = json.load(db)

        for produto in dados:
            if produto['nome'] == nomedel:
                dados.remove(produto)
                print("Produto excluído com sucesso!")
                break
        else:
            print("Produto não encontrado!")
        with open('db.json', 'w') as db:
            json.dump(dados, db, indent=4)
                     
                 
    # ALTERAR PRODUTOS

    @staticmethod
    def alterar():
            nomealt = Menu.alterar_sel()
            with open('db.json', 'r') as db:
                dados = json.load(db)

    # Procurar pelo nome
            for produto in dados:
                if produto['nome'] == nomealt:
                    print("\nDados do produto: ")
                    print("Nome:", produto['nome'])
                    print("Preço:", produto['preco'])
                    print("Tipo:", produto['tipo'])
                    print("Descrição:", produto['descricao'])
                    print("Composição:", produto['composicao'])
                    print("Quantidade:", produto['quantidade'])

                    print("\nDigite os novos dados:")
                    produto['nome'] = input("Novo nome: ")
                    produto['preco'] = float(input("Novo preço: "))
                    produto['tipo'] = input("Novo tipo: ")
                    produto['descricao'] = input("Nova descrição: ")
                    produto['composicao'] = input("Nova composição: ")
                    produto['quantidade'] = int(input("Nova quantidade: "))

                    print("Produto alterado com sucesso!")
                    break
            else:
                print("Produto não encontrado!")

            with open('db.json', 'w') as db:
                json.dump(dados, db, indent=4)  


    # FILTRAR PRODUTOS (Nome,composição)

    @staticmethod
    def filtrar_produtos():
        composicao_filtrada, nome_filtrado = Menu.filtra_prod()
        composicao_filtrada = [comp.strip() for comp in composicao_filtrada.split(",")] if composicao_filtrada else []

        with open('db.json', 'r') as db:
            dados = json.load(db)

        produtos_filtrados = []
        for produto in dados:
            if (not composicao_filtrada or all(comp in produto['composicao'] for comp in composicao_filtrada)) and \
                    (not nome_filtrado or produto['nome'] == nome_filtrado):
                produtos_filtrados.append(produto)

        if produtos_filtrados:
            print("\nProdutos encontrados:")
            print("." * 50)
            for produto in produtos_filtrados:
                print("\nNome:", produto['nome'])
                print("\nPreço:", produto['preco'])
                print("\nTipo:", produto['tipo'])
                print("\nDescrição:", produto['descricao'])
                print("\nComposição:", produto['composicao'])
                print("\nQuantidade:", produto['quantidade'])
                print("." * 50)
        else:
            print("Nenhum produto encontrado.")
        



        

class CarrinhoDeCompras():
    def __init__(self, arquivo_carrinho):
        self.arquivo_carrinho = arquivo_carrinho
        self.produtos = self.carregar_carrinho()

    def carregar_carrinho(self):
        try:
            with open(self.arquivo_carrinho, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def salvar_carrinho(self):
        with open(self.arquivo_carrinho, 'w') as file:
            json.dump(self.produtos, file, indent=4)



    def adicionar_por_nome(self, nome_produto, arquivo_estoque):
        with open(arquivo_estoque, 'r') as file:
            estoque = json.load(file)

        produto_encontrado = None
        for produto in estoque:
            if produto['nome'] == nome_produto:
                produto_encontrado = produto
                break
        
        if produto_encontrado is None:
            print(f'O produto "{nome_produto}" não está disponível no estoque.')
            return
        
        quantidade_disponivel = produto_encontrado['quantidade']
        if quantidade_disponivel == 0:
            print(f'O produto "{nome_produto}" está esgotado.')
            return
        
        while True:
            quantidade = input(f'Digite a quantidade de "{nome_produto}" a ser adicionada: ')
            if not quantidade.isdigit() or int(quantidade) <= 0:
                print('Quantidade inválida. Digite um número inteiro positivo.')
            else:
                quantidade = int(quantidade)
                if quantidade > quantidade_disponivel:
                    print(f'A quantidade disponível de "{nome_produto}" é inferior a {quantidade}.')
                else:
                    break
        
        for produto_carrinho in self.produtos:
            if produto_carrinho['nome'] == nome_produto:
                produto_carrinho['quantidade'] += quantidade
                break
        else:
            produto_carrinho = {
                'nome': produto_encontrado['nome'],
                'preco': produto_encontrado['preco'],
                'quantidade': quantidade
            }
            self.produtos.append(produto_carrinho)

       
        produto_encontrado['quantidade'] -= quantidade
        self.salvar_carrinho()

        print(f'Foram adicionadas {quantidade} unidades do produto "{nome_produto}" ao carrinho.')




    def exibir(self):
        print('Produtos no carrinho:')
        for produto in self.produtos:
            print(f'Nome: {produto["nome"]}, Preço: R${produto["preco"]}, Quantidade: {produto["quantidade"]}')

    def alterar_quantidade(self, nome_produto, nova_quantidade):
            produto_encontrado = None
            for produto in self.produtos:
                if produto['nome'] == nome_produto:
                    produto_encontrado = produto
                    break
            
            if produto_encontrado is None:
                print(f'O produto "{nome_produto}" não está no carrinho.')
                return

            if nova_quantidade < 1:
                print('A quantidade deve ser um valor positivo.')
                return

            produto_encontrado['quantidade'] = nova_quantidade
            self.salvar_carrinho()
            print(f'A quantidade do produto "{nome_produto}" foi alterada para {nova_quantidade}.')

    

    def excluir_item(self, nome_produto):
        produto_encontrado = None
        for produto in self.produtos:
            if produto['nome'] == nome_produto:
                produto_encontrado = produto
                break

        if produto_encontrado is None:
            print(f'O produto "{nome_produto}" não está no carrinho.')
            return

        self.produtos.remove(produto_encontrado)
        self.salvar_carrinho()
        print(f'O produto "{nome_produto}" foi removido do carrinho.')

        if not self.produtos:
            print("O carrinho está vazio.")


    def finalizar_compra(self):
        nota_fiscal = "nota_fiscal.txt"
        
        with open(nota_fiscal, 'w') as file:
            file.write("=== NOTA FISCAL ===\n")

            with open('dados_cliente.json', 'r') as client_file:
                dados_cliente = json.load(client_file)

                nome = dados_cliente['nome']
                datanasc = dados_cliente['datanasc']
                endereco = dados_cliente['endereco']

                file.write(f"Nome: {nome}\n")
                file.write(f"Data de Nascimento: {datanasc}\n")
                file.write(f"Endereço: {endereco}\n")

            file.write("==================\n")

            for produto in self.produtos:
                nome_produto = produto['nome']
                quantidade = produto['quantidade']
                valor_total = produto['preco'] * quantidade

                file.write(f"Produto: {nome_produto} | Quantidade: {quantidade} | Valor total: R$ {valor_total:.2f}\n")

            while True:
                forma_pagamento = int(input("Escolha a forma de pagamento (Digite 1 para pagamento à vista "
                                            "ou 2 para pagamento parcelado em até 12x): "))

                if forma_pagamento == 1:
                    valor_total = self.calcular_valor_total()
                    file.write(f"Valor total da compra à vista: R$ {valor_total:.2f}\n")
                    break
                elif forma_pagamento == 2:
                    vezes = int(input("Você deseja parcelar em quantas vezes? "))
                    parc = valor_total / vezes
                    file.write(f"Valor parcelado em {vezes}x: R$ {parc:.2f} por parcela\n")
                    break
                else:
                    print("Forma de pagamento inválida. Digite novamente.\n")


        print("\n=== Nota Fiscal ===\n")
        with open(nota_fiscal, 'r') as file:
            for line in file:
                print(line.strip())
        def calcular_valor_total(self):
                valor_total = 0.0
                for produto in self.produtos:
                    preco = produto['preco']
                    quantidade = produto['quantidade']
                    valor_total += preco * quantidade
                return valor_total

           
            

    def calcular_valor_total(self):
            valor_total = 0.0
            for produto in self.produtos:
                preco = produto['preco']
                quantidade = produto['quantidade']
                valor_total += preco * quantidade
            return valor_total


    









   