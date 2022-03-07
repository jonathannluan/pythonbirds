class Pessoa:
    def __init__(self,*filhos,nome=None,idade=35):
        self.filhos=list(filhos)
        self.idade = idade
        self.nome=nome
    def cumprimentar(self):
        return f'Olá'


if __name__ == '__main__':
    helena=Pessoa(nome='Helena')
    p= Pessoa(helena,nome='Luan')
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
    for n in p.filhos:
        print(n.nome)