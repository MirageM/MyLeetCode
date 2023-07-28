class Solution(object):

    def answer(self, current, end, scalar):
        if current == end:
            return scalar
        self.visited.add(current)
        if current in self.graph:
            for i in self.graph[current]:
                if i[0] not in self.visited:
                    a = self.answer(i[0], end, scalar * i[1])
                    if a != 1:
                        return a
            return -1
