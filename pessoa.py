from menus import Menu
from produtos import Produtos

class Pessoa:
    pass



class Cliente(Pessoa):
    def listar(self):
        produtos_carregados = Produtos.carregar('db.json')
        for produto in produtos_carregados:
            print(produto.nome, produto.preco)

class Admin(Pessoa):
    def __init__(self, p_user='admin', p_senha='123456'):
        self.user = p_user
        self.senha = p_senha
    
    def valida(self):
        user, senha = Menu.log_admin()
        
        if self.user == user and self.senha == senha:
            print("Senha e usuário corretos")
            print("Você está logado como administrador")
            retorno = 'correto'
        else:
            retorno = 'incorreto'
        
        return retorno