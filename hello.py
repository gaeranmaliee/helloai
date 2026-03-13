print("안녕하세요! 파이썬 공부를 시작합니다!")
import random  # 1. 무작위 숫자를 만들기 위한 도구 가져오기

# 컴퓨터가 1~100 사이의 비밀 숫자를 선택합니다.
secret_number = random.randint(1, 100)
attempts = 0  # 시도 횟수를 저장할 변수

print("🤖: 1부터 100 사이의 숫자를 하나 골랐습니다. 맞춰보세요!")

# 2. 맞힐 때까지 계속 반복하는 'while' 반복문
while True:
    try:
        # 3. 사용자로부터 입력 받기 (숫자로 변환)
        guess = int(input("숫자를 입력하세요: "))
        attempts += 1  # 시도 횟수 1 증가

        # 4. 비교하기 (if-elif-else 조건문)
        if guess < secret_number:
            print("UP! 더 큰 숫자예요.")
        elif guess > secret_number:
            print("DOWN! 더 작은 숫자예요.")
        else:
            print(f"🎉 정답입니다! {attempts}번 만에 맞히셨네요!")
            break  # 정답을 맞혔으므로 반복문 탈출!
            
    except ValueError:
        print("❌ 숫자만 입력해 주세요!")