#!/usr/bin/python3
for number in range(100):
    if ((number // 10) == 8) and ((number % 10) == 9):
        print("{}".format(number))
    elif (number // 10) == (number % 10):
        continue
    elif (number // 10) > (number % 10):
        continue
    else:
        print("{:0>2}, ".format(number), end='')
