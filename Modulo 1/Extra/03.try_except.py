# Crie uma função chamada calculadora que receba 3 parãmetros
# Dois numeros e uma operação + - 8 ou % 
# a função deve retornar o resultado da operação mas precisa tratar
# as seguintes exceções
# Divisão por zero (zerodivisionerror)
# tipo de dado invaçido (valeuerror)
def calculadora():
    try:
        n = input('Digite um número ou x para sair do sistema:  ')
        if n.lower() == 'x':
            print('Até breve')
            return
        n1 = input('Digite um número ou x para sair do sistema: ')
        if n1.lower() == 'x':
            print('Até breve')
            return
        operador = input('Informe um operador matemático (+, *, -, /): ')
        if operador.lower() == 'x':         
            print('Até breve')
            return

        # Converter para float depois das checagens
        n = float(n)
        n1 = float(n1)

        if operador == '+':
            resultado = n + n1
        elif operador == '-':
            resultado = n - n1  # corrigido aqui
        elif operador == '*':
            resultado = n * n1  # corrigido aqui
        elif operador == '/':
            if n1 == 0:
                raise ZeroDivisionError('Não foi possível dividir por zero')
            resultado = n / n1
        else:
            print('Você escolheu algo inválido.')
            return

        print(f'Operação {n} {operador} {n1} = {resultado}')
    except ValueError:
        print('Você digitou um caractere inválido, digite somente números.')
    except ZeroDivisionError as zero:
        print(zero)

calculadora()
