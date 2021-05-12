import zeep

client = zeep.Client(wsdl='http://127.0.0.1:8888')

val1 = 10
print('%s é ' % val1 + ('par' if client.service.verifica_NumeroPar(val1) else 'impar'))

val2 = 11
print('%s é ' % val2 + ('par' if client.service.verifica_NumeroPar(val2) else 'impar'))

val3 = '529.982.247-25'
print(val3 + ' é um CPF ' + ('válido' if client.service.verifica_CPF(val3) else 'inválido'))

val4 = '111.111.111-11'
print(val4 + ' é um CPF ' + ('válido' if client.service.verifica_CPF(val4) else 'inválido'))

val5 = 10
val6 = 5
val7 = '*'
print('{} {} {} = {}'.format(val5, val7, val6, client.service.verifica_Calculo(val5, val6, val7)))


val8 = 10
val9 = 5
val10 = '/'
print('{} {} {} = {}'.format(val8, val10, val9, client.service.verifica_Calculo(val8, val9, val10)))
