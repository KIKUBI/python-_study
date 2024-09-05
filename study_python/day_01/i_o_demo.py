# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      i_o_demo.py
# Author:       lao_zhao
# Datetime:     2024/8/7 11:14
# Description:
# 
# ---------------------------------------------------------------------------


"""
    io流：i:input, o:output

    io流中如何获取文件对象：open函数
        open("文件路径", mode="对文件的操作模式"[, encoding="utf-8"]): 返回文件对象，open函数中就指明了文件的操作方式。
            # utf-8的编码格式没法表示文件内容时，操作文件的编码格式。比如：图片，视频等。

        文件的操作模式：
            r: 只读
                r+: 可读可写，读取时可以正常读取，写入时会进行文件内容的覆盖，或者在写入时会写入到文件的末尾。---不要使用。
            w: 只写--写入内容时，会对文件的内容进行全覆盖
                w+: 可读可写，写入内容时，正常写入，如果读取时，读取时也会读文件的内容全覆盖。---不要使用。
            a: 追加--写入内容时，会将写入的内容追加到文件的末尾
                a+: 可读可写, 写入时正常写入，读取时，因为文件的指针默认在末尾，所有读取不到任何内容。

            b: 一般时操作二进制相关的文件，b的模式不能单独的存在，只能和前面的默认结合使用。
                注意: 二进制操作时，不要设置编码格式。
"""
"""
    文件的操作方式：
        读：读取文件时，文件必须存在
            readable(): 获取当前的文件对象是否可读
            
            # read、readline、readlines在读取文件内容时，都会移动文件内容的指针。
            read([n]): read方法默认读取文件的全部内容，但是可以指定读取的长度,返回值类型为字符串。
            readline(): 一行一行的读取文件的内容，返回值为字符串
            readlines(): 读取文件的全部内容，返回值为列表，列表的每个元素，就会文件的每行内容，列表中的元素都为字符串。
        
        写：如果是写的默认，如果文件不存在，就会创建一个新的文件进行写入，如果文件存在就正常进行写入。
            writable(): 获取文件是否可写
            write("字符串")：将字符串写入到文件中.
            writelines(列表)：将列表的元素写入到文件中，列表的每个元素必须为字符串
"""

# 读取-r
"""
res = open("./file/1.txt", mode="r", encoding="utf-8")
print(res, type(res))

# 判断文件对象是否可读
print(res.readable())

# read:读取文件
# print([res.read(4)])

# readline: 一行一行的读取文件的内容，返回值为字符串
# print(res.readline(), end="")
# print(res.readline())

# realines: 返回值为列表
# print(res.readlines())


# print(res.read(2))
# print(res.readline())
# print(res.readlines())

print(res.read())

print("-------------", res.read())
"""

# 写入-w
'''
res = open("./file/2.txt", mode="w", encoding="utf-8")

# writable: 是否可写
print(res.writable())

# write(): 写入字符串
# res.write("hello python")

# writelines: 写入列表
list1 = ["A\n", "b\n", "c\n"]
res.writelines(list1)
'''

# 追加-a-写-写时，在文件内容的最后进行追加
'''
obj = open("./file/1.txt", mode="a", encoding="utf-8")
# 判断读写
print(obj.readable())
print(obj.writable())

obj.write("hello")
obj.writelines(["a", "b"])
'''

# r+/w+/a+
'''
obj = open("./file/1.txt", mode="r+", encoding="utf-8")
print(obj.readable())
print(obj.writable())

print(obj.read(1))
obj.write("成都")
'''
'''
obj = open("./file/1.txt", mode="w+", encoding="utf-8")
print(obj.readable())
print(obj.writable())

# print(obj.read(1))
# obj.write("成都")
res = obj.read()
print(res)
'''
'''
obj = open("./file/1.txt", mode="a+", encoding="utf-8")
print(obj.readable())
print(obj.writable())

# obj.write("\nhello")
res = obj.read()
print(res)
'''

# 读取图片
'''
obj = open("./file/1.txt", mode="rb")
res = obj.read()
obj.close()

print(res)
'''

# 上下文管理器，来进行获取文件对象
"""
    with .... as 变量:
        变量的操作

"""

with open("./file/1.png", mode="rb") as a:
    content = a.read()

with open("./file/3.png", mode="wb") as f1:
    f1.write(content)



# 了解--自己实现上下文管理器类
'''
class MyOpen:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        """对象资源操作时，所做的事情-前置动作"""
        print("----默认调用__enter__----")
        self.obj = open(self.file_path, mode="r", encoding="utf-8")
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        """资源操作完成之后的后置动作"""
        print("----默认调用__exit__----")
        self.obj.close()


with MyOpen("./file/1.txt") as f:
    print(f.read())
    print("xxxxxx")
'''