


class Produtos():

        def __init__(self, p_nome:str, p_preco:float, p_tipo:str, p_descricao:str, p_composicao:str, p_quant:int, p_idade:bool) -> None:
            
            self.nome = p_nome
            self.preco = p_preco
            self.tipo = p_tipo
            self.descricao = p_descricao
            self.composicao = p_composicao
            self.quantidade = p_quant
            self.idade = p_idade


        def dict(self):
            
            return  {'nome' : self.nome,'preco' : self.preco,
                    'tipo' : self.tipo,'descricao' : self.descricao,
                    'composicao' : self.composicao,'quantidade' : self.quantidade,
                    'idade' : self.idade  }        
        

