var soap = require('soap');
var url = 'http://127.0.0.1:8888';

soap.createClient(url, function(err, client) {
  let args1 = {in0: 10};
  client.verifica_NumeroPar(args1, function(err, result) {
      console.log(args1.in0 + ' é ' + (result.out0 ? 'par' : 'impar'));
  });

  let args2 = {in0: 11};
  client.verifica_NumeroPar(args2, function(err, result) {
      console.log(args2.in0 + ' é ' + (result.out0 ? 'par' : 'impar'));
  });

  let args3 = {in0: '529.982.247-25'};
  client.verifica_CPF(args3, function(err, result) {
      console.log(args3.in0 + ' é um CPF ' + (result.out0 ? 'válido' : 'inválido'));
  });

  let args4 = {in0: '111.111.111-11'};
  client.verifica_CPF(args4, function(err, result) {
      console.log(args4.in0 + ' é um CPF ' + (result.out0 ? 'válido' : 'inválido'));
  });

  let args5 = {in0: 10, in1: 5, in2: '*'};
  client.verifica_Calculo(args5, function(err, result) {
      console.log(args5.in0 + args5.in2 + args5.in1 + ' = ' + result.out0);
  });

  let args6 = {in0: 10, in1: 5, in2: '/'};
  client.verifica_Calculo(args6, function(err, result) {
      console.log(args6.in0 + args6.in2 + args6.in1 + ' = ' + result.out0);
  });
});