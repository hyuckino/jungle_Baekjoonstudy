##ver.1 실패 이유 : 등차가 유지되는 조건을 생략함 233도 한수로 출력 0이상만되도됨
number=input()
#첫번째 자리수수
#등차:두번째 자리수-첫번째 자리수/ 등차가 음수 일 경우 : 성립 불가?
#등차를 뺏을때 각 자리수가 양수여야함 : 음수가 되면  while or for문 탈출
#변수명 중복 조심 i==>num으로 바꿈 number을 for문 내에서 잘 못 사용함
count=0
for num in range(1,int(number)+1):
    if num<100:
        count+=1
    else:
        num=str(num)
        d=int(num[1])-int(num[0])
        for i in range(1,len(num)-1):

            if int(num[i])+d==int(num[i+1]):
                
                if i==len(num)-2:
                    count+=1
                continue
            else:
                break
print(count)