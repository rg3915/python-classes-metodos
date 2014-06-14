# -*- coding: utf-8 -*-
class User(object):

    # Define um atributo que servirá como contador inicial e um atributo objects
    # (tupla vazia) que é uma lista de instâncias de User que foram salvos
    # (que chamaram o método save).
    seq = 0
    objects = []

    # Atribui um valor inicial aos atributos no momento da chamada do
    # construtor.
    def __init__(self, nome, idade):
        # inicializando os atributos, id começa com None, pois a instância foi
        # criada mas ainda não foi salva.
        self.id = None
        self.nome = nome
        self.idade = idade

    # Método para salvar os dados
    # ele incrementa o atributo de classe que conta quantas instâncias
    # foram salvas e adiciona a instância na lista de objects.
    def save(self):
        # self.__class__ acessa a classe que criou a instância, assim é possível
        # acessar o atributo de seq. Aqui poderia ser usado User.seq,
        # porém caso User fosse herdado, o seq seria o de User e não da classe
        # filha.
        self.__class__.seq += 1
        self.id = self.__class__.seq
        # Da mesma forma que acessamos seq, acessamos objects e é feito um
        # append com a instância.
        self.__class__.objects.append(self)

    # Retorna uma representação do objeto como str, usado em conversões para string.
    # Exemplo: str(my_user), print my_user
    def __str__(self):
        return self.nome

    # Retorna uma representação do objeto usada para outros objetos.
    # Exemplo: quando é convertida uma lista de user para string.
    def __repr__(self):
        # self.__class__.__name__ é a forma de acessar o nome da classe que
        # gerou a instância.
        return '<{}: {} - {} - {}>\n'.format(self.__class__.__name__, self.id, self.nome, self.idade)

    # Class method usado para acessar todas as instâncias salvas (que chamaram o método save).
    # Aqui usamos um @classmethod, pois faz mais sentido ser um método de classe
    # do que de instância, pois estamos retornando informações da classe
    # e não de uma instância isolada.
    @classmethod
    def all(cls):
        return cls.objects

# Demonstração do uso da classe.
if __name__ == '__main__':
    u1 = User('Regis', 35)
    u2 = User('Fabio', 20)
    # Note que nesse print a lista está vazia
    print(User.all())
    u1.save()
    u2.save()
    # Após chamar o save para as duas instâncias elas são guardadas
    # e o método User.all() retorna essa lista.
    print(User.all())
