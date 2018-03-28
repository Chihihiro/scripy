from WindPy import w as wind
import pandas as pd

wind.start()    # 启动wind


def crawl_benchmark(id):    # 定义方法
    tmp = wind.wsd(id, "close,lastradeday_s", "2017-05-10", "2017-06-08", "Days=Alldays") # 万得API用法
    df = pd.DataFrame(tmp.Data)   # 用结果(list)去构造一个DataFrame二维表
    # statistic_date = 1
    df = df.T   # 把表转置
    df.columns = [tmp.Fields[0], "statistic_date"]  # 给表添加列标题
    return df   # 返回结果

q = crawl_benchmark("512500.SH")    # 调用方法，并且把返回结果存放到变量q中
q.drop_duplicates(["statistic_date", "CLOSE"])  #   去重

q.to_excel("c:/Users/Yu/Desktop/test.xlsx") #导出到excel


# hs = wind.wsd("000300.SH", "close,lastradeday_s", "2017-05-10", "2017-06-08", "Days=Alldays")
#
#
# result = [hs.Data, cbi.Data[0]]
#
#
# a = [[1, 3, 5], [2, 4, 6]]
# b = [1, 3, 5]
#
# df = pd.DataFrame(result).T
# df.columns = ["hs300", "cbi"]



