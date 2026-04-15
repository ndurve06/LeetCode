class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers1(self, l1, l2):
        list = []
        carry = 0
        for i in range(len(l1), 1, -1):
            for j in range(len(l2), 1, -1):
                digit = l1[i] + l2[j] + carry
                if digit >= 10:
                    carry = digit // 10
                    digit = digit % 10
                list.append(digit)
                print(list)
    
    def addTwoNumbers(self, l1, l2):
        temporary = ListNode(0)
        current = temporary
        carry = 0
        
        while l1 or l2 or carry:
            value_1 = l1.val if l1 else 0
            value_2 = l2.val if l2 else 0

            total = value_1 + value_2 + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return temporary.next