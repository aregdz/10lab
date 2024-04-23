class Fraction:
    MAX_SIZE = 100

    def __init__(self, size):
        if size > Fraction.MAX_SIZE:
            raise ValueError("Введите размер меньше:")
        self.integer_part = [0] * size
        self.decimal_part = [0] * size
        self.size = size
        self.count = 0

    def get_size(self):
        return self.size

    def get_count(self):
        return self.count

    def __add__(self, other):
        result = Fraction(self.size)
        carry = 0
        for i in range(self.size - 1, -1, -1):
            total = self.integer_part[i] + other.integer_part[i] + carry
            result.integer_part[i] = total % 10
            carry = total // 10

        for i in range(self.size):
            total = self.decimal_part[i] + other.decimal_part[i] + carry
            result.decimal_part[i] = total % 10
            carry = total // 10

        return result

    def __sub__(self, other):
        result = Fraction(self.size)
        borrow = 0

        for i in range(self.size - 1, -1, -1):
            sub = self.integer_part[i] - other.integer_part[i] - borrow
            if sub < 0:
                borrow = 1
                sub += 10
            else:
                borrow = 0
            result.integer_part[i] = sub

        for i in range(self.size):
            sub = self.decimal_part[i] - other.decimal_part[i] - borrow
            if sub < 0:
                borrow = 1
                sub += 10
            else:
                borrow = 0
            result.decimal_part[i] = sub

        return result


    def __str__(self):
        integer_str = "".join(map(str, reversed(self.integer_part)))
        decimal_str = "".join(map(str, self.decimal_part))
        return f"{integer_str}.{decimal_str}"


fraction1 = Fraction(5)
fraction1.integer_part = [1, 2, 3, 4, 5]
fraction1.decimal_part = [6, 7, 8, 9, 0]
fraction2 = Fraction(5)
fraction2.integer_part = [5, 4, 3, 2, 1]
fraction2.decimal_part = [0, 9, 8, 7, 6]

result_add = fraction1 + fraction2
result_sub = fraction1 - fraction2
print(f"Сумма: {result_add}")
print(f"Результат умножения:: {result_sub}")
