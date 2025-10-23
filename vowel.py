x="nomaan"
dist=['aeiou']
for i in x:
    if i in dist:
      dist[i] += 1
      print(x,"exicted")
    else:
      dist[i]=1
print(dist)
string=(" i am nomaan shaik")
vowels='aeiouAEIOU'
count=sum(1 for x in string if x in vowels)
print(count)