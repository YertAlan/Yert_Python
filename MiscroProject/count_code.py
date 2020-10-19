#coding=utf-8
#统计指定目录下的所有python代码行数
import os

#获取目录下所有.py后缀文件的文件名和路径
def file_get():
    file_list = []
    path = 'd:/Python/test' #指定文件路径
    for root,dirs,files in os.walk(path):
        for file in files:
            if file.endswith(".py") == True:                    #get all of python file name in the dir         
                file_list.append((os.path.join(root,file)).replace('\\','/'))  #将路径的\\替换为/
    
    return file_list

#统计单个文件的代码行数
def count_lines(s):
    file = open(s,encoding="UTF-8")  #encoding避免read方法读取中文字符出现报错
    lines = []
    for line in file.readlines():
        #排除注释
        if line[0] == '#':
            continue        
        line_cl = clear_str(line)        
        lines.append(line_cl.rstrip('\n').strip())
        
    file.close
    lines = [ls for ls in lines if ls != '']
    LS = [x for x in lines if isQuotes(x) == False]    
    return len(LS)

#将代码中的中文字符去除
def clear_str(s):    
    content_str = ""
    for i in s:
        if is_ch(i) == True:
            content_str += i
    return(content_str)    
    

#检查字符是否是中文字符
def is_ch(uchar):
    if u'\u4e00' <= uchar <= u'\u9fff':
        return False
    else:
        return True

#检查字符串是否是以'或"开头的注释字符串
def isQuotes(s):
    if s.startswith('\'') or s.startswith('\"'):
        return True
    else:
        return False

def main():
    files = file_get()
    core_count = {}
    core_sum = 0
    for file in files:       
        core_count[file] = count_lines(file)    
    for ks in core_count.keys():
        core_sum += core_count[ks]
        print(ks,'---',core_count[ks],'\n')
    print("The file sum :",len(files))
    print('The core sum :',core_sum)



if __name__ == '__main__':
    main()  