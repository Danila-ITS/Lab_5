#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из вещественных элементов, вычислить:
# 1) сумму отрицательных элементов списка;
# 2) произведение элементов списка, расположенных между максимальным и минимальным
# элементами.
# Упорядочить элементы списка по возрастанию.

import sys

N = 10
if __name__ == '__main__':
    A = list(map(float, input("Введите список ").split()))
    sum = 0
    proiz = 1

    min = max = A[0]
    i_min = i_max = 0
    for i, item in enumerate(A):
        if item < min:
            i_min, min = i, item
        if item >= max:
            i_max, max = i, item

    for i, item in enumerate(A):
        if item < 0:
            sum += item
        if i_min < i < i_max:
            proiz *= item
            print(proiz)
    A = sorted(A)

    print("Отсортированный по возрастанию список ", A)
    print("Сумма и произведение ", sum, proiz)
