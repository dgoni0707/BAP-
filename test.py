######## TASK 60    
'''
arr = [10, 20, 30]
tar = 5
for i in range (len(arr)):
        if arr[i] // tar :
            print ("Yes")
        else :
            print ("No")

'''

######## TASK 59
'''
nums = [3, 1, 4, 1, 5]
m = min(nums)
nums.pop(m)
print (nums)
'''


######## TASK 58
'''
num1=[]
nums = [1, 2, 2, 3, 3, 3]
for i in range(len(nums)):
    if i % 3 == 0:
        num1.append(nums[i])
print(set(num1))
'''


######## TASK 57
'''
numbers = [121, 343, 123]
output = []
for num in numbers:
    if str(num) == str(num)[::-1]:
        output.append(True)
    else:
        output.append(False)
print(output)  # [True, True, False]

'''

######## TASK 56
'''
number = 1234
digits = []

for digit in str(number):
    digits.append(int(digit))

print(digits)  
'''


######## TASK 55
'''
digits = [1, 2, 3, 4]
number = int(''.join(map(str, digits)))
print(number)
'''


######## TASK 54
'''
n1 = [1, 2, 3]
n2 = [2, 3, 4]
n3 = n1 + n2
print (set(n3))
'''


######## TASK 53
'''
arr1 = [1, 2, 3]
arr2 = [2, 3, 4]

i = list(set(arr1) & set(arr2))

print(i)  
'''


######## TASK 52
'''
n1 = [1,2,3]
n2 = [1,2,3]

if n1 == n2:
    print ("Yes")
else:
    print ("No")
'''


######## TASK 51
'''
arr = [4, 2, 7, 1]
a1 = list(set(arr))
a1.sort()
min2 = a1[1]
print (min2)
'''


######## TASK 50
'''
arr = [1, 2, 3, 4]
larg = list(set(arr))
larg.sort()
lar2 = larg[-2]
print (lar2)
'''

######## TASK 49
'''
nums = [1, 2, 3]
answer = []
for i in range(len(nums)):
    num = nums[i] * 3
    answer.append(num)
print(answer)
'''


######## TASK 48
'''
nums = [1, 2, 3, 4]
answer = 0
nums_len = len(nums)
for i in range (len(nums)):
    answer += nums[i]
print (answer / nums_len)
'''


######## TASK 47
'''
arr = [1, 2, 3, 4]

if len(arr) == len(set(arr)):
    print("Yes")
else:
    print("No")

'''

######## TASK 46
'''
arr = [1, 2, 3, 4, 5, 6]
size = 2

output = []
for i in range(0, len(arr), size):
    output.append(arr[i:i + size])

print(output)  
'''


######## TASK 45 
'''
arr = [5, 10, 15, 20]
differences = []
for i in range(len(arr) - 1):
    differences.append(arr[i + 1] - arr[i]) 
print(differences) 
'''



######## TASK 44
'''
nums = [1, 2, 5, 6]
tar = 4 
for i in range(len(nums)):
    if nums[i] > tar :
        nums[i] = tar 
print (nums)
'''



######## TASK 43
'''
nums = [1, 2, 3, 4]
tar = 3
for num in nums[:]:
    if num < tar:
        nums.remove(num)  
print(nums)
'''

######## TASK 42
"""
arr = [1, 2, 3, 4]
arr = arr[1:] + arr[:1] 
print(arr)  
"""


######## TASK 41
'''
n = [1, 2, 3, 4]
r = n[::-1]
print(r)  
'''


######## TASK 40
'''
arr = [1, 2]  
result = [[]]
for num in arr:
    new = []
    for curr in result:
        new.append(curr + [num])
    result += new
print(result)  
'''


######## TASK 39
'''
import itertools
s = "abc" 
a = []
for p in itertools.permutations(s):
    a.append(''.join(p))
print(a)  
'''


######## TASK 38
'''
lst = ["apple", "banana", "cherry"]
if lst == sorted(lst):
    print("yes")
else:
    print("no")
'''


######## TASK 37
"""
ar1 = [1, 2, 3]
ar2 = [4, 5, 6]
ar3 = []

for i in range(len(ar1)):
    ar = ar1[i] + ar2[i]  
    ar3.append(ar)      
print(ar3) 


"""
######## TASK 36
'''
arr = [1, 2, 2, 3, 3, 3]
n = {}
for num in arr:
    if num in n:
        n[num] += 1
    else:
        n[num] = 1
most = max(n, key=n.get)
print(most) 
'''


######## TASK 35
"""
arr = [1, 2, 3, 4]
target = 5
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Yes")
            break
    else:
        continue
    break
else:
    print("No")

"""

######## TASK 34
"""
arr = [1, 2, 3, 4]
a = 2
rr = []
for i in range (len(arr)):
    r = arr[i] **2
    rr.append(r)
print (rr)
"""


######## TASK 33
"""
arr = [1, 2, 3, 4, 2]
tar = 2 
for i , arr in enumerate(arr):
    if arr == tar:
        break
print (i)
"""


######## TASK 32
'''
num = 15
start = 10
end = 20

if start <= num <= end:
    print("Yes")
else:
    print("No")
'''



######## TASK 31
"""
arr = [10, 20, 33, 46]
tar = 5
answer = []
for i  in range(len(arr)):
    if arr[i] % tar == 0 :
        answer.append(arr[i])
print (answer)
"""


######## TASK 30
"""
nums = [[1, 2], [3, 4], [5, 6]]
answer = 0
for i in range(len(nums)):
    answer = nums[i]+nums[i+1]
    answer = answer +nums[i-1]
    break 
print (answer)
"""


######## TASK 29
'''
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [list(row) for row in zip(*matrix)]
print(transposed)
'''


######## TASK 28
'''
matrix = [[1, 2], [3, 4]]
is_square = True
for row in matrix:
    if is_square:
        print("Yes")
        break
    else:
        print("No")
'''


######## TASK 27
'''
nums =  [[1, 2], [3, 4], [5, 6]]
answer = []
for i in range (len(nums)):
    answer.append(max(nums [i]))
print (answer)
'''


######## TASK 26
"""
nums = [[1, 2], [3, 4], [5, 6]]
answer = 0
for row in nums: 
    for num in row:  
        answer += num 
print(answer)
"""



######## TASK 25
'''
n = 1234
r = str(n)[::-1]
print(int(r))  
'''


######## TASK 24
'''
n = 45987
n = str(abs(n)) 
m = max(n)
print(int(m))
'''


######## TASK 23
'''
n = 6  
if n <= 1:
    print("No")
else:

    div = 0
    for i in range(1, n):
        if n % i == 0:
            div += i
    if div == n:
        print("Yes")
    else:
        print("No")
'''


######## TASK 22
'''
answer = 0
for i in range(1, 11):
    if i % 2 != 0:
        answer += i
print(answer)
'''


######## TASK 21
'''
answer = 0
for i in range(1, 11):
    if i % 2 == 0:
        answer += i
print(answer)
'''

"""{"""
######## TASK 20

'ИХ НЕТ В СПИСКЕ УЧИТЕЛЯ'

######## TASK 19
"""}"""

######## TASK 18
'''
s = ("hello", "world")
print(s[0] + s[1])
'''


######## TASK 17
'''НЕ ПОНЯЛ КАК НАДО'''


######## TASK 16
'''
s = "hello world"
words = s.split() 
word1 = []
for word in words:
    word1.append(word[::-1])
output = ' '.join(word1)
print(output) 
'''
######## TASK 15
'''
s = "programming"
r = ""
for char in s:
    if char not in r:
        r += char
print(r)
'''


######## TASK 14
'''
s = "hello world"
old = "o"
new = "x"
s1 = ""
for char in s:
    if char == old:
        s1 += new
    else:
        s1 += char
print(s1) 
'''


######## TASK 13
'''
s = "The quick brown fox"
words = s.split()
word = len(words)
print(word) 
'''


######## TASK 12
'''
text = "hello world"
vowels = {"a", "e", "y", "u", "i", "o"}
result = ""
for char in text:
    if char.lower() not in vowels:
        result += char
print(result)
'''


######## TASK 11
'''
s = "12345"

if s.isdigit():
    print("Yes")
else:
    print("No")
'''


######## TASK 10
"""
nums = [1, 2, 3, 4, 5, 6]
div = 2
odd = []
single = []
for num in nums:
    if num % div == 0 :
        odd.append(num)
    else:
        single.append(num)
print (single , odd)
"""

######## TASK 9
"""
arr1 = [1, 2, 3]
arr2 = [2, 3, 4]

i = list(set(arr1) & set(arr2))

print(i)  
"""



######## TASK 8
'''
nums = [3, 1, 4, 1, 5]
for i in range(len(nums)):
    for j in range(i + 1):            
        if nums [i] < nums[j]:
            nums[j], nums [i] = nums[i], nums[j]
print(nums)
'''


######## TASK 7
'''
nums = [1, 2, 3, 4, 5]
answer = 0
for i in range (len(nums)):
    if nums[i] % 2 == 0:
        answer += nums[i]
print(answer)
'''

######## TASK 6
"""
nums = [1, 2, 3, 4, 5]
answer = 0
for i in range(len(nums)):
    if i % 2 == 0:
        answer += nums[i]
print(answer)
"""


######## TASK 5
'''
arr = [1, 2, 2, 3, 3, 4]
a= set(arr)
print(a)
'''


######## TASK 4
'''
arr = [1, 2, 3, 1]
if len(arr) != len(set(arr)):
   print("Yes")
else:
    print("No")
'''


######## TASK 3
"""
nums = [1, 2, 2, 3, 3, 3]

for i in range (len(nums)):
    for j in range(i + 1):
        if nums[i] == nums[j]:
"""


######## TASK 2
"""
arr = [-1, 2, -3, 4]
for i in range (len(arr)):
    if arr[i] < 0:
        arr[i] = 0
    else:
        continue
print (arr)
"""


######## TASK 1
"""
nums = [2, 3, 4]
answer = 0
for i in range(len(nums)):
    answer = nums[i]*nums[i+1]
    answer = answer *nums[i-1]
    break 
print (answer)
"""
