import validation
import conversion
import reversion
import calculation


print(" --Welcome to the Application.-- ")
continueloop=True
while continueloop==True:
    try:
        number1=validation.valid_check()
        print("The first decimal number to be converted is:",number1)
        binary_numb1=conversion.conversion(number1)
        binaryNumber1=reversion.reverse(binary_numb1)
        print("The conversion into binary number is :",binaryNumber1[1])
        print("\n")
    except:
        number1=validation.valid_check()
        print("The first decimal number to be converted is:",number1)
        binary_numb1=conversion.conversion(number1)
        binaryNumber1=reversion.reverse(binary_numb1)
        print("The conversion into binary number is :",binaryNumber1[1])
        print("\n")

    try:
        number2=validation.valid_check()
        print("The second decimal number to be converted is:",number2)
        binary_numb2=conversion.conversion(number2)
        binaryNumber2=reversion.reverse(binary_numb2)
        print("The conversion into binary number is :",binaryNumber2[1])
        print("\n")
    except:
        number2=validation.valid_check()
        print("The second decimal number to be converted is:",number2)
        binary_numb2=conversion.conversion(number2)
        binaryNumber2=reversion.reverse(binary_numb2)
        print("The conversion into binary number is :",binaryNumber2[1])
        print("\n")

    result1=calculation.sum_calculation(binaryNumber1[0],binaryNumber2[0])
    result=reversion.reverse(result1)
    print("The obtained sum of two binary numbers is:",result[1])
    print("\n")

    continuous=input("Do you wish to continue?(yes or no)")
    while continuous!="no" or continuous!="yes" :
        if continuous=="no":
            print("\n")
            continueloop=False 
            break
        elif continuous=="yes":
            print("\n")
            break
        else:
            continuous=input("\nPlease enter yes or on. Do you wish to continue?")
        
print("Thank You. For Your Valuable Time !!! Do visit again. ")
 

