#coding=utf-8
'''
def min(*args):
    list_num = list(args)
    
    for i in range(len(list_num)):
        
        if list_num[i-1] < list_num [i]:
            r = list_num[i-1]
            list_num[i-1] = list_num[i]
            list_num[i] = r
        print(list_num)
    
 '''   
def bubble_min(*args):
    list_num = list(args) 

    for a in range(len(list_num)-1): #定义外循环
        
        for b in range(len(list_num)-a-1): #定义内循环
            print(a,"--",b)
            if list_num[b] < list_num[b+1]:
                r = list_num[b]
                list_num[b] = list_num[b+1]
                list_num[b+1] = r
            print(list_num,'-----\n')
    
    print("result :",list_num)


    

bubble_min(1,2,3,4,2)