def is_armstrong(num):
    total=0
    n=num
    power=len(str(num))
    while n>0:
        digit=n%10
        total+=digit**power
        n//=10
    return total==num

def is_palindrome(num):
    original=num
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num//=10
    return rev==original

number=int(input("Enter a number:"))

if is_armstrong(number):
    print(number,"is an Armstrong number")
else:
    print(number,"is not an Armstrong number")

if is_palindrome(number):
    print(number,"is an Palindrome number")
else:
    print(number,"is not an Palindrome number")