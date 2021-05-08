def Collision(V):
    count=0
    i=1
    while i<len(V):
        if V[i] < V[i-1]:
            count+=1
        i+=1
    print(count)
T=input()
N=input()
V=input()
Collision(V)
