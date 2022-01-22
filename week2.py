# 주제: 1.문자열 입출력 // 2. 자료형

# [문자열 입출력]
## 문자열 입출력 연습문제
# str = input("이름을 입력하세요: ")
# print("%s님 안녕하세요?"%str)


## 문자열 입출력 Mission


# [자료형]
## 숫자형 1) 정수형(integer, int)
## : 소수점이 없는 숫자의 형태
## mission>> 정수형인 숫자를 출력하고 type() 함수를 활용하여
## 자료형을 주석으로 적기
# print(10000)
# print(type(10000))  #int 형


## 숫자형 2) 실수형(float)
## : 소수점이 있는 숫자의 형태
## mission>> 실수형인 숫자를 출력하고 type() 함수를 활용하여 자료형을 주석으로 적기
# print(0.589)
# print(type(0.589))


## 문자열
## : 문자를 나열한 형태의 자료형
## mission1>> ""와 ''를 활용하여 내가 지금 하고 싶은 말을 문자열로 출력하기
# str = "bavava"
# print(str)



## mission2>> 문자열로 인용구호('') 출력하기
# print("나는 '박'이다.")
# print('나는 "박"이다.')

## mission3>> sep과 end를 활용하여 print() 용법 익히기
## sep: ,로 출력이 구분된 문자열 사이 출력 설정 // end: print문의 끝났을 때의 문자열 출력 설정
# print(" 고양이는 ", " 강아지는 ",sep = " 야옹 ",end = " 멍멍 \n")
# print("안녕하세요")


## - 불린형(참/거짓)
## : 참(True)/거짓(False) 형태의 자료형
## mission>> 불린형의 True와 False를 출력하고 type() 함수를 활용하여
## 자료형을 주석으로 적기
# print(True)
# print(type(True)) #bool형이다.





# [변수]
## 변수란?: 데이터를 저장할 공간. 할당연산자(=)를 활용.
## 특징: "언제든지 데이터를 변경"할 수 있다.
## 문법: 변수이름 = 데이터

## mission>> 내가 좋아하는 게임의 캐릭터 혹은 재밋게 본 책의 정보를
## 변수로 저장하고 출력해보자.
## 예시) LOL 챔피언 정보: https://lol.inven.co.kr/dataninfo/champion/
name = "박정범"
age = 14
school = "불암중학교"
print("%s는 %d살이고 %s에 다닌다. "%(name, age, school))
print(f"{name}은 {age}살이고 {school}에 다닌다.")



## 변수 Mission: input()응용하기, 속으로 10초를 세어 맞히는 프로그램

