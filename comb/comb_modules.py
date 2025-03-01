# -*- coding: utf-8 -*-
"""Exercice 1

Implemente a equacão:

q = a or !b
"""


from myhdl import *


@block
def exe1(q, a, b):
    """
    q = a or !b
    """

    @always_comb
    def comb():
        q.next = a or (not b)

    return instances()


@block
def exe2(q, a, b, c):
    """
    Implemente a tabela verdade a seguir:

    A B C | Q
    ------|--
    0 0 0 | 1
    0 0 1 | 0
    0 1 0 | 0
    0 1 1 | 1
    1 0 0 | 1
    1 0 1 | 0
    1 1 0 | 0
    1 1 1 | 1

    Não utilize IF!
    """

    @always_comb
    def comb():
        q.next = ((not b) and (not c)) or (b and c)

    return instances()


@block
def exe3(q, a, b, c, d, e):
    """
    Exercice 3

    Implemente o circuito lógico a seguir:

                __
    a---------\  \
                |  |-  __
    b---------/__/  -|  \
                    |   )-
    c----------------|__/  -  __
                            -|  \
                            |   )-
    d------------------------|__/  -  __
                                    -|  \
                                    |   )-----
    e--------------------------------|__/
    """

    @always_comb
    def comb():
        q.next = (((a or b) and c) and d) and e

    return instances()


@block
def exe4(led, sw):
    @always_comb
    def comb():
        led[0].next = sw[0] and (not sw[1])

    return instances()


@block
def exe5(leds, sw):
    """
    led0 é uma copia da chave sw0
    led1 é sw0 & sw1
    led2 é o led1 invertido
    led3 é xor entre sw0 e sw1
    todos os outros leds acesos
    """

    @always_comb
    def comb():
        led0 = sw[0]
        leds[0].next = led0
        leds[1].next = sw[0] and sw[1]
        leds[2].next = not led0
        leds[3].next = ((not sw[0]) and sw[1]) or (sw[0] and (not sw[1]))
        for i in range(4, 10):
            leds[i].next = 1

    return instances()


@block
def sw2hex(hex0, sw):
    @always_comb
    def comb():
        pass

    return instances()


@block
def bin2hex(hex0, sw):
    @always_comb
    def comb():
        if sw[4:0] == 0:
            hex0.next = "1000000"
        elif sw[4:0] == 1:
            hex0.next = "1111001"
        elif sw[4:0] == 2:
            hex0.next = "0100100"
        elif sw[4:0] == 3:
            hex0.next = "0110000"
        elif sw[4:0] == 4:
            hex0.next = "0011001"
        elif sw[4:0] == 5:
            hex0.next = "0010010"
        elif sw[4:0] == 6:
            hex0.next = "0000010"
        elif sw[4:0] == 7:
            hex0.next = "1111000"
        elif sw[4:0] == 8:
            hex0.next = "0000000"
        elif sw[4:0] == 9:
            hex0.next = "0010000"
        else:
            hex0.next = "1111111"

    return instances()



#OBS: VETORES NAO FORAM CRIADOS NA MAO! O arquivo vector.py foi utilizado para tal tarefa.
DIG0 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
DIG1 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9)
@block
def bin2bcd(b, bcd1, bcd0):
    """
    componente que converte um vetor de b[8:] (bin)
    para dois digitos em BCD

    Exemplo:
    bin  = `01010010`
    BCD1 = 8
    BCD0 = 2
    """
    

    @always_comb
    def comb():

        bcd0.next = DIG0[int(b)]
        bcd1.next = DIG1[int(b)]

        #bcd0.next = int(str(int(bin(b), 2))[1])
        #bcd1.next = int(str(int(bin(b), 2))[0])

    return comb