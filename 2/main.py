def main():
    with open('data.csv') as f:
        lines = f.readlines()
        count = 0
        for i in lines:
            count += checkValidity(i)
    print(count)

def checkValidity(l):
    asc = True
    
    for j in range(len(l.split(' '))-1):
        a = int(l.split(' ')[j])
        b = int(l.split(' ')[j+1])
        
        if j == 0:
            if a > b:
                asc = False
    
        if(abs(a-b)>3 or abs(a-b)<1):
            return 0
        
        if asc:
            if a > b:
                return 0
        else:
            if a < b:
                return 0
    return 1

if __name__ == '__main__':
    main()