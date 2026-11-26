# Reverse a string without using slicing.
# s = "hello"
# result = ""
# for ch in s:
#     result = ch + result 
# print(result)    

# Count the number of vowels in a string.
# s = "hello world"
# count = 0
# for ch in s:
#     if ch in "aeiouAEIOU":
#         count +=1
# print(count)  
# 
# Check whether a string is a palindrome.
# s = "madam"
# result = ""
# for ch in s:
#     result = result + ch
# print(result)    
# 
# 
# Find the largest number in a list without using max().    
# nums = [12,35,56,98,23]
# largest = nums[0]
# for n in nums:
#     if n > largest:
#         largest = n
# print (largest)

# Remove duplicate elements from a list.
# nums = [1,3,3,5,6,8]
# unique =[]
# for n in nums:
#     if n not in unique:
#         unique.append(n)
# print(unique)        


# print the second largest number in the list

# num = [10,20,30,50]
# largest = second = float("-inf")
# for i in num:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i> second and i != largest:
#         second =i
# print(second)  
# 
#  Count the frequency of each character in a string using a dictionary
# word = "ppython"
# frequency = {}
# for i in word:      
#         if i in frequency:
#                 frequency[i] =+1
#         else:
#                 frequency[i] = 1
# print(frequency)    
# number = int(input("enter the number"))
# for i in range(1,11):
#     print(f"{number}*{i} = {number * i}")   


# for i in range(1,51):
#     if i%2==0:
#         print("is even number", i)    

  
total = 0     
for i in range(1,51):
    total += i
print(total)