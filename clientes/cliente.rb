require 'savon'

client = Savon.client(wsdl: "http://127.0.0.1:8888")


val1 = 10
response = client.call(:verifica_numero_par, message: { in0: val1 })
print("#{val1} é " + (response.body[:verifica_numero_par_response][:out0] ? "par \n" : "impar \n"))

val2 = 11
response = client.call(:verifica_numero_par, message: { in0: val2 })
print("#{val2} é " + (response.body[:verifica_numero_par_response][:out0] ? "par \n" : "impar \n"))

val3 = '529.982.247-25'
response = client.call(:verifica_cpf, message: { in0: val3 })
print("#{val3} é um CPF " + (response.body[:verifica_cpf_response][:out0] ? "válido \n" : "inválido \n"))

val4 = '111.111.111-11'
response = client.call(:verifica_cpf, message: { in0: val4 })
print("#{val4} é um CPF " + (response.body[:verifica_cpf_response][:out0] ? "válido \n" : "inválido \n"))

val5 = 10
val6 = 5
val7 = '*'
response = client.call(:verifica_calculo, message: { in0: val5, in1: val6, in2: val7 })
res1 = response.body[:verifica_calculo_response][:out0]
print("#{val5} #{val7} #{val6} = #{res1} \n")

val8 = 10
val9 = 5
val10 = '/'
response = client.call(:verifica_calculo, message: { in0: val8, in1: val9, in2: val10 })
res2 = response.body[:verifica_calculo_response][:out0]
print("#{val8} #{val10} #{val9} = #{res2} \n")