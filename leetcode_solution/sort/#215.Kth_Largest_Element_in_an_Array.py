#  215. Kth Largest Element in an Array (medium)
#  https://leetcode.com/problems/kth-largest-element-in-an-array/
#
#  here we have sort-frist and find k-th largest or make a queue of k size, and 
#  output minimum val of the queue
#
class HeapSort:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.MaxheapSort(nums, k)
    
    def MaxheapSort(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, (-num, num))
                        
        for _ in range(k):
            _, e = heapq.heappop(heap)
            # print (e)
        return e
#
#
class MergeSort:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = self.mergeSort(nums)
        return nums[-k]
    
    def mergeSort(self, nums):
        '''
    https://runestone.academy/runestone/books/published/pythonds3/SortSearch/TheMergeSort.html
        '''
        if len(nums) <= 1: return nums
        
        mid = len(nums) // 2
        
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
            
        if i < len(left): nums[k:] = left[i:]  # if left is longer than right
        if j < len(right): nums[k:] = right[j:] # if right is longer than left
        return nums
#
#
class QuickSort:
    def findKthLargest(self, nums: List[int], k: int) -> int:        
        return self.quickSort(nums, k)
        
    def quickSort(self, nums, k):
        '''
        http://bookshadow.com/weblog/2015/05/23/leetcode-kth-largest-element-array/
        http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html
        '''
        import random
        pivot = random.choice(nums)
        nums1, nums2 = [], []
        for num in nums:
            if num > pivot:
                nums1.append(num)
            elif num < pivot:
                nums2.append(num)
        if k <= len(nums1):
            return self.findKthLargest(nums1, k)
        if k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))
        return pivot
#    
#    
class QueueSolution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        queue = []
        for num in nums:
            queue = self.isKth(queue, num, k)
        
        return queue[0]
                                
    def isKth(self, queue, num, k):
        if queue == []:
            queue.append(num)
        else:
            queue = self.InsertNum(queue, num, k)
        
        return queue[-k:]    
    
    def InsertNum(self, queue, num, k):
        if num >= queue[-1]:
            queue.append(num)
        elif num < queue[0]:
            queue.insert(0, num)
        elif queue[0] < num < queue[-1]:
            i = 1
            while i < len(queue)-1 and num > queue[i]:
                i += 1
            queue.insert(i, num)
                
        return queue