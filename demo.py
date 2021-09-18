from datetime import date, timedelta


def create_one(lst,_date):
    ## 复习间隔，以天数为单位
    times = [0,0,1, 3, 5, 7, 15, 30] 
    for a in times:
        ## 复习的时间点计算
        review_time = _date + timedelta(a) 
        r_t = str(review_time)
        if r_t in DIC.keys():
            DIC[r_t].append(lst)
        else:
            DIC[r_t] = [lst]


DIC = dict()

## 总共需要背的topic
t_sum = 43
## 第一个topic开始日期，后面的topic日期加一
start_date = date(2021, 9, 15)
for i in range(1,t_sum+1):
    ## 每个topic开始计算日期
    _date = start_date + timedelta(i-1)
    ## 每个topic创建遗忘曲线
    create_one('t'+str(i),_date)

## 显示出来
for i in sorted(DIC):
    _str_list = DIC[i]
    new_str = str()
    for j in _str_list:
        new_str += j+' '
    print(i,':',new_str)
