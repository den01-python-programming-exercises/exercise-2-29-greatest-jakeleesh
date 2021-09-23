def main():
    #write your code below this line
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    answer = greatest(num1, num2, num3)
    print("Greatest: " + str(answer))

def greatest(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        return num1
    elif (num2 > num1 and num2 > num3):
        return num2
    elif (num3 > num1 and num3 > num2):
        return num3

if __name__ == '__main__':
    main()
