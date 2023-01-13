import time

def format(mylist):
    usrs = mylist
    usrs = usrs.split()
    variable = usrs[2][len(usrs[2])-1]

    a = usrs[0][:usrs[0].index("{}^2".format(variable))]
    if len(a) == 0:
        a = 1
    elif len(a) == 1 and a == '-':
        a = -1

    b = usrs[2][:usrs[2].index("{}".format(variable))]
    if len(b) == 0:
        b = 1
    elif len(b) == 0 and usrs[1] == '-':
        b = -1
    elif usrs[1] == '-':
        b = 0 - int(b)

    c = usrs[4]
    if usrs[3] == '-':
        c = 0 - int(c)

    multiple = int(c) * int(a)
    add = b
    return multiple, add

def make_(number):
    number += 1
    number = 0 - number
    return number


# print("""Two test inputs 
# k^2 - 18k + 80
# 6p^2 + 36p - 240""")
# ax + bx + c

usrs = input('Enter equation: ')

multiple, add = format(usrs)
time.sleep(2)

print('\n\nMultiples to', multiple)
print('Adds to', add)
solutions = {}
for num1 in range(100):
    num1 +=1
    for num2 in range(100):
        num2 += 1
        if num2 * num1 == multiple:
            # print(num1, num2)
            solutions[num1] = num2

        if num2 * make_(num1) == multiple:
            # print(make_(num1), num2)
            solutions[make_(num1)] = num2

        if make_(num2) * num1 == multiple:
            # print(num1, make_(num2))
            solutions[num1] = make_(num2)

        if make_(num2) * make_(num1) == multiple:
            # print(make_(num1), make_(num2))
            solutions[make_(num1)] = make_(num2)

# print(solutions)
f = False
for item in solutions:
    # print(item, solutions[item], item + solutions[item], add)
    if item + solutions[item] == int(add):
        print('Factors:', item, solutions[item])
        f = True
        break
if f == False:
    print('not factorable')
