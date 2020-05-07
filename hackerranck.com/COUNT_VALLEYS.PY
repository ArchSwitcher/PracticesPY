# def Count_valleys(s):
#     """D DU UD DU DU U UD = 2 ---UD D DU DU U = 1"""
#     s1 = list(s)
#     valleys = 0
#     array   = 'DU'
#     array2  = 'UD'
#     length  = len(s)
#     count   = 0
#     while(length != count):
#         try:
#             if s1[count] == 'D' and s1[count+1]=='U':
#                 # s2.append(s1[c]+s1[c+1])
#                 print(count , "DU")
#                 count+=1
#             elif s1[count] == 'U' and s1[count+1]=='D':
#                 # s2.append(s1[c]+s1[c+1])
#                 print(count ,"UD")
#                 valleys+=1
#                 count+=1
#             else:
            
#             count+=1
#         except IndexError:
#             return valleys
#     return valleys
#   Scanner sc = new Scanner(System.in);
#         int n = sc.nextInt();
#         String s = sc.next();
        
#         int v = 0;     // # of valleys
#         int lvl = 0;   // current level
#         for(char c : s.toCharArray()){
#             if(c == 'U') ++lvl;
#             if(c == 'D') --lvl;
            
#             // if we just came UP to sea level
#             if(lvl == 0 && c == 'U')
#                 ++v;
#         }
def Count_valleys(s):
    """D D U U    D D U D U U   U D = 2 ---UD D DU DU U = 1"""
    s1 = list(s)
    lvl = 0
    v = 0
    for c in s1:
        if c == 'U':
            lvl +=1
        elif c == 'D':
            lvl -=1

        if lvl == 0 and c =='U':
            v+=1
    
    return v

    
    
if __name__ == '__main__':
     
    path_valley = 'DUDUUUUUUUUDUDDUUDUUDDDUUDDDDDUUDUUUUDDDUUUUUUUDDUDUDUUUDDDDUUDDDUDDDDUUDDUDDUUUDUUUDUUDUDUDDDDDDDDD'
    # path_valley = 'UD U U UD UD D D'
    result = Count_valleys(path_valley)

    print(result)