try:
    len = int(input("Ведіть довжину строки: "))
    for i in range(0, len):
        print("*", end = '')
except Exception:
    print("Error")