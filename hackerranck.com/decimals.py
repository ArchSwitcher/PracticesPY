def plusMinus(arr):
    arry = []
    print("{}".format(round(len([i for i in arr if i > 0])/len(arr),6))) 
    print("{}".format(round(len([i for i in arr if i < 0])/len(arr),6))) 
    print("{}".format(round(len([i for i in arr if i == 0])/len(arr),6))) 

if __name__ == "__main__":
    n= int(12)
    arrat = [1,2,3,4,5,6,7,-9,-3,-6,-8,-7,9,0,0]
    arr = list(map(int, arrat))

    plusMinus(arr)