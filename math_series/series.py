def fibonacci(number):
    num_array = [0,1]
    for i in range(0,number):
        num = num_array[i] + num_array[i+1]
        num_array.append(num)
    return str(num_array[number-1])


def lucas(number):
    num_array = [2,1]
    for i in range(0,number):
        num = num_array[i] + num_array[i+1]
        num_array.append(num)
    return str(num_array[number-1])

def sum_series(number,first_num=0,second_num=1):
    num_array = [first_num,second_num]
    for i in range(0,number):
        num = num_array[i] + num_array[i+1]
        num_array.append(num)
    return str(num_array[number-1])


    