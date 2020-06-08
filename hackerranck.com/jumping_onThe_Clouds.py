def jumpingOnClouds(c, n):
    index = 0
    jumpNumber = 0

    while index < len(c):
        # print("variable i en %s" % index )
        # try:
            # if c[index+1] == 1:
            #     print("index+1")
            #     index +=2
            #     jumpNumber += 1
        if c[index+2] == 0:
            index += 2
            jumpNumber+=1
            print("index+2  ")
        #     else:
        #         jumpNumber += 1
        #         index+=1
        #         print("else")
        # except IndexError:
            # jumpNumber+=1
            break
    return jumpNumber
#  0 0 0 1 0 0 1
     

if __name__ == "__main__":
    # list1 = [0,1,0,0,0,1,0]
    # list1 = [0,0,0,0,1,0]
    # list1 = [0, 0, 0, 1, 0, 0]
    # list1 = [0, 0, 1, 0, 0, 1, 0]
    list1 = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
    n = 7
    result = jumpingOnClouds(list1, n)
    print(result)