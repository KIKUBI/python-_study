# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   test62
# FileName:      io_example.py
# Author:       lao_zhao
# Datetime:     2024/8/7 15:24
# Description:
# 
# ---------------------------------------------------------------------------


"""
def generator_data(n):
    for i in range(n+1):
        yield str(i)


def write_data(file_path, gen_obj):
    with open(file_path, mode="wb") as fp:
        for i in gen_obj:
            fp.write((i+"\n").encode())



gen1 = generator_data(10)
write_data("./file/4.txt", gen1)
"""
import time


def get_file_data(file_path, length):
    with open(file_path, mode="rb") as f1:
        n = 1
        while True:
            content = f1.read(length)
            if len(content) == 0:
                break
            print(f"第{n}读取文件的内容")
            n += 1
            yield content


def write_data_file(file_path, data):
    with open(file_path, mode="wb") as f:
        for i in data:
            f.write(i)


start = time.time()
gen1 = get_file_data("./file/data.zip", 2048*100)
write_data_file("./file/data-副本.zip", gen1)
end = time.time()
print(f"复制文件所耗费的时间{int(end) - int(start)}秒")




# print(next(gen1).decode(), end="")
# print(next(gen1).decode(), end="")
# print(next(gen1).decode(), end="")
# print(next(gen1).decode(), end="")
# print(next(gen1).decode(), end="")
# print(next(gen1).decode(), end="")
# print(next(gen1).decode(), end="")
# print(next(gen1).decode(), end="")
# print(next(gen1).decode(), end="")
# print(next(gen1).decode(), end="")
# print(next(gen1).decode(), end="")
# print(next(gen1).decode(), end="")
# print(next(gen1).decode(), end="")

# for i in gen1:
#     print([i])