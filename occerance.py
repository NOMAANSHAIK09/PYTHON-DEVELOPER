list=[1,2,1,3,4,2,4,3,7,6,7,6]
dist={}
for x in list:
    if x in dist:
      dist[x] += 1
      print(x,"exicted")
    else:
      print(x," not exicted")
      dist[x]=1
print(dist)