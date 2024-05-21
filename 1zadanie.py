#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# задание: Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально задействовав
# задание: имеющиеся в Python средства перегрузки операторов.

# Ошибки, которые были ранее: нужно выводить ошибку(e), убрать функцию make_pair(проверяет корректность введённых данных, ч
# через исключения), данные исключения прописать в main

class Pair:
    def __init__(self, first, second):
        self.set_first(first)
        self.set_second(second)

    def set_first(self, value):
        if isinstance(value, int) and value > 0:
            self.first = value
        else:
            raise ValueError("НЕ правильное значение.")

    def set_second(self, value):
        if isinstance(value, float) and value > 0:
            self.second = value
        else:
            raise ValueError("НЕ правильное значение.")

    def read(self):
        first = int(input("Введите целое положительное число для 'first': "))
        second = float(input("Введите дробное положительное число для 'second': "))
        self.set_first(first)
        self.set_second(second)

    def display(self):
        print(f"Калорийность 100 г продукта: {self.first} ккал,\nМасса продукта: {self.second} кг.")

    def power(self):
        return self.first * self.second * 10


if __name__ == "__main__":
    try:
        first = int(input("Введите калорийность 100 г продукта: "))
        second = float(input("Введите массу продукта в килограммах: "))
        my_pair = Pair(first, second)
        my_pair.display()
        print(f"Общая калорийность продукта: {my_pair.power()} ккал.")
    except ValueError as ve:
        print(f"Введены некорректные данные. {ve}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
