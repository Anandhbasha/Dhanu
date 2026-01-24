# def rotate_left(arr,d):
#     n = len(arr)
#     d=d%n
#     arr[:] = arr[d:]+arr[:d] #[3,4,5]+[1+2]
#     return arr

# print(rotate_left([1, 2, 3, 4, 5],2))
# print(rotate_left([2, 4, 6, 8, 10, 12, 14, 16, 18, 20],3))
# print(rotate_left([7, 3, 9, 1],9))


# Reverse an Array
# def reverse_array(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr-1)):
#             arr[i] = arr[len(arr)]


# arr = [1,2,3,4,5]
# rev=[]
# for i in range(len(arr)-1,-1,-1):
#     rev.append(arr[i])
# print(rev)
# arr.reverse()
# print(arr)

# rev = arr[::-1]
# print(rev)




# n=5

# 5
# 4
# 3
# 2
# 1
# for i in range(10,-1,-2):
#     print(i)

# def reverse_array(arr):
#     left =0
#     right = len(arr)-1
#     while left <right:
#         arr[left],arr[right] = arr[right],arr[left]
#         left+=1 
#         right-=1
#     return arr

# print(reverse_array([1, 4, 3, 2, 6, 5]))
# print(reverse_array([4, 5, 2]))
# print(reverse_array([1]))



# Check if array is sorted
def sorted_array(arr):
    n=len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
        return True
    
print(sorted_array([10, 20, 30, 40, 50]))
print(sorted_array([90, 80, 100, 70, 40, 30]))