def reverse(number_list):
    actualBinary=[]
    binaryNumber=" "
    for i in range(len(number_list)-1,-1,-1):
        actualBinary.append(number_list[i])
        binaryNumber = binaryNumber + str(number_list[i])
    return (actualBinary,binaryNumber)
