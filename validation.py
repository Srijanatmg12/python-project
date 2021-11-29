def number_check():
    while True:
        try:
            n=int(input("Enter the decimal number: "))
            break
        except ValueError:
            print("The number cannot be in String.")
            print("\n")
            continue
        else:
            break
    return n

def valid_check():
    error=True
    while error == True:
        try:
            number=number_check()
            if number > 0 and number < 255:
                if number+number>255:
                    print("result should be in 8 bit")
                    error=True
                else:
                    error = False
                    return number

            else:
                print("Please!!enter the correct number between 0-255: ")
                number=int(number_check())
                error = True
        except:
            print("The entered number is invalid.Please insert valid number.")

