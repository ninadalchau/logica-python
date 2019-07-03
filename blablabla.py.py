# Avaliação de Programação
# Resolva esses exercícios sem usar if, for ou while.
# Utilize apenas fatiamento, funções embutidas e métodos dos
# objetos string, lista, dicionário, etc.

def soma_tres_inteiros(a, b, c):
    """ Recebe três números inteiros, e retorna a sua soma"""
    return a + b + c

def preco_com_desconto(preco, percentual):
    """ Recebe um preço e sua porcentagem de desconto, e retorna
    novo preço"""
    return round(preco - (preco * percentual/100), 2)


def aluguel_airbnb(valor_diaria, dias):
    """ Recebe uma quantidade de dias que ficou hospedado e o valor da
    diária, e retorna o valor a ser pago, considerando um acréscimo de
    R$ 75,00 para limpeza e 5% de taxa de administração sobre o valor
    do aluguel sem a taxa de limpeza"""
    pagar = valor_diaria * dias
    return pagar + 75 + (pagar * 0.05)


def media_final_aprovado_reprovado(prova, exercicio, projeto):
    """ Recebe as notas de 1 prova, 1 exercício e 1 projeto, e retorna
    se o aluno foi ou não aprovado. A prova tem peso 4, o exercício
    tem peso 1, e o projeto tem peso 3."""
    nota1 = prova * 4
    nota2 = exercicio * 1
    nota3 = projeto * 3
    mediafinal = (nota1 + nota2 + nota3) / 8
    return mediafinal >= 7

def troca_caixa(texto):
    """Vogais ficam em caixa baixa (minúsculas)
    Consoantes ficam em caixa alta (maiúsculas)"""
    texto = texto.upper()
    texto = texto.replace("A", "a")
    texto = texto.replace("E", "e")
    texto = texto.replace("I", "i")
    texto = texto.replace("O", "o")
    texto = texto.replace("U", "u")
    return texto

def encontra_caracter(texto, caracter_procurado):
    """Receba um texto e retorne a localização da primeira vez que
    aparece o caracter especificado"""
    return texto.find(caracter_procurado, 1)

def é_sortudo(numero):
    """O último dígito deve ser igual ao primeiro, e ao elemento do meio."""
    return numero[-1]==numero[0]==numero[len(numero) // 2]

def media_saltos_lista(saltos):
    """Receba uma lista com os saltos de um atleta e calcule a média
    dos seus saltos.
    """
    return round((saltos[0] + saltos[1] + saltos[2] + saltos[3] + saltos[-1]) / 5, 2)


def mes_extenso(mes):
    """Receba um número correspondente ao mês e devolva o nome do mês.
    Ex.: 1-janeiro, 2-fevereiro, ..., 12-dezembro.
    Use um dicionário com os nomes dos meses."""
    meses = {
        1:"janeiro",
        2:"fevereiro",
        3:"março",
        4:"abril",
        5:"maio",
        6:"junho",
        7:"julho",
        8:"agosto",
        9:"setembro",
        10:"outubro",
        11:"novembro",
        12:"dezembro",
    }
    return meses[mes]


def insere(texto, posicao, texto_inserir):
    """
    Insira na posição especificada o novo texto.
    """
    texto.insert(posicao, texto_inserir)
    return texto[:posicao] + texto_inserir[:posicao + 2] + texto[posicao:]

# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % 'Falhou'
    else:
        prefixo = '\033[32m%s' % 'Passou'
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():

    print('Soma três inteiros:')
    test(soma_tres_inteiros(0, 0, 0), 0)
    test(soma_tres_inteiros(-1, 0, 0), -1)
    test(soma_tres_inteiros(10, 10, 10), 30)
    test(soma_tres_inteiros(-10, -10, -10), -30)

    print('Desconto do preco atual baseado na porcentagem do desconto:')
    test(preco_com_desconto(1330, 20), 1064.00)
    test(preco_com_desconto(1000, 0), 1000.00)
    test(preco_com_desconto(1000.10, 5.5), 945.09)
    test(preco_com_desconto(0.0, 200), 0.00)

    print('Preco a pagar pelo aluguel do airBnB:')
    test(aluguel_airbnb(100, 1), 180.00)
    test(aluguel_airbnb(100, 2), 285.00)
    test(aluguel_airbnb(200, 10), 2175.00)
    test(aluguel_airbnb(50, 5), 337.50)

    print('Média final:')
    test(media_final_aprovado_reprovado(10, 10, 10), True)
    test(media_final_aprovado_reprovado(8, 7, 6), True)
    test(media_final_aprovado_reprovado(8, 7, 5), False)
    test(media_final_aprovado_reprovado(5, 5, 5), False)
    test(media_final_aprovado_reprovado(7, 7, 7), True)

    print(' Troca caixa:')
    test(troca_caixa("Araquari"), "aRaQuaRi")  # normal
    test(troca_caixa("Caxias do Sul"), "CaXiaS Do SuL")  # com espaços

    print(' Encontra caracter:')
    test(encontra_caracter("--*--", "*"), 2)
    test(encontra_caracter("19/05/2014", "/"), 2)
    test(encontra_caracter("Avaliação de Programação", "P"), 13)

    print(' É sortudo:')
    test(é_sortudo('2132452'), True)
    test(é_sortudo('23141'), False)
    test(é_sortudo('31213145563'), False)
    test(é_sortudo('3455133453341'), False)
    test(é_sortudo('3455133453343'), True)

    print(' Média dos saltos em lista:')
    test(media_saltos_lista([10, 10, 10, 10, 10]), 10)
    test(media_saltos_lista([9, 9.1, 8, 7, 6.9]), 8)
    test(media_saltos_lista([1, 1, 3, 5, 5]), 3)
    test(media_saltos_lista([10, 10, 9.9, 10, 10]), 9.98)
    test(media_saltos_lista([1, 4.5, 0, 7, 5]), 3.5)

    print('Mês por extenso:')
    test(mes_extenso(1), 'janeiro')
    test(mes_extenso(3), 'março')
    test(mes_extenso(12), 'dezembro')

    print('Apaga')
    test(insere('kitten', 3, 'i'), 'kititen')
    test(insere('nasci', 2, 'i'), 'naisci')
    test(insere('code', 0, 'vs'), 'vscode')
    test(insere('code', 1, 'h'), 'chode')
    test(insere('chocolate', 9, 's'), 'chocolates')


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (
        total, acertos, total - acertos, float(acertos * 10) / total)
          )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")