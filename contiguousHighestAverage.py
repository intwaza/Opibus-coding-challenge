# Question 1.
import decimal
def contiguous_average(array):
    #check if values in array are positive numbers
    for nums in array:
        if nums>0:
            newArr=[]
            #creating subarrays in array
            for element in range(len(array)-1):
                arrSlice=array[element:element+2]
                #adding the elements in subarrays 
                sum= arrSlice[0]+arrSlice[1]
                #append the sum of elements in subarrays in a new array
                newArr.append(sum)
                average=newArr[0]
                #check the highest number in the new array and find it's average
                for nums in newArr:
                    if nums>average:
                        average=nums
                        return decimal.Decimal(average)/2
    
print(contiguous_average([2, 3, 4, 1, 5])) #output: 3.5 [3,4]
print(contiguous_average([6,7, 2,4, 8,12])) #output: 10 [8,12]
