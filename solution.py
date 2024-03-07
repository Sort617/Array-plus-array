def array_plus_array(arr1,arr2):
    arr1.extend(arr2)
    a = len(arr1)
    count = 0
    sum = 0
    while count < a:
        sum = sum + arr1[count]
        count += 1
    return sum
        
