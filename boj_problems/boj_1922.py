from sys import stdin
read=stdin.readline

N = int(input())
M = int(input())

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

parent = [0]*(N+1) #부모테이블 초기화

for i in range(1, N+1): #부모테이블에서 부모를 자기자신으로 초기화
    parent[i]=i

computers = []
result=0
for _ in range(M):
    a, b, cost = map(int, input().split())
    computers.append((cost, a, b))
computers.sort()

for computer in computers:
    cost, a, b = computer
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost
print(result)
