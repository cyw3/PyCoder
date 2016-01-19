#皮尔逊相关度评价，使用皮尔逊相关系数
#判断两组数据与某一直线拟合程度的一种度量。当数据不是太规范是，会倾向于更好的结果
#该直线，是最佳拟合线。原则是尽可能的靠近图上的所有坐标点

#修正了 夸大分值

#以用户为坐标轴

#具体步骤：
#1、找到两者都评价过的 物品
#2、计算两者的评分总和、平方和，评分乘积之和
#3、计算皮尔逊系数

from math import sqrt

#返回一个-1~1的值
def sim_pearson(prefs,p1,p2):
    si={}
    #两者共同之处
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1

    n=len(si)

    if n==0:return 1

    #评分总和
    sum1=sum([prefs[p1][it]for it in si])
    sum2=sum([prefs[p2][it]for it in si])

    #求平方和
    sum1Sq=sum([pow(prefs[p1][it],2)for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2)for it in si])

    #求对应乘积之和
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    #计算皮尔逊相关系数
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0:return 0

    r=num/den

    return r

#test
import recommendations
#reload(recommendations)
print sim_pearson(recommendations.critics,'Lisa Rose','Gene Seymour')

    
    
