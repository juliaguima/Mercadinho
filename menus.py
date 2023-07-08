
from datetime import datetime
import json



class Menu():

    
    
    # menu de login incial  
    def inicial():
        print('\n\t\t\t🛒 Seja bem-vindo(a) ao Mercadinho do seu Zé 🛒')
        acesso = int(input('\t\t\t\t\tAcessar como : \n\n\t\t\t\t ✿  Cliente (digite 1)\n\t\t\t\t ✿  Supridor (digite 2)\n\t\t\t\t ✿  Sair (digite 3)\n\n\t\t➫  '))
        return acesso
    

    def validar_data_nascimento(data_nascimento):
        try:
            data = datetime.strptime(data_nascimento, "%d/%m/%Y")
            # Verificar se a data é anterior à data atual
            if data > datetime.now():
                return False
            return True
        except ValueError:
            return False
    # menu de login do cliente (validar) 
    
    def log_cliente():
        
        print('\n\t\t\t  ............  Login cliente ..............')
        nome = input("\n\t\t\t ✒️  Nome: ")
        while True:
            datanasc = input("\n\t\t\t 🚼  Data de nascimento (dd/mm/aaaa): ")
            if Menu.validar_data_nascimento(datanasc):
                break
            else:
                print("\n\t\t\tData de nascimento inválida. Por favor, digite novamente.")
        endereco = input("\n\t\t\t 🏘️  Endereço : ")
        print(f'Seja bem vindo(a) {nome}')
        dados_cliente = {
                'nome': nome,
                'datanasc': datanasc,
                'endereco': endereco
            }

            
        with open('dados_cliente.json', 'w') as file:
                json.dump(dados_cliente, file)

        return nome, datanasc, endereco
            

    def opcoes_cliente():
        print("\n\t\t\t\t O que você deseja realizar?  ")                                                                                       
        menu_op = int(input("\n\t\t\t\t ✿ Listar produtos   (1)\n\t\t\t\t ✿ Filtrar produto   (2)\n\t\t\t\t ✿ Adicionar produto ao carrinho  (3)\n\t\t\t\t ✿ Visualizar carrinho  (4)\n\t\t\t\t ✿ Alterar quantidade(5)\n\t\t\t\t ✿ Remover produto do carrinho  (6)\n\t\t\t\t ✿ Finalizar compra   (7)\n\t\t\t\t ✿ Abandonar carrinho   (8)\n\t\t\t>>>  "))
        return menu_op    


    # menu de login do funcionario (validar) 
    def log_admin():
        print('\n\t\t\t  ............  Login de supridor ..............')
        user =  input ("\n\t\t\t 👤  Usuário:  ")
        senha = input ("\t\t\t 🔒  Senha: ")
        return user,senha
    
    def opcoes_admin():
        print("\n\t\t\t\t O que você deseja realizar?  ")
        menu_op = int(input("\n\t\t\t\t ✿ Listar produtos   (1)\n\t\t\t\t ✿ Alterar produto   (2)\n\t\t\t\t ✿ Excluir produto   (3)\n\t\t\t\t ✿ Adicionar produto (4)\n\t\t\t\t ✿ Sair (5)\n\t\t\t>>>  "))
        return menu_op


    
    

    def adiconar_novo():
        print("\n\t\t\t  ............  Cadastrando um novo produto ..............")
        
        nomeadd = input("\n\t\t\t Nome:  ")
        precoadd = float(input("\n\t\t\t Preço:  "))
        tipoadd = input("\n\t\t\t Tipo:  ")
        descricaoadd = input("\n\t\t\t Descrição:  ")
        quantadd = int(input("\n\t\t\t Quantidade:  "))
        idadeb = True
        def split_input(input_string):
                words = []
                current_word = ''
                for char in input_string:
                    if char != ' ':
                        current_word += char
                    elif current_word:
                        words.append(current_word)
                        current_word = ''
                if current_word:
                    words.append(current_word)
                return words

        composicaoadd = split_input(input("\n\t\t\t Composição: "))

        return nomeadd,precoadd,tipoadd,descricaoadd,composicaoadd,quantadd,idadeb
        # idade = bool

    def excluir_sel():
        print("\n\t\t\t  ............  Excluindo produto ..............")
        nomedel = input("Digite o nome do produto a ser excluído:  ")
        return nomedel
    
    def alterar_sel():
        print("\n\t\t\t  ............  Editando produto ..............")
        nomedel = input("Digite o nome do produto a ser alterado:  ")
        return nomedel


    def filtra_prod():
        op = int(input("Você deseja filtrar pela composição (1) ou pelo nome (2)? "))

        if op == 1:
            composicao_filtrada = input("Filtrar por qual componente? ")
            nome_filtrado = None
        elif op == 2:
            nome_filtrado = input("Digite o nome a ser filtrado: ")
            composicao_filtrada = None
        else:
            print("Opção inválida")
            composicao_filtrada = None
            nome_filtrado = None

        return composicao_filtrada, nome_filtrado
    
