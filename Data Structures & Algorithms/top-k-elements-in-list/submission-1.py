class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {
        }
        for i in nums:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        output = []
        maxamt = 0
        maxnum = []

        for i in dictionary:
            if dictionary[i] > maxamt:
                maxamt = dictionary[i]
                maxnum = [i]
            elif dictionary[i] == maxamt:
                maxamt = dictionary[i]
                maxnum.append(i)
        output = []
        sorted_items = sorted(dictionary.items(), key = lambda item:item[1], reverse = True)
        count = 0
        while k>0:
            output.append(sorted_items[count][0])
            count +=1 
            k -=1
        return output
            
            

