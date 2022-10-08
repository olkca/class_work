try:
    len = int(input("Ведіть довжину строки: "))
    sim = input("Ведіть символ: ")
    for i in range(0, len):
        print(sim, end = '')
except Exception:
    print("Error")