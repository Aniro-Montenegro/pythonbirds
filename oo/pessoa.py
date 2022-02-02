class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    marisa = Pessoa(nome='Marisa')
    aniro = Pessoa(marisa, nome='Aniro')
    print(Pessoa.cumprimentar(aniro))
    print(id(aniro))
    print(aniro.cumprimentar())
    print(aniro.nome)
    print(aniro.idade)
    for filho in aniro.filhos:
        print(filho.nome)
    aniro.sobrenome = 'Montenegro'
    print(aniro.__dict__)
    print(marisa.__dict__)
    del aniro.filhos
    print(aniro.__dict__)
    print(marisa.__dict__)
    print(Pessoa.olhos)
    print(aniro.olhos)
    print(marisa.olhos)
    print(id(Pessoa.olhos))
    print(id(aniro.olhos))
    print(id(marisa.olhos))
    aniro.olhos=1
    print(aniro.__dict__)
    print(marisa.__dict__)
    Pessoa.olhos=3
    print(Pessoa.olhos)
    print(aniro.olhos)
    print(marisa.olhos)
    print(aniro.__dict__)
    print(marisa.__dict__)
