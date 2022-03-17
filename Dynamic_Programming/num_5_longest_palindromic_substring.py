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








'''
Credit for explanation - https://leetcode.com/problems/longest-palindromic-substring/discuss/2921/Share-my-Java-solution-using-dynamic-programming/264539


A little explanation for why the indices in the for loops are set the way they are (I was really confused for a long time):

j must be greater than or equal i at all times. Why?
i is the start index of the substring, 
j is the end index of the substring. 
It makes no sense for i to be greater than j. Visualization helps me, so if you visualize the dp 2d array, think of a diagonal that cuts from top left to bottom right. 
We are only filling the top right half of dp.

Why are we counting down for i, but counting up for j? 
Each sub-problem dp[i][j] depends on dp[i+1][j-1] (dp[i+1][j-1] must be true and s.charAt(i) must equal s.charAt(j) for dp[i][j] to be true).





'''