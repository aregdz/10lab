#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
        second = float(
            input("Введите дробное положительное число для 'second': ")
        )
        self.set_first(first)
        self.set_second(second)

    def display(self):
        print(
            f"Калорийность 100 г продукта: {self.first} ккал,\nМасса продукта: {self.second} кг."
        )

    def power(self):
        return self.first * self.second * 10


def make_pair(first, second):
    try:
        pair = Pair(first, second)
        return pair
    except ValueError as ve:
        print(ve)
        return None


if __name__ == "__main__":
    try:
        first = int(input("Введите калорийность 100 г продукта: "))
        second = float(input("Введите массу продукта в килограммах: "))
        my_pair = make_pair(first, second)
        if my_pair:
            my_pair.display()
            print(f"Общая калорийность продукта: {my_pair.power()} ккал.")
    except Exception as e:
        print("Введены некорректные данные.")
