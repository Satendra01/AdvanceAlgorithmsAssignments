import numpy as np
def checkSolutionsValidity():
    rows,cols=a.shape
    flag=0
    for i in range(rows):
        sum=0
        for j in range(cols):
            sum+=a[i][j]*primalVars[j]
        if sum>b[i]:
            flag=1
            break
        if flag==1 :
            break
    if flag==1:
        print(" Constraint {} is violated".format(i+1))
        return False
    else:
        return True
def calculatePrimalSlack():
    for i in range(noc):
        sum=0
        for j in range(nov):
            sum+=a[i][j]*primalVars[j]
        primalSlack.append(b[i][0]-sum)
#        print(primalSlack[i])
def calculateDualSlackAndVariableValues():
    for i in range(len(primalVars)):
        if primalVars[i]!=0:
            dualSlack.append(0)
        else:
            dualSlack.append(-1)
    for i in range(len(primalSlack)):
        if primalSlack[i]!=0:
           dualVars.append(0)
        else:
           dualVars.append(-1)
    c=a
    c=np.transpose(c)
    for i in range(len(dualSlack)):
        templist=np.empty([nov,1])
        for j in range(nov):
            if j==i:
                templist[j][0]=-1
            else:
                templist[j][0]=0
        c=np.concatenate((c,templist),axis=1)
#    print(c)
    d=np.empty([nov,1])
    for i in range(len(objcoeff)):
            d[i][0]=objcoeff[i]
#    print(dualVars)
    rows,cols=c.shape
    finalarr=np.empty([nov,1])
    finalarr=np.delete(finalarr,0,1)
#    print(finalarr)
    for j in range(cols-len(dualSlack)):
        if dualVars[j]!=0:
            tempcol=np.empty([nov,1])
            for k in range(rows):
                tempcol[k][0]=c[k][j]
            finalarr=np.concatenate((finalarr,tempcol),axis=1)
#            print(finalarr)
    for j in range(len(dualSlack)):
        if dualSlack[j]!=0:
            tempcol=np.empty([nov,1])
            for k in range(rows):
                tempcol[k][0]=c[k][len(dualVars)+j]
            finalarr=np.concatenate((finalarr,tempcol),axis=1)
#            print(finalarr)
    finalrows,finalcols=finalarr.shape
    val2=[]
    oldflag=0
# =============================================================================
#     print(finalrows,finalcols)
#     print(dualVars,dualSlack)
#     print(d)
# =============================================================================
    if finalrows!=finalcols and finalcols==1:
        for j in range(finalrows):
                if finalarr[j][0]==0 and d[j][0]!=0:
                    oldflag=1
                    break
                elif finalarr[j][0]!=0:
                    val2.append(d[j][0]/finalarr[j][0])
        for i in range(len(val2)-1):      
            if val2[i]!=val2[i+1] or val2[i]<0:
                oldflag=1
                varindex=i
                break
    
    if oldflag==1:
        print("The solution for dual does not exist since y{} is negative ".format(var+1))
        return False
    if(finalcols==0):
       print("All the variables in dual form have values 0 and therefore no solution exist")
       return False
#    print(oldflag)
    
    if finalcols!=finalrows:
        return False
    inverse=np.linalg.inv(finalarr)
    result=np.dot(inverse,d)
    k,flag=0,0
    resrows,rescols=result.shape
    for i in range(resrows):
        if result[i]<0:
            flag=1
            break
    if flag==0:
        return True
    else:
        print('The solution for dual does not exist')
        return False
#     for i in range(len(dualVars)):
#         if(dualVars[i]!=0):
#             dualVars[i]=result[i][0]
#             k++
#     for i in range(len(dualSlack)):
#         if dualSlack[i]!=0 && k<result.shape[0]:
#             dualSlack[i]=result[k][0]
#             k++
#     dualnetsum=0
#     for i in range(noc)
#         dualnetsum+=b[i][0]*dualVars[i]
#     primalnetsum=0    
#     for i in range(nov)
#         primalnetsum+=objcoeff[i]*primalVars[i]
#     if dualnetsum==primalnetsum:
#         return true
primalSlack=[]
dualSlack=[]
primalVars=[]
objcoeff=[]
dualVars=[]
print('Enter the number of variables')
nov=int(input())
print('Enter the number of constraints')
noc=int(input())
a=np.empty([noc,nov])
b=np.empty([noc,1])
print('Enter the coefficient of objective function')
for i in range(nov):
    objcoeff.append(int(input()))
for i in range(noc):
    print("Enter the coefficient of constraint {}".format(i+1))
    for j in range(nov):
        a[i][j]=int(input())
print('Enter the values of vector b')
for i in range(noc):
    b[i][0]=int(input())
print('Enter the coefficient of solution variables')
for i in range(nov):
    primalVars.append(int(input()))
print('The slack form is :')
for i in range(noc):
    for j in range(nov):
        print("{}x{} + ".format(a[i][j],(j+1)),end=" ")
    print("u{}={}".format((i+1),b[i][0]))
    print('')
value=checkSolutionsValidity()
if value==False:
    print('False')
else:
    calculatePrimalSlack()
    value=calculateDualSlackAndVariableValues()
    if value==False:
        print('False')
    else:
        print('True')