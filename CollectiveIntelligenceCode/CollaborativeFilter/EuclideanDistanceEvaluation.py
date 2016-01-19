
#欧几里得距离评价
#以经过人们一致评价的物品为坐标轴，将参与的【评价的人绘制图中，考察彼此间的距离远近
#偏好空间，求欧几里得距离

#0-1
from math import sqrt
import recommendations

def sim_distance(prefs, person1, person2):
    #得到shared_items列表
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    #如果两者没有共同之处，则返回0
    if len(si)==0:
        return 0

    #计算所有差值的平方和,for特殊的用法
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1] if item in prefs[person2]])

    return 1/(1+sqrt(sum_of_squares))


#测试
#reload(recommendations)
print sim_distance(recommendations.critics,'Lisa Rose','Gene Seymour')
