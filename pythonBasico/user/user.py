# -*- coding: utf-8 -*-
class User(object):

    seq = 0
    objects = []

    def __init__(self, nome, idade):
        self.id = None
        self.nome = nome
        self.idade = idade

    def save(self):
        self.__class__.seq += 1
        self.id = self.__class__.seq
        self.__class__.objects.append(self)

    def __str__(self):
        return self.nome

    def __repr__(self):
        return '<{}: {} - {} - {}>\n'.format(self.__class__.__name__, self.id, self.nome, self.idade)

    @classmethod
    def all(cls):
        return cls.objects

if __name__ == '__main__':
    u1 = User('Regis', 35)
    u1.save()
    u2 = User('Fabio', 20)
    u2.save()
    print(User.all())
