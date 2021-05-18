from pysimplesoap.client import SoapClient
import json

client = SoapClient(wsdl="http://localhost:8888")

action = input('Digite "cpf" para validar um cpf, "calc" para realizar uma conta e qualquer outra coisa para sair:\n')
while (action == "cpf" or action == "calc"):
    if action == "cpf":
        val3 = input('Digite um CPF para validar (com pontuação): ')
        #val3 = '529.982.247-25'
        print(val3 + ' é um CPF ' + ('válido' if client.verifica_CPF(val3)['out0'] else 'inválido'))
    else:
        val5 = input('Digite o primeiro número: ')
        val6 = input('Digite o segundo número: ')
        val7 = input('Digite o operador (+ - * / %): ')
        print('{} {} {} = {}'.format(val5, val7, val6, client.verifica_Calculo(val5, val6, val7)['out0']))
    action = input('Digite "cpf" para validar um cpf, "calc" para realizar uma conta e qualquer outra coisa para sair:\n')


