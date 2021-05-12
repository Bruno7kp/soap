from pysimplesoap.client import SoapClient
import json

client = SoapClient(wsdl="http://localhost:8888")

val1 = 10
print('%s é ' % val1 + ('par' if client.verifica_NumeroPar(val1)['out0'] else 'impar'))

val2 = 11
print('%s é ' % val2 + ('par' if client.verifica_NumeroPar(val2)['out0'] else 'impar'))

val3 = '529.982.247-25'
print(val3 + ' é um CPF ' + ('válido' if client.verifica_CPF(val3)['out0'] else 'inválido'))

val4 = '111.111.111-11'
print(val4 + ' é um CPF ' + ('válido' if client.verifica_CPF(val4)['out0'] else 'inválido'))

val5 = 10
val6 = 5
val7 = '*'
print('{} {} {} = {}'.format(val5, val7, val6, client.verifica_Calculo(val5, val6, val7)['out0']))


val8 = 10
val9 = 5
val10 = '/'
print('{} {} {} = {}'.format(val8, val10, val9, client.verifica_Calculo(val8, val9, val10)['out0']))
