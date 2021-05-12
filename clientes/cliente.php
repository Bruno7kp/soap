<?php

$client = new SoapClient('http://localhost:8888');

$val1 = 10;
$result = $client->verifica_NumeroPar(['in0' => $val1]);
print("$val1 é " . ($result->out0 ? 'par' : 'impar') . "\n");

$val2 = 11;
$result = $client->verifica_NumeroPar(['in0' => 11]);
print("$val2 é " . ($result->out0 ? 'par' : 'impar') . "\n");

$val3 = '529.982.247-25';
$result = $client->verifica_CPF(['in0' => $val3]);
print("$val3 é um cpf " . ($result->out0 ? 'válido' : 'inválido') . "\n");

$val4 = '111.111.111-11';
$result = $client->verifica_CPF(['in0' => $val4]);
print("$val4 é um cpf " . ($result->out0 ? 'válido' : 'inválido') . "\n");

$val5 = 10;
$val6 = 5;
$val7 = '*';
$result = $client->verifica_Calculo(['in0' => $val5, 'in1' => $val6, 'in2' => $val7]);
print("$val5 $val7 $val6 = " . $result->out0 . "\n");

$val8 = 10;
$val9 = 5;
$val10 = '/';
$result = $client->verifica_Calculo(['in0' => $val8, 'in1' => $val9, 'in2' => $val10]);
print("$val8 $val10 $val9 = " . $result->out0 . "\n");
