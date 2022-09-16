
# Criando a classe "Cadastro" na qual possui 4 funções que serão as 4 opções que o usuário tem ao usar a agenda
class Cadastro:

    def __init__(self):
        self.lista_contato = {}

    def Adicionar(self):
        nome = input("Digite o nome do contato:\n")
        idade = input("Digite a idade do contato:\n")
        telefone = input("Digite o telefone do contato:\n")
        endereco = input("Digite o endereco do contato:\n")

        if nome in self.lista_contato:
            print("Esse nome já existe na lista")

        else:
            self.lista_contato[nome] = [idade,telefone,endereco]
            print("O contato",nome,"foi adicionado com sucesso")


    def Buscar(self,nome):
        self.nome = nome
        
        if self.nome in self.lista_contato:
            print("Informações do contato",self.nome)
            print(self.lista_contato[self.nome])

        else:
            print("Esse contato não existe")

    def Deletar(self,nome):
        self.nome = nome
        
        if self.nome in self.lista_contato:
            del self.lista_contato[self.nome]
            print("Esse contato acaba de ser deletado")

        else:
            print("Esse nome não existe na lista")

    def Listar(self):
        nomes = list(self.lista_contato.keys())
        i = 0
        while i < len(nomes):
            print(nomes[i])
            print(self.lista_contato[nomes[i]])
            i = i + 1



    


        


    

