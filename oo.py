import random

# 숫자와 가위바위보를 연결하는 딕셔너리
# 1을 넣으면 "가위"가 나오는 마법의 사전입니다.
rps_map = {1: "가위", 2: "바위", 3: "보"}

user_wins = 0
computer_wins = 0

print("🏆 숫자 가위바위보 삼세판! (1:가위, 2:바위, 3:보)")

while user_wins < 2 and computer_wins < 2:
    print(f"\n현재 스코어 - 나: {user_wins} | 컴퓨터: {computer_wins}")
    
    user_input = input("숫자를 선택하세요 (1, 2, 3): ")
    
    # 1. 입력값이 숫자인지 확인하고 변환
    if not user_input.isdigit() or int(user_input) not in [1, 2, 3]:
        print("❌ 1, 2, 3 중에서만 골라주세요!")
        continue
    
    user_choice_num = int(user_input)
    user_choice = rps_map[user_choice_num] # 숫자를 "가위/바위/보" 글자로 변환
    
    # 2. 컴퓨터의 선택 (1~3 사이 무작위)
    computer_choice_num = random.randint(1, 3)
    computer_choice = rps_map[computer_choice_num]

    print(f"나: {user_choice} vs 컴퓨터: {computer_choice}")

    # 3. 승패 판정
    if user_choice == computer_choice:
        print("🤝 비겼습니다!")
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        print("✅ 이겼습니다!")
        user_wins += 1
    else:
        print("💀 졌습니다...")
        computer_wins += 1

# 최종 결과
print("\n" + "="*20)
if user_wins == 2:
    print("🎊 축하합니다! 최종 승리하셨습니다!")
else:
    print("🤖 컴퓨터가 최종 승리했습니다!")
print("="*20)