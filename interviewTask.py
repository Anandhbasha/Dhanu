# # def rotate_left(arr,d):
# #     n = len(arr)
# #     d=d%n
# #     arr[:] = arr[d:]+arr[:d] #[3,4,5]+[1+2]
# #     return arr

# # print(rotate_left([1, 2, 3, 4, 5],2))
# # print(rotate_left([2, 4, 6, 8, 10, 12, 14, 16, 18, 20],3))
# # print(rotate_left([7, 3, 9, 1],9))


# # Reverse an Array
# # # def reverse_array(arr):
# # #     for i in range(len(arr)):
# # #         for j in range(len(arr-1)):
# # #             arr[i] = arr[len(arr)]


# # # arr = [1,2,3,4,5]
# # # rev=[]
# # # for i in range(len(arr)-1,-1,-1):
# # #     rev.append(arr[i])
# # # print(rev)
# # # arr.reverse()
# # # print(arr)

# # # rev = arr[::-1]
# # # print(rev)




# # # n=5

# # # 5
# # # 4
# # # 3
# # # 2
# # # 1
# # # for i in range(10,-1,-2):
# # #     print(i)

# # # def reverse_array(arr):
# # #     left =0
# # #     right = len(arr)-1
# # #     while left <right:
# # #         arr[left],arr[right] = arr[right],arr[left]
# # #         left+=1 
# # #         right-=1
# # #     return arr

# # # print(reverse_array([1, 4, 3, 2, 6, 5]))
# # # print(reverse_array([4, 5, 2]))
# # # print(reverse_array([1]))



# # # Check if array is sorted
# # def sorted_array(arr):
# #     n=len(arr)
# #     for i in range(n-1):
# #         if arr[i] > arr[i+1]:
# #             return False
# #         return True
    
# # print(sorted_array([10, 20, 30, 40, 50]))
# # print(sorted_array([90, 80, 100, 70, 40, 30]))

# # # Sum of Array

# # def sum(arr):
# #     sum= 0
# #     for i in range (len(arr)):
# #         sum+=arr[i]
# #     return sum

# # print(sum([1, 2, 3, 4]))
# # print(sum([1, 3, 3]))


# # # palindrome
# # def palindrome(arr):
# #     for i in arr:
# #         new = i #111 
# #         rev = 0
# #         while i>0:
# #             rev = rev*10+i%10 
# #             i//=10
# #         if rev!=new:
# #             return False
# #     return True

# # print(palindrome([111, 222, 333, 444, 555]))



# # Count of smaller elements
# # def countofElements(arr,x):
# #     count = 0
# #     for i in arr:
# #         if i<=x:
# #             count+=1
# #     return count

# # print(countofElements([10, 1, 2, 8, 4, 5],9))
# # print(countofElements([1, 2, 2, 5, 7, 2, 9],2))


# # # Find Index
# # def firstandLast(arr,key):
# #     start = -1
# #     end =-1

# #     for i in range (len(arr)):
# #         if arr[i]==key:
# #             if start==-1:
# #                 start=i
# #             end=i
# #     return [start,end]
    
# # print(firstandLast([1, 2, 3, 4, 5, 5],5))

# # Find the element before which all the elements are smaller than it, and after which all are greater

# # def findElement(arr):
# #     n = len(arr)
# #     for i in range(n):
# #         leftOk = True
# #         RightOk = True
# #         for j in range(i):
# #             if arr[j]>arr[i]:
# #                 leftOk=False
# #                 break
# #         for j in range(i+1,n):
# #             if arr[j]<arr[i]:
# #                 RightOk=False
# #                 break
# #         if leftOk and RightOk:
# #             return arr[i]
# #     return -1

# # print(findElement([5, 1, 4, 3, 6, 8, 10, 7, 9]))

# # min = lambda a,x:a>x

# # print(min(5,6))

# # Sort elements by frequency

# from collections import Counter

# # def sortbyFreq(arr):
# #     freq = Counter(arr)
# #     arr.sort(key= lambda x:(-freq[x],x))
# #     return arr


# # print(sortbyFreq([5, 5, 4, 6, 4]))

# # freq ={4:2,5:2,6:1}
# # #4->(-4,4)
# # # 5->(-5,5)
# # #6->(-1,6)

# # {4,4,5,5,6}


# # Find the two repeating elements in a given array

# def findReapeating(arr):
#     freq = Counter(arr)
#     res = []
#     for num in arr:
#         if freq[num] ==2:
#             res.append(num)
#             freq[num] = 0
#     return res

# print(findReapeating([4, 2, 4, 5, 2, 3, 1]))



# intersection of two array
# naive approach
# Triple Loops


# def intersection_naive(a,b):
#     res = []
#     for i in range(len(a)): #  i =1
#         duplicate = False
#         for k in range(i):  # k=-1
#             if a[k]==a[i]:
#                 duplicate=True
#                 break
#         if duplicate:
#             continue
#         for j in range(len(b)):
#             if a[i]==b[j]:
#                 res.append(a[i])
#                 break
#     return res
    
# print(intersection_naive([1, 2, 1, 3, 1],[3, 1, 3, 4, 1]))

# # Better Approach
# # NestedLoop HasHset
# def intersection_better(a,b):
#     res =set()
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if a[i]==b[j]:
#                 res.add(a[i])
#     return res

# print(intersection_better([1, 2, 1, 3, 1],[3, 1, 3, 4, 1]))


# # Arr[] = {1, 10, 12, 9, 2, 3}
# # 6
# # 1+2->3 {3,10,12,9,3}
# # 3+3->{6,10,12,9}

# import heapq
# def minOpeartions(arr,k):
#     heapq.heapify(arr)
#     # [1,2,3,4,5,9,12]
#     count=0
#     while arr and arr[0]<k: #6
#         if len(arr)<2:
#             return -1
#         x=heapq.heappop(arr)
#         y=heapq.heappop(arr)
#         heapq.heappush(arr,x+y)
#         # 1+2 =3
#         # [3,3,4,5,9,12]
#         # 3+3
#         count+=1
#     return count

# print(minOpeartions([1,2,3,12,9,5,4],6))



# Subarray
# [nums[i]+nums[i+2] = /frac{nums[i+1]}{2}]

# def constSubArray(nums):
#     count = 0
#     n=len(nums)
#     for i in range(n-2):
#         if  nums[i]+nums[i+2] ==nums[i+1]/2:
#             count+=1
#     return count

# # [1,2,1,4,1]
# # 1,2,1  
# # 2,1,4 
# # 1,4,1 

# print(constSubArray([1,2,1,4,1]))
# print(constSubArray([1,1,1]))



# Wildcard string matching
# def match(wild,pattern):
#     n=len(wild)
#     m=len(pattern)
#     dp = [[False]*(m*1) for _ in range(n+1)]
#     dp[0][0] = True
#     for i in range(1,n+1):
#         if wild[i-1]=="*":
#             dp[i][0] =dp[i-1][0]
#     for i in range(1,n+1):
#         for j in range(1,m+1):
#             if wild[i-1]=="*":
#                 dp[i][j]=dp[i-1][j] or dp[i][j-1]
#             elif wild[i-j]=='?' or wild[i-1]==pattern[j-1]:
#                 dp[i][j] = dp[i-1][j-1]
#             else:
#                 dp[i][j]=False
#     return dp[i][j]

# print(match("ge*ks","geeks"))



# Non Repeating Character
# def NonReapeting(s):
#     freq={}

#     res =[]
#     # count freq
#     for ch in s:
#         freq[ch] = freq.get(ch,0)+1

#     for ch in s:
#         if freq[ch]==1:
#             print("Hello")
#             res.append(ch)
#     if len(res)==0:
#         return "$"
#     return res


# {
#     g:2,e:4,k:2,s:2,f:1,o:1,r:1
# }

# print(NonReapeting("geeksforgeeks"))


# Remove Consecutive Characters
# def consucutive(s):
#     if not s:
#         return ""
#     res = [s[0]]
#     for i in range (1,len(s)):
#         if s[i] != s[i-1]:
#             res.append(s[i])
#     return res

# print(consucutive("aabb"))
# print(consucutive("abcddcba"))


# def maxFreq(s):
#     words = s.split()
#     freq = {}
#     for word in words:
#         freq[word] = freq.get(word,0)+1
#         max_Count = 0
#         resultWord = ""
#     for word in words:
#         if freq[word]>max_Count:
#             max_Count=freq[word]
#             resultWord=word
#     return resultWord+ " " +str(max_Count)
        
# print(maxFreq("the devil in the sky"))


# def reverseWords(s):
#     newtext = s.split(".")
#     words =[]
#     for n in newtext:
#         if n!="":
#             words.append(n)
#     words.reverse()
#     return ".".join(words)

# print(reverseWords("i.like.this.program.very.much"))


# def rearrange(arr):
#     pos = []
#     neg = []

#     # O(n)
#     for x in arr:
#         if x >= 0:
#             pos.append(x)
#         else:
#             neg.append(x)

#     res = []
#     i = j = 0

#     # First: alternate 2 times (+ - + -)
#     for _ in range(2):
#         if i < len(pos) and j < len(neg):
#             res.append(pos[i]); i += 1
#             res.append(neg[j]); j += 1

#     #+ -
#     if i < len(pos):
#         res.append(pos[i]); i += 1
#     if j < len(neg):
#         res.append(neg[j]); j += 1

#     # Remaining: alternate
#     while i < len(pos) and j < len(neg):
#         res.append(pos[i]); i += 1
#         res.append(neg[j]); j += 1

#     # Leftovers
#     while i < len(pos):
#         res.append(pos[i]); i += 1
#     while j < len(neg):
#         res.append(neg[j]); j += 1

#     return res


# print(rearrange([9, 4, -2, -1, 5, 0, -5, -3, 2]))

# def fibb(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fibb(n-1)+fibb(n-2)

# print(fibb(5))

def fact(n):
    res = 1
    for i in range(1,n+1): #5 
        res = res*i
    return res

print(fact(5))

# class Students:
#     studentName = "Arun"
#     studentTotal = 420
#     studentRollNo="11ME784"
#     def marks(self):
#         print(self.studentName,self.studentTotal)

# Stu1 = Students()
# print(Stu1.studentName)
# Stu1.studentName ="Ajay"
# print(Stu1.studentName)
# print(Stu1.studentTotal)
# stu2 = Students()
# stu2.studentTotal="489"
# stu2.marks()



# class Students:
#     def __init__(self,name,age):
#         self.name=name
#         self.age =age
#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)

# stu = Students("Vijay",32)
# stu.display()



class Father:
    property="House"
class son(Father):
    def prints(self):
        print(self.property)
class doughter(Father):
    def prints(self):
        print(self.property)

s=son()
s.prints()
d=doughter()
d.prints()

