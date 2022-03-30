n = int(input())
data = list(map(int, input().split()))
data.sort()  ## 공포도가 낮은 순으로 오름차순 정렬

result = 0  ##총 그룹의 수
count = 0   ##현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1        ## 현재 그룹에 반복문 순서에 해당되는 모험가 포함시키기
    if count >= i:    ## 만약 count(현재 그룹의 인원수)가 i(공포도)보다 크거나 같다면 그룹 결성
        result += 1   ## 총 그룹 수 증가 시키기
        count = 0     ## 현재 그룹에 포함된 모험가의 수 증가

print(result)
