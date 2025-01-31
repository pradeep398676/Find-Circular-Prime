digit = 3
count = 0

number_in_str = str(digit)
number_of_digit = []
for i in range(0,len(number_in_str)):
    s = int(number_in_str[i:] + number_in_str[:i])
    number_of_digit.append(s)

# print(number_of_digit)

for j in number_of_digit:

    for i in range(2, j//2+1):

        if j % i == 0:
            count = count+1

if count > 0:
    print(f'{digit} Is Not Prime')
else:
    print(f'{digit} Is Prime')




