# Question 2

def electric_bike_booking(bookings):
    arr=[] #empty array that will hold the range of bookings
    newArray=[] #empty array that will hold the arr without subarrays

    for items in bookings:
        #changing elements in array into a range 
        itemRange= range(items[0],items[1])
        #creating a list contain all subarrays
        arr.append(itemRange)
    #turning subarray into one array
    for subarray in arr:
        for nums in subarray:
            newArray.append(nums)
            #creating a set to remove duplicates
            newSet=set(newArray)
    #comparing the length of an array with duplicates and the length of the set
    #if the length is equal we return true, else false
    if len(newArray)==len(newSet):
        return True
    else:
        return False

        
print(electric_bike_booking([[1,4], [2,5], [7,9]]))  #output False because [1,4],[2,5] overlap
print(electric_bike_booking([[6,7], [2,4], [8,12]])) #output True because there is no overlap
print(electric_bike_booking([[4,5], [2,3], [3,6]])) #output False because [4,5], [3,6] overlap
