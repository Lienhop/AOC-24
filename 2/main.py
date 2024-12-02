def main():
    #Result is almost correct, just -1. No idea where the error is...
    with open('data.csv') as f:
        lines = f.readlines()
        count = 0
        for i in lines:
            count += checkValidityInitial(i)
    print(count)

def checkValidityInitial(l):
    asc = True
    
    for j in range(len(l.split(' '))-1):
        a = int(l.split(' ')[j])
        b = int(l.split(' ')[j+1])
        
        if j == 0:
            if a > b:
                asc = False
        if(abs(a-b)>3 or abs(a-b)<1):
            lNew = ' '.join(l.split(' ')[:j] + l.split(' ')[j+1:])
            if(checkValidity(lNew) == 1):
                return 1
            else:
                lnew = ' '.join(l.split(' ')[:j+1] + l.split(' ')[j+2:])
                if checkValidity(lnew) == 1:
                    return 1
            return 0
        
        if asc:
            if a > b:
                lNew = ' '.join(l.split(' ')[:j] + l.split(' ')[j+1:])
                if(checkValidity(lNew) == 1):
                    return 1
                else:
                    lnew = ' '.join(l.split(' ')[:j+1] + l.split(' ')[j+2:])
                    if checkValidity(lnew) == 1:
                        return 1
                return 0
        else:
            if a < b:
                lNew = ' '.join(l.split(' ')[:j] + l.split(' ')[j+1:])
                if(checkValidity(lNew) == 1):
                    return 1
                else:
                    lnew = ' '.join(l.split(' ')[:j+1] + l.split(' ')[j+2:])
                    if checkValidity(lnew) == 1:
                        return 1
                return 0
    return 1

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