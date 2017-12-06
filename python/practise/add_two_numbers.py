'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = curr = ListNode(0)
        carray = 0

        p = l1
        q = l2

        while p or q or carray:
        	x = y = 0
        	
        	if p:
        		x = p.val
        		p = p.next
        	if q:
        		y = q.val
        		q = q.next

        	sum = x + y + carray
        	carray = sum // 10        

        	curr.next = ListNode(sum % 10)
        	curr = curr.next      	

        return dummy.next

# Complexility ( O(max(m,n)) ), m,n is the lenght of l1 and l2 respectively

# testcase
def to_list_node(arr):
	ln = l = ListNode(0)
	for i in range(len(arr)):
		l.next = ListNode(arr[i])
		l = l.next

	return ln.next

def to_array(listNode):
	arr = []
	while listNode:
		arr += [listNode.val]
		listNode = listNode.next

	return arr


l1 = to_list_node([0, 1])
l2 = to_list_node([0, 1, 2])

assert to_array(Solution().addTwoNumbers(l1, l2)) == [0, 2, 2]

l1= to_list_node([])
l2= to_list_node([0,1])

assert to_array(Solution().addTwoNumbers(l1, l2)) == [0, 1]

l1 = to_list_node([9,9])
l2 = to_list_node([1])

assert to_array(Solution().addTwoNumbers(l1, l2)) == [0, 0, 1]