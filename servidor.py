import re

from pysimplesoap.server import SoapDispatcher, WSGISOAPHandler
from http.server import BaseHTTPRequestHandler, HTTPServer


class SOAPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """User viewable help information and wsdl"""
        args = self.path[1:].split("?")
        if self.path != "/" and args[0] not in self.server.dispatcher.methods.keys():
            self.send_error(404, "Method not found: %s" % args[0])
        else:
            if self.path == "/":
                # return wsdl if no method supplied
                response = self.server.dispatcher.wsdl()
            else:
                # return supplied method help (?request or ?response messages)
                req, res, doc = self.server.dispatcher.help(args[0])
                if len(args) == 1 or args[1] == "request":
                    response = req
                else:
                    response = res
        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()
        self.wfile.write(response)

    def do_POST(self):
        """SOAP POST gateway"""
        request = self.rfile.read(int(self.headers.get('content-length')))
        # convert xml request to unicode (according to request headers)
        encoding = self.headers.get_param("charset")
        request = request.decode(encoding)
        fault = {}
        # execute the method
        response = self.server.dispatcher.dispatch(request, fault=fault)
        # check if fault dict was completed (faultcode, faultstring, detail)
        if fault:
            self.send_response(500)
        else:
            self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()
        self.wfile.write(response)


# método com a implementação da operação/serviço
def is_par(in0):
    return in0 % 2 == 0


def is_cpf(in0: str) -> bool:
    """ Efetua a validação do CPF, tanto formatação quando dígito verificadores.

    Parâmetros:
        cpf (str): CPF a ser validado

    Retorno:
        bool:
            - Falso, quando o CPF não possuir o formato 999.999.999-99;
            - Falso, quando o CPF não possuir 11 caracteres numéricos;
            - Falso, quando os dígitos verificadores forem inválidos;
            - Verdadeiro, caso contrário.

    Exemplos:

    >>> is_cpf('529.982.247-25')
    True
    >>> is_cpf('52998224725')
    False
    >>> is_cpf('111.111.111-11')
    False
    """

    # Verifica a formatação do CPF
    if not re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', in0):
        return False

    # Obtém apenas os números do CPF, ignorando pontuações
    numbers = [int(digit) for digit in in0 if digit.isdigit()]

    # Verifica se o CPF possui 11 números ou se todos são iguais:
    if len(numbers) != 11 or len(set(numbers)) == 1:
        return False

    # Validação do primeiro dígito verificador:
    sum_of_products = sum(a * b for a, b in zip(numbers[0:9], range(10, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[9] != expected_digit:
        return False

    # Validação do segundo dígito verificador:
    sum_of_products = sum(a * b for a, b in zip(numbers[0:10], range(11, 1, -1)))
    expected_digit = (sum_of_products * 10 % 11) % 10
    if numbers[10] != expected_digit:
        return False

    return True


def calc(in0: int, in1: int, in2: str):
    if in2 == '+':
        return in0 + in1
    if in2 == '-':
        return in0 - in1
    if in2 == '*':
        return in0 * in1
    if in2 == '/':
        return in0 / in1
    if in2 == '%':
        return in0 % in1
    return None


# criação do objeto soap
dispatcher = SoapDispatcher('AbcBolinhas', location='http://localhost:8888/', action='http://localhost:8888/',
                            namespace="http://localhost:8888/", prefix="ns0",
                            documentation='Exemplo usando SOAP através de PySimpleSoap', trace=True, debug=True,
                            ns=True)
# publicação do serviço, com seu alias, retorno e parâmetros
dispatcher.register_function('verifica_NumeroPar', is_par, returns={'out0': bool}, args={'in0': int})
dispatcher.register_function('verifica_CPF', is_cpf, returns={'out0': bool}, args={'in0': str})
dispatcher.register_function('verifica_Calculo', calc, returns={'out0': float}, args={'in0': int, 'in1': int, 'in2': str})


def main():
    httpd = HTTPServer(("", 8888), SOAPHandler)
    httpd.dispatcher = dispatcher
    httpd.serve_forever()


if __name__ == '__main__':
    main()
