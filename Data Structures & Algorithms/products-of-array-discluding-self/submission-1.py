class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productList = []
        product = 1
        current = 0
        while current < len(nums):
            for n in range(len(nums)):
                if n != current:
                    product *= nums[n]
            productList.append(product)
            current += 1
            product = 1
        return productList

            
