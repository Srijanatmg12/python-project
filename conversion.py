def conversion(number):
    number_list=[]
    for n in range(0,8,1):
        Reminder=number%2
        number_list.append(Reminder)
        number=number // 2
        n=n+1
    return number_list
