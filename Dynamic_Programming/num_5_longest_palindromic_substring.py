x = "BABAD"
def longest_palindrome(x):
    res = ''
    table = [[0]*len(x) for _ in range(len(x))]#Create a table for all strings
    #print(table)
    y = len(table) 

    for i in range(y):## We make sure our diagnol is true
        table[i][i] = 1

        
    res = x[i] ## last diagnol
    for j in range(len(x)):
        for i in range(j):## Travel through the array with i 
            #t = f'x[{i}] = {x[i]} and x[{j}] = {x[j]}'
            #g = f'table[{i+1}][{j-1}]'
            #print(t)
            if x[i]==x[j] and (table[i+1][j-1] or j==i+1): ## if its next to diagnol, its good
                #print(j-1,i+1,table[i+1][j-1])
                #print(x[i],x[j],table[i+1][j-1])
                #print(j-i)
                #print(t)
                #print(g)
                table[i][j]=True
                if j-i+1>len(res):
                    res=x[i:j+1]
                    #print(res)
        #print(table)
        #print(res)
    return res

i = longest_palindrome("BABAD")
print(i)