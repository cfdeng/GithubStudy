import random

# 生成一个1到100之间的随机数作为要猜的数字
number_to_guess = random.randint(1, 100)
guess_count = 0
guessed_correctly = False

print("欢迎来到猜数字游戏！")
print("我已经想好了一个1到100之间的数字，你来猜猜看哦。")

while not guessed_correctly:
    try:
        # 获取玩家的猜测
        player_guess = int(input("请输入你的猜测: "))
        guess_count += 1

        if player_guess == number_to_guess:
            guessed_correctly = True
            print(f"太棒了！你猜对了，答案就是{number_to_guess}，你一共猜了{guess_count}次。")
        elif player_guess < number_to_guess:
            print("猜小了，再试试吧。")
        else:
            print("猜大了，再试试吧。")
    except ValueError:
        print("请输入一个有效的整数哦。")




