
class RomanoInvalido(Exception):
    pass

class SequenciaInvalida(RomanoInvalido):
    pass

class CaracterInvalido(RomanoInvalido):
    pass

def convert(alg):
    soma = 0

    dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    l_valido = set([4, 9, 40, 90])

    for carac in alg:
        if carac not in dic:
            raise CaracterInvalido('Caractere invalido: '+ carac)
    

    anterior = 0
    for carac in reversed(alg):
        if anterior <= dic[carac]:
            soma += dic[carac]
        else:
            if anterior - dic[carac] in l_valido:
                soma -= dic[carac]
            else:
                raise SequenciaInvalida('Sequencia invalida')
        anterior = dic[carac]

    return soma