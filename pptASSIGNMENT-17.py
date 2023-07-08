#!/usr/bin/env python
# coding: utf-8

# In[1]:


#aNSWER1:
def first_unique_char(s):
    freq = {}

    # Update frequency of each character
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Find the first character with frequency 1
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i

    return -1


# Example usage:
s = "leetcode"
result = first_unique_char(s)
print(result)  

s = "loveleetcode"
result = first_unique_char(s)
print(result)  

s = "aabb"
result = first_unique_char(s)
print(result)  


# In[2]:


#anSWER2:


def max_subarray_sum(nums):
    n = len(nums)
    max_sum = curr_max = nums[0]

    # Find maximum sum of non-circular subarray
    for i in range(1, n):
        curr_max = max(nums[i], curr_max + nums[i])
        max_sum = max(max_sum, curr_max)

    if max_sum >= 0:
        return max_sum

    # Find minimum sum subarray
    min_sum = curr_min = nums[0]
    for i in range(1, n):
        curr_min = min(nums[i], curr_min + nums[i])
        min_sum = min(min_sum, curr_min)

    total_sum = sum(nums)
    return max(max_sum, total_sum - min_sum)


# Example usage:
nums = [1, -2, 3, -2]
result = max_subarray_sum(nums)
print(result)  

nums = [5, -3, 5]
result = max_subarray_sum(nums)
print(result)  

nums = [-3, -2, -3]
result = max_subarray_sum(nums)
print(result)  


# In[5]:


from collections import deque

def count_students_unable_to_eat(students, sandwiches):
    student_queue = deque(students)
    count = 0

    while count < len(student_queue):
        if student_queue[0] == sandwiches[0]:
            student_queue.popleft()
            sandwiches.pop(0)
            count = 0
        else:
            student_queue.append(student_queue.popleft())
            count += 1

    return len(student_queue)


# Example usage:
students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
result = count_students_unable_to_eat(students, sandwiches)
print(result) 


# In[ ]:


if count == len(student_queue):
           return len(student_queue)

   return 0


# In[6]:


students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]
result = count_students_unable_to_eat(students, sandwiches)
print(result) 



# In[7]:


#Answer 4:
from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)

        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()

        return len(self.requests)

# Example usage:
recentCounter = RecentCounter()
print(recentCounter.ping(1))   
print(recentCounter.ping(100)) 
print(recentCounter.ping(3001))
print(recentCounter.ping(3002))


# In[8]:


#Answer5:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findTheWinner(n: int, k: int) -> int:
    # Create circular linked list representing the friends
    head = ListNode(1)
    current = head
    for i in range(2, n+1):
        current.next = ListNode(i)
        current = current.next
    current.next = head  # Make it circular

    # Iterate until only one friend is left
    while current.next != current:
        # Count k-1 friends in the clockwise direction
        for _ in range(k - 1):
            current = current.next

        # Remove the next friend from the circle
        current.next = current.next.next

    return current.val

# Example usage:
n = 5
k = 2
winner = findTheWinner(n, k)
print(winner)  


# In[9]:


n = 6
k = 5
winner = findTheWinner(n, k)
print(winner)  


# In[10]:


#Answer6: 

import collections

def deckRevealedIncreasing(deck):
    n = len(deck)
    deck.sort()
    queue = collections.deque()

    for i in range(n - 1, -1, -1):
        if queue:
            queue.appendleft(queue.pop())
        queue.appendleft(deck[i])

    return list(queue)

# Example usage:
deck = [17, 13, 11, 2, 3, 5, 7]
ordering = deckRevealedIncreasing(deck)
print(ordering)  


# In[11]:


deck = [1,1000]
ordering = deckRevealedIncreasing(deck)
print(ordering)  


# In[13]:


#Answer7:
from collections import deque

class FrontMiddleBackQueue:
    def __init__(self):
        self.front = deque()
        self.back = deque()

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)
        self._balance()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._balance()

    def popFront(self) -> int:
        if self.front:
            return self.front.popleft()
        elif self.back:
            return self.back.popleft()
        else:
            return -1

    def popMiddle(self) -> int:
        if len(self.front) == len(self.back):
            return self.front.pop()
        elif len(self.front) > len(self.back):
            return self.front.popleft()
        else:
            return self.back.pop()

    def popBack(self) -> int:
        if self.back:
            return self.back.pop()
        elif self.front:
            return self.front.pop()
        else:
            return -1

    def _balance(self) -> None:
        if len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())
        elif len(self.front) < len(self.back):
            self.front.append(self.back.popleft())


# In[14]:


operations = ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
values = [[], [1], [2], [3], [4], [], [], [], [], []]

queue = FrontMiddleBackQueue()
output = []
for op, val in zip(operations, values):
    if op == "pushFront":
        queue.pushFront(val[0])
        output.append(None)
    elif op == "pushBack":
        queue.pushBack(val[0])
        output.append(None)
    elif op == "pushMiddle":
        queue.pushMiddle(val[0])
        output.append(None)
    elif op == "popFront":
        output.append(queue.popFront())
    elif op == "popMiddle":
        output.append(queue.popMiddle())
    elif op == "popBack":
        output.append(queue.popBack())

print(output)


# In[22]:


#Answer8:
from collections import deque

class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stream = deque()

    def consec(self, num: int) -> bool:
        self.stream.append(num)
        if len(self.stream) < self.k:
            return False
        for i in range(len(self.stream) - self.k, len(self.stream)):
            if self.stream[i] != self.value:
                return False
        return True


# In[23]:


operations = ["DataStream", "consec", "consec", "consec", "consec"]
values = [[4, 3], [4], [4], [4], [3]]

data_stream = DataStream(*values[0])
output = [None]
for num in values[1:]:
    output.append(data_stream.consec(*num))

print(output)


# In[ ]:




