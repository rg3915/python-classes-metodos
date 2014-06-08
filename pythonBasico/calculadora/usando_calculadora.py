# -*- coding: utf-8 -*-
from calculadora import Calculadora

c = Calculadora(128,2)

print 'Soma:', c.soma()
print 'Subtração:', c.subtrai()
print 'Multiplicação:', c.multiplica()
print 'Divisão:', c.divide()

c.a = 12
c.b = 42

print c.soma()