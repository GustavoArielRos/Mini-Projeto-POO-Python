
# Aqui onde realmente ocorre a interação do programa com o usuário
# Importando a classe Cadastro
from cadastro import Cadastro

agenda = Cadastro()

resposta = input("Bem-vindo a agenda virtual, caso queira usá-la digite 'sim':\n")

while resposta == 'sim':
    resposta2 = input("Digite 'adicionar' para adicionar um contato\nDigite 'buscar' para buscar um contato\nDigite 'listar' para listar todos os contatos\nDigite 'deletar' para deletar um contato\n")
    
    if resposta2 == 'adicionar':
        agenda.Adicionar()

    if resposta2 == 'buscar':
        nome = input("Digite o nome do contato:\n")
        agenda.Buscar(nome)

    if resposta2 == 'listar':
        agenda.Listar()
    
    if resposta2 == 'deletar':
        nome = input("Digite o nome do contato:\n")
        agenda.Deletar(nome)

    resposta = input("Bem-vindo a agenda virtual, caso queira usá-la digite 'sim':\n")


                      
 