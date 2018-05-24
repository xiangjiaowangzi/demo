import pandas as pd

# DataFrame
df = pd.read_csv("/home/xjr99721/桌面/person.csv")
# print(df)
assert isinstance(df, pd.DataFrame)


def fun1():
    df1 = df.head(1)
    print(df1)

    print(type(df))

    print(df.columns)

    print(df.index)

    print(df.loc[1])

    print(df[df.性别 == 1])


# fun1()

def fun2():
    # 排序
    df1 = df.sort_values(['姓名', '性别']).head()
    print(df1)
    # 访问
    print(df1.loc[2])
    # 索引
    scores = {
        "英语": [20, 40],
        '体育': [30, 30],
        '姓名': ["流弊", "方法"]
    }
    df2 = pd.DataFrame(scores, index=["one", "two"])
    print(df2)
    print(df2.loc["one"])
    # 实实在在的索引第几个
    print(df2.iloc[1])
    # df2.ix[0]
    print(df2.values)

    def func(sorce):
        if sorce > 30:
            return "优秀"
        else:
            return "傻逼"

    df2["评价"] = df2.英语.map(func)
    print(df2)
    df2.drop(['评价'], axis=1)
    print(df2)
    print(df2.applymap(lambda x: str(x) + "-"))


# fun2()


def fun3():
    # MATPLOTLIB绘图
    import numpy as np
    import matplotlib.pyplot as plt
    # matplotlib.iniline
    x = np.linspace(0, 10, 500)
    y = np.sin(x)

    plt.subplot(2, 2, 1)
    (plt.plot(x, y, 'o', color="yellow",label="sin(x)"))
    plt.plot(x, np.cos(x),label="con(x)")
    plt.subplot(2, 1, 2)
    plt.plot(x, np.cos(x), '--')
    (plt.plot(x, y))
    plt.legend
    plt.show()


fun3()
