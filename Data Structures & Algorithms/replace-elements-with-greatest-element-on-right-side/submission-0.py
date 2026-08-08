class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0,len(arr)-1):
            a1 = arr[i+1:]
            a =  max(a1)
            arr[i] = a

        arr[-1] = -1
        return arr
        