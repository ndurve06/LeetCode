# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        previous, current = dummy, head

        while current and current.next:
            next_pair = current.next.next
            second = current.next

            second.next = current
            current.next = next_pair
            previous.next = second

            previous = current
            current = next_pair
        
        return dummy.next
    


testing = Solution()
print(testing.swapPairs([1,2,3,4]))
print(testing.swapPairs([]))
print(testing.swapPairs([1]))

#runtime: 0ms, beats 100.00%
#memory: 19.28MB, beats 60.97%