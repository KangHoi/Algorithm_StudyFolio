import sys
import heapq

N=int(input())
lecture=[]
room=[]

lecture =[list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lecture.sort()

#첫번째 강의실에 가장 먼저 시작하는 강의 집어넣기
heapq.heappush(room, lecture[0][1])
for i in range(1,N): #2번째 강의부터 마지막 강의까지
    if room[0]>lecture[i][0]: #강의가 가장 먼저 끝나는 강의실보다 해당 강의 시작시간이 빠를 때
        heapq.heappush(room,lecture[i][1]) #해당 강의를 새로운 강의실에 배정
    else:
        heapq.heappop(room) # 해당 강의실에 저장된 강의 종료시간 삭제
        heapq.heappush(room,lecture[i][1]) #강의 종료시간 업데이트, 최소힙으로 정렬
print(len(room))




