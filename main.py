try:
    num = int(input(""))
    fact=1
    for i in range(2,num+1):
        fact=fact*i
        print("The factorial of ",num," is: ",fact)
except Exception as e:
    print(f"Error: {e}")