try:
    num = int(input(""))
    num2 = int(input(""))
    sum = 0
    counter = num2 - num + 1
    for i in range(num, num2 + 1):
        sum += i
        avg = sum / counter
    else:
        print(f"{sum}\n{avg}")
except Exception as e:
    print(f"Error {e}")