
arr=[1,4,35,6,34,7,3]

def bubble(arr):
    
    n=len(arr)

    for i in range(n):
        for j in range(0,n-i-1):

            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]


    return arr

print(bubble(arr))