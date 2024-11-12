def check_input(value):
    num = int(value)
    if 1 <= num <= 100:
        return num
    else:
        print(f"Ви ввели неправильне значення: {num}")
        return None


a_input = int(input("Введіть значення a (від 1 до 100): "))
a = check_input(a_input)

b_input = int(input("Введіть значення b (від 1 до 100): "))
b = check_input(b_input)

if a is None or b is None:
    print("введіть правильні значення")
else:
    if a > b:
        X = 2 * a + b
    elif a == b:
        X = -2
    else:
        X = (a - 5) / b

    print(f"Значення X: {X}")