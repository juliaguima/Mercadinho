from menus import Menu
from pessoa import Pessoa
from estoque import CarrinhoDeCompras
from produtos import Produtos
from pessoa import Admin,Cliente
from estoque import Estoque

class Mercado():
    try:
        carrinho = CarrinhoDeCompras('carrinho.json')                       
        carrinho.produtos = []
        carrinho.salvar_carrinho()
        while True:
            while True:
                acesso = Menu.inicial()
                
                if acesso == 1:
                    Menu.log_cliente()
                    
                    while True:
                        while True:
                            menu_op = Menu.opcoes_cliente()

                            if menu_op == 1:
                                print("Lista de produtos: ")
                                Estoque.listar()
                                print("." * 50)

                            elif menu_op == 2:
                                Estoque.filtrar_produtos()

                            elif menu_op == 3:  # Adicionar ao carrinho
                                carrinho = CarrinhoDeCompras('carrinho.json')
                                addprod = input("Digite o nome do produto a ser adicionado:  ")
                                carrinho.adicionar_por_nome(addprod, 'db.json')

                            elif menu_op == 4:  # Visualizar carrinho
                                carrinho = CarrinhoDeCompras('carrinho.json')
                                carrinho.exibir()

                            elif menu_op == 5:  # Alterar quantidade
                                carrinho = CarrinhoDeCompras('carrinho.json')
                                produto = input("Digite o nome do produto para alterar a quantidade:  ")
                                quantidade = int(input("Digite a quantidade a ser alterada:  "))
                                carrinho.alterar_quantidade(produto, quantidade)

                            elif menu_op == 6:  # Remover produto
                                carrinho = CarrinhoDeCompras('carrinho.json')
                                produtorem = input("Digite o nome do produto a ser removido:  ")
                                carrinho.excluir_item(produtorem)

                            elif menu_op == 7:  # Finalizar compra
                                    while True:
                                        carrinho = CarrinhoDeCompras('carrinho.json')
                                        carrinho.finalizar_compra()
                                        carrinho.produtos = []
                                        carrinho.salvar_carrinho()
                                        break
                                
                            
                                
                            elif menu_op == 8:
                                    break
                                

                            else:
                                print("Opção inválida")
                                break

                elif acesso == 2:
                    while True:
                        while True:
                            adm = Admin()
                            retorno = adm.valida()

                            if retorno == 'correto':
                                while True:
                                    menu_op = Menu.opcoes_admin()

                                    if menu_op == 1:
                                        print("\n\t\t\t\t LISTAR")
                                        while True:
                                            Estoque.listar()
                                            break

                                    elif menu_op == 2:
                                        print("FUNÇÃO ALTERAR")
                                        while True:
                                            Estoque.alterar()
                                            break

                                    elif menu_op == 3:
                                        print("FUNÇÃO EXCLUIR")
                                        while True:
                                            Estoque.excluir()
                                            break

                                    elif menu_op == 4:
                                        while True:
                                            Estoque.adicionar_supridor()
                                            break

                                    elif menu_op == 5:
                                        break

                                    else:
                                        print("\n\t\t\t\t OPÇÃO INVÁLIDA, DIGITE NOVAMENTE")
                                break

                            else:
                                print("\n\t\t\tUsuário ou senha incorretos! Digite novamente")

                        break

                elif acesso == 3:
                    break

                else:
                    print("\n\t\t\t ------ Opção inválida, digite novamente! ----- ")
    except:
        ValueError
