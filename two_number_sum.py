#in this problem we have to find 
#two number which is equals too 
#target sum.

#first approach is to traverse the 
#array in nested loops

#O(n^2) time || O(1) space

def twoNumberSum(arr,targetSum):
    for i in range(len(arr)-1):
        firstNum = arr(i)
        for j in range(i+1,len(arr)):
            secondSum=arr[j]
            if firstNum + secondSum == targetSum:
                return [firstNum,secondSum]
    return("Numbers not find in the array")

# second approach is to make hash table//hash map
#O(n) || O(n) space

def twoNumberSum(arr, targetSum):
    nums = {} #intializing dictionary
    for i in arr:
        if targetSum - i in nums:
            return [targetSum-1, i]
        else:
            nums[i] = True
    return("Number not found in array")

# their is the third apporach to solve this 
# problem by sorting the array and then
# run two pointer from 0 index to last index 
# of the array.
# the idea is that if the Sum value of these index is 
# grater than targetSum then the right pointer
# moves towards left beacuse value is grater than 
# targetSum thats so we have to decrease the value 
# to get targetSum.
# if the Sum value is less than the targetSum then left pointer
# moves towards right.
# 
# 
# O(nlogn) || O(1) space        

def twoNumberSum(arr,targetSum):
    arr.sort()
    left = 0
    right = len(arr)-1
    while left<right:
        currentSum = arr[left] + arr[right]
        if currentSum == targetSum:
            return[arr[left],arr[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right += 1
    return ("No number found which is equal to the targetSum")




