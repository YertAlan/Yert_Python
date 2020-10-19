#-*- coding:utf-8 -*-
#创建一个摇色子的游戏

import random

#生成一个色子的随机数
def ran_num():
    list = [1,2,3,4,5,6]
    n = random.choice(list)
    return n

#将三个色子的随机数进行总和
def ran_sum():
    s = 0
    list = []
    for i in range(3):
        n = ran_num()
        list.append(n)
        s = sum(list)
    print(list," = ",s)
    return s

#判断摇色子后的输赢
def ran_win(c):
    s = ran_sum()
    if s >= 11:
        if c == "Big":
            return True
        else:
            return False
    else:
        if c == "Small":            
            return True
        else:            
            return False
        

#获取选择，并根据选择和结果对比输赢
def choice():
    choi = ["Big","Small","Stop"]
    score = 1000
    while True:
        your_choice = str(input("Please input your choice: Big or Small or Stop\n"))
        
        if your_choice not in choi:
            print("Your choice is error")
        else:
            if your_choice == "Stop":
                break
            else:     
                n = ran_win(your_choice)
                if n == True:
                    score += 100
                    print("You're win,your score is ",score)
                else:
                    score -= 200
                    print("You're loose,your score is ",score)
        if score <= -1000:
            print("Your score is low -1000,game over.")
            break


def main():
    choice()


if __name__ == '__main__':
    main()  