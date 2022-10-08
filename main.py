try:
    num1 = int(input("Число 1: "))
    num2 = int(input("Число 2: "))
    sum = num1 + num2
    sum2 = sum / 2
    print(f"Сума чисел:{sum} Середне арифматичне:{sum2}")
except Exception as e:
    print(f"Error...{e}")