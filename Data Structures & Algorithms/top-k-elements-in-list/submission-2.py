class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #idea: sorted dict of k elements key is the number value is the frequency -> first k just put in dictionary then if i get a frequency higher than dict[k] remove dict[k] and add new key val pair and sort 
        top_dict = dict()
        for num in nums:
            if num in top_dict:
                 top_dict[num] +=1
                    
            else:
                 top_dict[num] = 1
                    
        top_dict = sorted(top_dict.items(), key =lambda item: item[1]) 
        topk= []
        for i in range(k):
            topk.append(top_dict[len(top_dict)-i-1][0])
        return topk
                      
        