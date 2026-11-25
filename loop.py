# to check if a number is postive 
# num = 0
# if num >= 0:
#     print("number is positive")
# else:
#     print("number is negative")    

# Write a program to check whether a number is even or odd.
# num = 24
# if num%2 == 0:
#     print("number is even ")
# else:    
#     print("number is odd")


# Write a program to check whether two numbers are equal.

# a = 50
# b = 50
# if a!=b:
#     print("a is not equal to b")
# else:
#     print("a is equal to b")    

#  Write a program to check whether a number is divisible by both 3 and 5
# num = 18
# if num % 3 ==0 and num % 5 ==0:
#     print("number is divisible by both 3 and 5")

#Write a program to identify whether a number is positive, negative, or zero.
# num = 0 
# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")  
# 
#     Write a program to find the greatest among three numbers.  

# a = 10
# b = 20
# c = 30 
# if a>=b and a>=c:
#     print("a is greatest")
# elif b>=a and b>=c:
#     print("b is greatest")
# else:
#     print("c is greatest")

# Write a program to identify whether a character is a vowel or consonant.
# ch = "e"
# if ch in "a,e,i,o,u":
#     print("vowels")
# else:
#     print("consonants")    

# year = 2028
# if (year%4 == 0 and year %100 != 0) or (year %400 ==0):
#     print("its a leap yr")
# else:             
#     print("its not a leap year")

a = 20
b = 5
op = "*"
if op == "+":
    print(a+b)
elif op =="-":
    print(a-b)
elif op =="*":
    print(a*b)
elif op =="/":
    if a/b != 0:
        print(a/b)
    else:
        print("cannot divide by zero")    
else:
    print("invalid operator")        

