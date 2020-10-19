#-*- coding:utf-8 -*-
#求一组数字的总和，最大值，最小值和平均值

#numlist函数创建数字组
def numlist():
    l = []
    while True:
        try:
            
            a = int(input("Please input the num(0 is stop):"))
            if a == 0:
                break
            else:
                l.append(a)

        except:
            print("The num is error!!!")
    return l


def main():
    num_list = tuple(numlist())
    num_sum = sum(num_list) #求总和
    num_max = max(num_list) #求最大值
    num_min = min(num_list) #求最小值
    num_average = num_sum / len(num_list) #求平均值
    
    print("\n",num_list,"\n")
    print(" sum:",num_sum,'\n',"max:",num_max,"\n","min:",num_min,"\n","average:",num_average)


if __name__ == '__main__':
    main()