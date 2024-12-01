
def main():

    a, b = [], []

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
        sum += abs(i -j)
    print(sum)

if __name__ == '__main__':
    main()