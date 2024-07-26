class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       l=[]
       for i in range(len(numbers)):
        if target-numbers[i] in numbers:
            l.append(i+1)
            if i==numbers.index(target-numbers[i]):
                l.append(numbers.index(target-numbers[i])+2)
            else:
                l.append(numbers.index(target-numbers[i])+1)
            return l