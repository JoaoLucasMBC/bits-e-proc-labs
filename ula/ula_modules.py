#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


@block
def halfAdder(a, b, soma, carry):
    @always_comb
    def comb():
        soma.next = a ^ b
        carry.next = a & b

    return instances()


@block
def fullAdder(a, b, c, soma, carry):
    s = [Signal(bool(0)) for i in range(3)]
    haList = [None for i in range(2)]

    haList[0] = halfAdder(a, b, s[0], s[1])
    haList[1] = halfAdder(c, s[0], soma, s[2])

    @always_comb
    def comb():
        #axorb = (a or b) and ((not a) or (not b))
        #soma.next = (axorb or c) and ((not axorb) or (not c))
        #carry.next = (axorb and c) or (a and b)

        carry.next = s[1] or s[2]

    return instances()


@block
def adder2bits(x, y, soma, carry):
    carry1 = Signal(bool(0))
    half = halfAdder(x[0], y[0], soma[0], carry1)
    full = fullAdder(x[1], y[1], carry1, soma[1], carry)

    return instances()


@block
def adder(x, y, soma, carry):
    n = len(x)

    faList = [None for i in range(n)]
    carry_aux = [Signal(bool(0)) for i in range(n)]

    faList[0] = fullAdder(x[0], y[0], 0, soma[0], carry_aux[0])

    for i in range(1, n):
        faList[i] = fullAdder(x[i], y[i], carry_aux[i - 1], soma[i], carry_aux[i])

    @always_comb
    def comb():
        carry.next = carry_aux[n - 1]

    return instances()


@block
def adderIntbv(x, y, soma, carry):
    @always_comb
    def comb():
        sum_ = x + y
        soma.next = sum_
        if sum_ > x.max - 1:
            carry.next = 1
        else:
            carry.next = 0
    
    return comb