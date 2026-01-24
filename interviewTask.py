# def rotate_left(arr,d):
#     n = len(arr)
#     d=d%n
#     arr[:] = arr[d:]+arr[:d] #[3,4,5]+[1+2]
#     return arr

# print(rotate_left([1, 2, 3, 4, 5],2))
# print(rotate_left([2, 4, 6, 8, 10, 12, 14, 16, 18, 20],3))
# print(rotate_left([7, 3, 9, 1],9))


# Reverse an Array
# # def reverse_array(arr):
# #     for i in range(len(arr)):
# #         for j in range(len(arr-1)):
# #             arr[i] = arr[len(arr)]


# # arr = [1,2,3,4,5]
# # rev=[]
# # for i in range(len(arr)-1,-1,-1):
# #     rev.append(arr[i])
# # print(rev)
# # arr.reverse()
# # print(arr)

# # rev = arr[::-1]
# # print(rev)




# # n=5

# # 5
# # 4
# # 3
# # 2
# # 1
# # for i in range(10,-1,-2):
# #     print(i)

# # def reverse_array(arr):
# #     left =0
# #     right = len(arr)-1
# #     while left <right:
# #         arr[left],arr[right] = arr[right],arr[left]
# #         left+=1 
# #         right-=1
# #     return arr

# # print(reverse_array([1, 4, 3, 2, 6, 5]))
# # print(reverse_array([4, 5, 2]))
# # print(reverse_array([1]))



# # Check if array is sorted
# def sorted_array(arr):
#     n=len(arr)
#     for i in range(n-1):
#         if arr[i] > arr[i+1]:
#             return False
#         return True
    
# print(sorted_array([10, 20, 30, 40, 50]))
# print(sorted_array([90, 80, 100, 70, 40, 30]))

# # Sum of Array

# def sum(arr):
#     sum= 0
#     for i in range (len(arr)):
#         sum+=arr[i]
#     return sum

# print(sum([1, 2, 3, 4]))
# print(sum([1, 3, 3]))


# # palindrome
# def palindrome(arr):
#     for i in arr:
#         new = i #111 
#         rev = 0
#         while i>0:
#             rev = rev*10+i%10 
#             i//=10
#         if rev!=new:
#             return False
#     return True

# print(palindrome([111, 222, 333, 444, 555]))



# Count of smaller elements
# def countofElements(arr,x):
#     count = 0
#     for i in arr:
#         if i<=x:
#             count+=1
#     return count

# print(countofElements([10, 1, 2, 8, 4, 5],9))
# print(countofElements([1, 2, 2, 5, 7, 2, 9],2))


# Find Index
def firstandLast(arr,key):
    start = -1
    end =-1

    for i in range (len(arr)):
        if arr[i]==key:
            if start==-1:
                start=i
            end=i
    return [start,end]
    
print(firstandLast([1, 2, 3, 4, 5, 5],5))