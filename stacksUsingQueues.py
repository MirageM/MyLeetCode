# LeetCode 225. Implement Stack using Queues
# Time Complexity: O(n) Space Complexity: O(n)
# Left to Right (Stack)
class MyStack(object):

    def __init__(self):
        self.queue = collections.deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        q = self.queue
        q.append(x)
        for i in range(len(q) - 1):
            q.append(q.popleft())
        
        

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()