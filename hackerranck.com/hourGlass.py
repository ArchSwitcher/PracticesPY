def hourglassSum(arr):
    maxSum = -63
    
    for i in range(4):
        for j in range(4):
        
            # sum of top 3 elements
            top = sum(arr[i][j:j+3])
            
            # sum of the mid element
            mid = arr[i+1][j+1]
            
            # sum of bottom 3 elements
            bottom = sum(arr[i+2][j:j+3])
            
            hourglass = top + mid + bottom
          
            if hourglass > maxSum:
                maxSum = hourglass
        print(hourglass)
    return maxSum

if __name__ == "__main__":
    arr = [
        [1, 1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0], #010000
        [1, 1, 1, 0, 0, 0],
        [0, 0, 2, 4, 4, 0],
        [0, 0, 0, 2, 0, 0],
        [0, 0, 1, 2, 4, 0]
        ]

    result = hourglassSum(arr)
    print(str(result))
