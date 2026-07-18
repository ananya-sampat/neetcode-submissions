#class Solution:
#    def productExceptSelf(self, nums: List[int]) -> List[int]:
#        productList = []
#        product = 1
#        current = 0
#        while current < len(nums):
#            for n in range(len(nums)):
#                if n != current:
#                    product *= nums[n]
#            productList.append(product)
#            current += 1
#            product = 1
#        return productList

# more efficient
#class Solution:
#    def productExceptSelf(self, nums: List[int]) ->List[int]:
#        leftProducts=[]
#        rightProducts=[]
#        
#        for n in range(len(nums)):
#            left = 1
#            right = 1
#            for i in range(n):
#                left *=nums[i]
#            for j in range(n+1, len(nums)):
#                right *= nums[j]
#            leftProducts.append(left)
#            rightProducts.append(right)
#        products=[]
#        for i in range(len(leftProducts)):
#            products.append(leftProducts[i]*rightProducts[i])
#        return products

# better 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1] * len(nums)
        rightProducts = [1] * len(nums)

        for i in range(1, len(nums)):
            leftProducts[i] = leftProducts[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            rightProducts[i] = rightProducts[i + 1] * nums[i + 1]

        products = []

        for i in range(len(nums)):
            products.append(leftProducts[i] * rightProducts[i])

        return products

            
