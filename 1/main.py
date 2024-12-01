
def main():

    a, b = [], []
    dict  = {}

    with open('data.csv') as f:
        lines = f.readlines()
        for i in lines:
            x, y = i.split('   ')
            a.append(int(x))
            b.append(int(y))
    a.sort()
    b.sort()
    sum = 0
    for i, j in zip(a, b):
        if j not in dict:
            dict[j] = 0
        dict[j] += 1
        sum += abs(i -j)
    print(sum)
    sum2 = 0
    for i in a:
        if i not in dict:
            continue
        sum2 +=  i * dict[i]
    print(sum2)
    
if __name__ == '__main__':
    main()