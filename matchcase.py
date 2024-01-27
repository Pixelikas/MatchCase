# Exemplo de match / case com number

numero = int(input('Digite um número de 1 a 3: '))

match(numero):
    
    case 1:
        print('Você digitou um!')
        
    case 2:
        print('Você digitou dois!')

    case 3:
        print('Você digitou três!')
        
    case _:
        print('São aceitos apenas os números 1, 2 e 3.')
                

# Exemplo de match / case com string

nome = input('Digite um nome: ')

match(nome):
    
    case 'Abgail':
        
        print('O nome digitado foi Abgail!')
        
    case 'Lucas':
        
        print('O nome digitado foi Lucas!')
        
    case 'Ursula':
        
        print('O nome digitado foi Ursula!')
        
    case other:
        
        print('O nome digitado não foi Abgail, nem Lucas, nem Ursula!')