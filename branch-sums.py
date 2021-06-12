class BinaryTree:
    def bstTree(self, value):
        self.value = value
        self.left = None 
        self.right = None


def BranchSums(root):
    sums = []
    calculateBranchSums(root,0,sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return 
    
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newrunningSum)
        return 
    
    calculateBranchSums(node.left,newRunningSum, sums)
    calculateBranchSums(node.right,newRunningSum, sums)
