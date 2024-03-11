def convert_to_utf8(filename):
    # 以gbk编码打开HTML文件
    with open(filename + '.html', 'r', encoding='gbk', errors='ignore') as infile:
        content = infile.read()

    # 以UTF-8编码写回HTML文件
    with open(filename + '_utf8.html', 'w', encoding='utf-8') as outfile:
        outfile.write(content)

# 调用函数将HTML文件转换为UTF-8编码

filenamelist = ['life','life_acad','life_h+t','rsch','TBD',]
for filename in filenamelist:
    convert_to_utf8(filename)