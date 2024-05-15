def biggest_odd(string):
    odd_num = [int(x) for x in string if int(x) / 2 != 0]
    return max(odd_num)


print(biggest_odd('1234'))