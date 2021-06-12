#in this question we have a bst and
#a target value and we have to find 
# which value in the bst is closest 
#to our target value.

#First we will assign a variable closest 
#give it some big value like infinity
#LOGIC:
#we will find the absolute value of (target-closest) And 
# (target - tree value)
# if the absoulte value of target-closest is larger than
#absolute value of target - tree value than we will update our
#closest and 
#than compare the tree value to target value if tree value is 
#greater than target then we only have to traverse left side of 
#tree if its lower than rigt side of tree

#RECURSIVE WAY :-

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelper(tree,target,float("inf"))

def findClosestValueInBstHelper(tree,target,closest):
    if tree is None:
        return closest
    if abs(target-closest) > abs(target-tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left,target,closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest

def findClosestValueInBSt_1(tree, target):
    return findClosestValueInBstHelper1(tree,target,float("inf"))

def findClosestValueInBstHelper1(tree,target,closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target-closest) > abs(target-tree.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
    





    
