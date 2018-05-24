# 读取文件操作


path = "../doc/testFIle"
dirPath = "../doc"


def read_file():
    # path = "/mnt/d/study/code/python/my/demo2/doc/testFIle"
    # docFile = open(path, "r")
    # print(docFile.name)
    # print(docFile.read())
    # docFile.close()

    # with 语法 自带close
    with open(path, "r") as docFile:
        print(docFile.name)
        lines = docFile.readlines()
        # print(docFile.read()) // 获取全部内容 不可以共存

    print(lines)


# def writeFile():
#     with open(path, "a") as fi:
#         lines = fi.readlines()
#         for line in lines:
#             fi.write("\n新增加第1行\n新增加第2行\n新增加第3行")

## 追加模式，覆盖模式可用 w
def append_file():
    with open(path, "a") as fi:
        fi.write("\n新增加第1行")


def create_file():
    import os
    # 获取当前程序运行目录
    print(os.getcwd())
    # 获取指定目录下的列表
    print(os.listdir(dirPath + "/../"))

    fileDir = dirPath + "/newFileDir"

    # 检查是否存在文件或文件夹
    print(os.path.exists(fileDir))

    # 创建文件夹，已经存在文件会报错
    # if os.path.exists(fileDir):
    #     pass
    # else:
    os.mkdir(fileDir)

    # 删除文件夹，只能删除文件夹
    if os.path.exists(fileDir + "/myFile"):
        os.remove(fileDir + "/myFile1")

    if (os.path.exists(fileDir + "/myFile1")):
        pass
    else:
        os.mkfifo(fileDir + "/myFile")

    # 文件重命名
    os.rename(fileDir + "/myFile", fileDir + "/myFile1")
