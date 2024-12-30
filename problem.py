def addParentheses(breaket,n,right_n,string,array):
    string=string+breaket
    if right_n==0 or (n==1 and right_n==1) :
        string=string+"("*right_n+")"*n
        array.append(string)
    elif right_n<n :
        addParentheses("(",n,right_n-1,string,array)
        addParentheses(")",n-1,right_n,string,array)
    elif right_n==n :
        addParentheses("(",n,right_n-1,string,array)

    return array 

n=3
right_n=n-1
string =""
array =[]
print(addParentheses("(",n,right_n,string,array))