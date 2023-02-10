def f1(num):
    c = 0
    s = 0
    for i in range(num):
        if i % 2 == 0:
            c += 1
            s += i
        print(i, end=' ')
    print('\nTotal Even Number: ',c)
    print('Sum: ',s)

num = int(input('Enter a number'))
f1(num)
