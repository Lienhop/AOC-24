import re

pattern = 'mul\([0-9]{1,3},[0-9]{1,3}\)'

def main():
    sum = 0
    with open('input.txt') as f:
        content = f.read()
        matches = re.findall(pattern, content)
        for match in matches:
            sum += mul(match)
    print(sum)

def mul(input):
    a, b = map(int, input[4:-1].split(','))
    return a*b

if __name__ == '__main__':
    main()