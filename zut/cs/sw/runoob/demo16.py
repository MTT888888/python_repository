import datetime
 # 输出今天的日期
print(datetime.date.today().strftime("%Y-%m-%d"))
# 创建日期对象
Date=datetime.date(2018,5,11)
print(Date.strftime("%d/%m/%Y"))
# 日起算术运算
Day=Date+datetime.timedelta(days=1)
print(Day.strftime("%d-%m-%Y"))
#日期替换
DD=Date.replace(year=Date.year+1)
print(DD.strftime("%Y/%m/%d"))