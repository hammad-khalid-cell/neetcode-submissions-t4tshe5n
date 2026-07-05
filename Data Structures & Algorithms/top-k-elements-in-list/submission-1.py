class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count  = {}

        for num in nums:
            if num not in count:
                count[num]=1
            count[num]+=1
        
        items = list(count.items())
        items.sort(key=lambda pair:pair[1], reverse=True)

        result =[]

        for i in range(k):
            result.append(items[i][0])
        return result


        

