# Really easy for a 10p

friend = [[],[6],[6],[4,5,6,15],[3,5,6],[3,4,6],[1,2,3,4,5,7],[6,8],[7,9],[8,10,12],[9,11],[10,12],[9,11,13],[12,14,15],[13],[3,13],[17,18],[16,18],[16,17],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

while True:
    action = input()
    if action == "i":
        x = int(input())
        y = int(input())
        friend[x].append(y)
        friend[y].append(x)
    elif action == "n":
        x = int(input())
        print(len(friend[x]))
    elif action == "d":
        x = int(input())
        y = int(input())
        friend[x].remove(y)
        friend[y].remove(x)
    elif action == "f":
        fof = set()
        x = int(input())
        for fri in friend[x]:
            for i in friend[fri]:
                if i not in friend[x] and i != x:
                    fof.add(i)
        print(len(fof))
    elif action == "s":
        x = int(input())
        y = int(input())
        s = x
        q=[]  
        vis=[0 for i in range(51)]
        dist=[0 for i in range(51)]
        q.append(s)
        vis[s] = 1
        while(len(q)):
            topNode = q.pop(0) 
            for node in friend[topNode]:
                if not vis[node]:
                    vis[node] = 1
                    dist[node] = dist[topNode] + 1
                    q.append(node)
        if x == y:
            print(0)
        elif dist[y] > 0:
            print(dist[y])
        else:
            print("Not connected")
    else:
        break
