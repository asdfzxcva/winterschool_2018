import random

ans1 ="그렇게 하는게 맞아"
ans2 ="그건 좀 아닌 것 같아"
ans3 ="그것도 괜찮아"
ans4 ="응 아니야"
ans5 ="그래"
ans6 ="그만해!"



print("mymagic8ball에 오신 것을 환영합니다.")

question = input("조언을 구하고 싶으면 질문을 입력하고 엔터 키를 누르세요.\n")

print("고민 중...\n" *4)

choice = random.randint(1,6)
if choice == 1:
                 answer=ans1
elif choice == 2:
                 answer=ans2
elif choice == 3:
                 answer=ans3
elif choice == 4:
                 answer=ans4
elif choice == 5:
                 answer=ans5
elif choice == 6:
                 answer=ans6

print(answer)

input("\n\n 마치려면 엔터 키를 누르세요 ")
