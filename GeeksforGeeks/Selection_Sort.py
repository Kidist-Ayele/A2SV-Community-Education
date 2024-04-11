class Solution: 
    def select(self, arr, i):
        # code here
        
        self.selectionSort(arr, len(arr))
            
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(0, n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[j], arr[min_index] = arr[min_index], arr[j]