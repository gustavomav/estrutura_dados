#5. Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método
#chamado “falar” que imprime uma mensagem com o nome da pessoa.

class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return print(f'Olá, sou o {self.nome} e tenho {self.idade} anos de idade')
    
pessoa1 = Pessoa('João',31)
pessoa1.falar()