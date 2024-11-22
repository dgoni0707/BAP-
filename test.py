######## TASK 60    
# arr = [10, 20, 30]
# tar = 5
# for i in range (len(arr)):
#         if arr[i] // tar :
#             print ("Yes")
#         else :
#             print ("No")



######## TASK 59
# nums = [3, 1, 4, 1, 5]
# m = min(nums)
# nums.pop(m)
# print (nums)



######## TASK 58
# num1=[]
# nums = [1, 2, 2, 3, 3, 3]
# for i in range(len(nums)):
#     if i % 3 == 0:
#         num1.append(nums[i])
# print(set(num1))



######## TASK 57
# numbers = [121, 343, 123]
# output = []
# for num in numbers:
#     if str(num) == str(num)[::-1]:
#         output.append(True)
#     else:
#         output.append(False)
# print(output)  # [True, True, False]



######## TASK 56
# number = 1234
# digits = []

# for digit in str(number):
#     digits.append(int(digit))

# print(digits)  



######## TASK 55
# digits = [1, 2, 3, 4]
# number = int(''.join(map(str, digits)))
# print(number)



######## TASK 54
# n1 = [1, 2, 3]
# n2 = [2, 3, 4]
# n3 = n1 + n2
# print (set(n3))



######## TASK 53
# arr1 = [1, 2, 3]
# arr2 = [2, 3, 4]

# i = list(set(arr1) & set(arr2))

# print(i)  



######## TASK 52
# n1 = [1,2,3]
# n2 = [1,2,3]

# if n1 == n2:
#     print ("Yes")
# else:
#     print ("No")



######## TASK 51
# arr = [4, 2, 7, 1]
# a1 = list(set(arr))
# a1.sort()
# min2 = a1[1]
# print (min2)



######## TASK 50
# arr = [1, 2, 3, 4]
# larg = list(set(arr))
# larg.sort()
# lar2 = larg[-2]
# print (lar2)



######## TASK 49
# nums = [1, 2, 3]
# answer = []
# for i in range(len(nums)):
#     num = nums[i] * 3
#     answer.append(num)
# print(answer)



######## TASK 48
# nums = [1, 2, 3, 4]
# answer = 0
# nums_len = len(nums)
# for i in range (len(nums)):
#     answer += nums[i]
# print (answer / nums_len)



######## TASK 47
# arr = [1, 2, 3, 4]

# if len(arr) == len(set(arr)):
#     print("Yes")
# else:
#     print("No")



######## TASK 46
arr = [1, 2, 3, 4, 5, 6]
size = 2

output = []
for i in range(0, len(arr), size):
    output.append(arr[i:i + size])

print(output)  

######## TASK 45 
# arr = [5, 10, 15, 20]
# differences = []
# for i in range(len(arr) - 1):
#     differences.append(arr[i + 1] - arr[i]) 
# print(differences) 




######## TASK 44
# nums = [1, 2, 5, 6]
# tar = 4 
# for i in range(len(nums)):
#     if nums[i] > tar :
#         nums[i] = tar 
# print (nums)




######## TASK 43
# nums = [1, 2, 3, 4]
# tar = 3
# for num in nums[:]:
#     if num < tar:
#         nums.remove(num)  
# print(nums)


######## TASK 42
# arr = [1, 2, 3, 4]
# arr = arr[1:] + arr[:1] 
# print(arr)  



######## TASK 41

######## TASK 40

######## TASK 39

######## TASK 38

######## TASK 37
# ar1 = [1, 2, 3]
# ar2 = [4, 5, 6]
# ar3 = []

# for i in range(len(ar1)):
#     ar = ar1[i] + ar2[i]  
#     ar3.append(ar)      
# print(ar3) 



######## TASK 36

######## TASK 35
# arr = [1, 2, 3, 4]
# target = 5
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print("Yes")
#             break
#     else:
#         continue
#     break
# else:
#     print("No")



######## TASK 34
# arr = [1, 2, 3, 4]
# a = 2
# rr = []
# for i in range (len(arr)):
#     r = arr[i] **2
#     rr.append(r)
# print (rr)



######## TASK 33
# arr = [1, 2, 3, 4, 2]
# tar = 2 
# for i , arr in enumerate(arr):
#     if arr == tar:
#         break
# print (i)



######## TASK 32


######## TASK 31
# arr = [10, 20, 33, 46]
# tar = 5
# answer = []
# for i  in range(len(arr)):
#     if arr[i] % tar == 0 :
#         answer.append(arr[i])
# print (answer)



######## TASK 30
# nums = [[1, 2], [3, 4], [5, 6]]
# answer = 0
# for i in range(len(nums)):
#     answer = nums[i]+nums[i+1]
#     answer = answer +nums[i-1]
#     break 
# print (answer)

######## TASK 29
######## TASK 28
######## TASK 27
######## TASK 26
# nums = [[1, 2], [3, 4], [5, 6]]
# answer = 0
# for row in nums: 
#     for num in row:  
#         answer += num 
# print(answer)



######## TASK 25
######## TASK 24
######## TASK 23
######## TASK 22
######## TASK 21
######## TASK 20
######## TASK 19
######## TASK 18
######## TASK 17
######## TASK 16
######## TASK 15
######## TASK 14
######## TASK 13
######## TASK 12
######## TASK 11
######## TASK 10
######## TASK 9
######## TASK 8
######## TASK 7
######## TASK 6
######## TASK 5


######## TASK 4
######## TASK 3
# nums = [1, 2, 2, 3, 3, 3]

# for i in range (len(nums)):
#     for j in range(i + 1):
#         if nums[i] == nums[j]:



######## TASK 2
# arr = [-1, 2, -3, 4]
# for i in range (len(arr)):
#     if arr[i] < 0:
#         arr[i] = 0
#     else:
#         continue
# print (arr)



######## TASK 1
# nums = [2, 3, 4]
# answer = 0
# for i in range(len(nums)):
#     answer = nums[i]*nums[i+1]
#     answer = answer *nums[i-1]
#     break 
# print (answer)

