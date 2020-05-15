def collconject(number):
    number1=number
    if number1%2==0:
        number1=number1//2
        print(number1)
    elif number1%2==1:
        number1=number1*3+1
        print(number1)
    return number1
        
def main():
    print("The collatz Conjecture Sequence")
    while True:
        try:
            number=int(input("enter a number: "))
            break
        except ValueError:
            print("input is not interger")
    #print(f"{num} is an interger")
    while number !=1:
        number=collconject(number)
    print("The End")

if __name__=="__main__":
    main()


#if isinstance(num,int):
#    print("this is an int")
#else:
#    print("this is Not an int")