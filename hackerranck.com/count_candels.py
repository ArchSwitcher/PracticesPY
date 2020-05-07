from collections import Counter

def birthdayCakeCandles(ar):
    repeated_candels = Counter(ar)
    cnt = max(repeated_candels)
    return repeated_candels[cnt]

    
if __name__ == '__main__':
    
    ar = [18, 75, 75, 13, 9, 75, 9, 8, 9, 43]
    result = birthdayCakeCandles(ar)
    print(result)