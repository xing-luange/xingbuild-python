
code = input("请输入您的代码文件名：")
with open(code, 'r') as f:
    data = f.readlines()[1]
    language = data.replace('#语言 = ', "")
    print(language)