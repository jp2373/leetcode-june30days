class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        answer = []
        
        people.sort(key = lambda x : (-x[0], x[1]))
        
        for x in people:
            answer.insert(x[1], x)
        return answer
