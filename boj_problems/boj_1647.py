from sys import stdin
read=stdin.readline

# 특정 원소가 속한 집합 탐색
def find_parent(x):
    if parent[x] != x:
        return find_parent(parent[x])
    else:
        return x

#두 원소가 속한 집합 합치기
def union_parent(a, b):
    a= find_parent(a)
    b= find_parent(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v, e = map(int, input().split())
parent = [i for i in range(v+1)]

towns = []
result= 0
for _ in range(e):
    a, b, cost = map(int, input().split())
    towns.append((cost, a, b))
towns.sort()

for cost, a, b in towns:
    if find_parent(a) != find_parent(b): #a, b이 같은 노드에 연결되어있는지 확인
        union_parent(a, b)
        result += cost
        _max = cost # if문 조건 속의 마지막 cost를 제거해야하므로 변수로 따로 지정필요
print(result - _max)



