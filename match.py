a = 10
b = 20
op = "*"
match op:
    case"+":
        print("result:", a+b)
    case"-":
        print("result:",a-b)
    case"*":
        print("result:",a*b)
    case"/":
        if b==0:
            print("cannot divide by zero")  
        else:
            print("result:",a%b)
    case _:
        print("invalid operator")
                    

#loop question               
for i in range(1,11):
    print(i)

#star sum    
n=5
for i in range (1, n+1):
    print("*" * i)
    
   