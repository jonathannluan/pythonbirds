class Pessoa:
    def __init__(self,nome=None,idade=35):
        self.idade = idade
        self.nome=nome
    def cumprimentar(self):
        return f'Olá'


if __name__ == '__main__':
    p= Pessoa('Luan')
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)