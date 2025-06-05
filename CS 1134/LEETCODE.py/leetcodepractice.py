# QUESTION 1:


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        self.nums=nums
        self.target=target
        right=len(nums)
        for i in range(left, right):
            for j in range(i+1,right):
                if self.nums[i]+self.nums[j]==target:
                    return [i,j]




# QUESTION 2:


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(l1, l2):
        s1=""
        s2=""
        s3=0
        for i in l1[::-1]:
            s1.append(str(i))
        for i in l2[::-1]:
            s2.append(str(i))
        s3=int(s1)+int(s2)
        result=[]
        for i in s3[::-1]:
            result.append(int(i))
        return result
        

    def addTwoNumbers(l1, l2):
        s1=""
        s2=""
        s3=0
        for i in l1[::-1]:
            s1.append(str(i))
        for i in l2[::-1]:
            s2.append(str(i))
        s3=int(s1)+int(s2)
        result=[]
        for i in s3[::-1]:
            result.append(int(i))
        return result

        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """



# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]


# Question 3:

# You are given a string word, and an integer numFriends.

# Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:

# word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
# All the split words are put into a box.
# Find the lexicographically largest string from the box after all the rounds are finished.

 

class Solution(object):

    if n<numFriends:
    
    else:
        n=0
    def answerString(self, word, numFriends):
        resulttemp=[]
        finalresult=[]
        for i in range(0,numFriends):
            for j in range(i,len(word)-numFriends+i):
                resultemp.append(word[i,j])
            finalresult.append(max(resulttemp))
        return max(finalresult)
        for i in resultbox:
            scores={}
            for j in i:
                if i not in scores:
                    scores[i]==0
                else:
                    scores[i]+=ord(j)
                

        tempword=word[i:len(word)-i-numFriends]

    

