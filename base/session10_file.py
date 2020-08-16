
# file = open("files/text.txt",mode="r",encoding="utf-8")
# content = file.read()
# print(content)

'''
file - 文件路径
mode - 打开文件的方式，r-只读/w-只写/rw-读写/a-追加/rb-二进制只读
encoding - 打开文件的编码 
'''

# #2-写入
# file = open("files/text_w.txt",mode="a",encoding="utf-8")
# file.writelines(["这个是第一行内容\n","这个是第二行内容"])
# file.close()


# file = open("files/text.txt",mode="r",encoding="utf-8")
# file.seek(3)
# content = file.read()
# print(content)

# import os
# # os.remove("files/text_w.txt")
# os.rename("files/text.txt","files/text_new.txt")

#文件夹
# import os
# os.mkdir("files/sub_folder")

# l = os.listdir("files")
# print(l)

# print(os.getcwd())

# os.rmdir("files")

import shutil
shutil.rmtree("files")

