N= int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

oil = cities[0]
sum = 0
for i in range(N-1):
    if oil > cities[i]:
        oil = cities[i] #현재의 최저 기름값보다 더 저렴하면 기름값 갱신
    sum += (oil*roads[i])

print(sum)