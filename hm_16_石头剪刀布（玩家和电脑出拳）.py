import random
# 1. 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
player = int(input("请输入您要出的拳-石头（1）／剪刀（2）／布(3):"))
# 2. 电脑 **随机** 出拳 —— 先假定电脑只会出石头，完成整体代码功能
computer = int(random.randint(1,3))
print("玩家出的拳是%d - 电脑出的拳是%d" % (player,computer))
# 3. 比较胜负（玩家胜的情况）
# | 1 | 石头 胜 剪刀 |
# | 2 | 剪刀 胜 布 |
# | 3 | 布 胜 石头 |
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("哎呦，我赢了")
#平局的情况
elif (player == computer):
    print("哎呀，真是心有灵犀一点通，平局了")
#电脑胜的情况
else:
    print("我输了")