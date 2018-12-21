import copy
people=[
    [0,-1,-1,-1],
    [0,0,0,1],
    [0,1,0,0],
    [-1,-1,-1,0]
]
find_flage=0


#-1 unknow 0 No 1 Yes
def change(X):
    count=0
    for a in X:
        if a ==-1:
            count+=1
        if count==3:
            for j in range(len(X)):
                if X[j]==-1:
                    X[j]=0
                else:
                    X[j]=1
            return X
    for i in range(len(X)):      
        if X[i]==0:
            X[i]=-1
        elif X[i]==1:
            X[i]=0
        elif X[i]==-2:
            X[i]=2
    return X



def bijioa(people):
    flage_bijioa=[0,0,0,0]
    for i in range(len(people)):
        logic=[]
        for j in range(len(people[i])):
            logic.append(people[j][i])
        if 0 not in logic :
            flage_bijioa[i]=1
        elif i not in logic:
            flage_bijioa[i]=1
    '''
        #error--
        elif -2 in logic:
            sit=logic.index(2)
            change(people[sit])
            people [i][sit]=-1 
            bijioa(people)
        #---

    '''
    if 0 not in flage_bijioa or 1 not in flage_bijioa:
        return True
    else:
        return False



def find_ture(people):
    people_1=copy.deepcopy(people)
    for i in range(len(people_1)):
        people_1=copy.deepcopy(people)
        for j in range(len(people_1)):
            if i==j :
                continue
            else:
                people_1[j]=change(people_1[j])
        if bijioa(people_1):
            find_flage=1
            return i+1
def find_sb():
    for i in ['A','B','C','D']:
        if(i!='A')+(i=='D')+(i=='B')+(i!='D')==1:
            print('罪犯是' ,i)
def main():
    anwer=find_ture(people)
    print('说真话的是:',anwer)
    find_sb()


main()






