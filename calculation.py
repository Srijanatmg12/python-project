def carry_over(high_bit,low_bit,carry):
    d=high_bit ^ low_bit
    e=high_bit & low_bit
    f=carry & d
    g=e|f
    return int(g)

def sum_calculation(high_bit,low_bit):
    result_list=[]
    carry=0
    high_bit.reverse()
    low_bit.reverse()
    for i in range(len(high_bit)):
        total_sum = (high_bit[i]^low_bit[i])
        result_list.append((carry^total_sum))
        carry=carry_over(high_bit[i],low_bit[i],carry)
        i=i+1

    return result_list
