//1
tc=int(input())
for i in range(tc):
    n=int(input())
    arr=input()
    dic={}
    count=0
    for i in range(n):
        if arr[i] not in dic:
            dic[arr[i]]=1
        else:
            dic[arr[i]]+=1
    for k in dic:
        if dic[k]%2!=0:
            count+=1
    if count==0 or count==1:
        print("Possible!")
    else:
        print("Not Possible!")
//2
n=int(input())
arr=list(map(int,input().split()))
dic={}
sumi=0
for i in range(len(arr)):
    if arr[i] not in dic:
        dic[arr[i]]=1
    else:
        dic[arr[i]]+=1
for k ,v in dic.items():
    if dic[k]==1:
        sumi+=k
print(sumi)

//3
n=int(input())
mat=[]
for i in range(n):
    arr=list(map(int,input().split()))
    mat.append(arr)
for i in range(n):
    mat[i].reverse()
        
for i in range(n):
    for j in range(n):
        if mat[i][j]==1:
            print(0,end=" ")
        elif mat[i][j]==0:
            print(1,end=" ")
    
    print()
 
