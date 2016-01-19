critics={
'Lisa Rose':{'Lady in the Water':2.5,'Snakes on a Plane':3.5,'Just My Luck':3.0,'Superman Returns':3.5,'You, Me and Dupree':2.5,'The Night Listener':3.0},
'Gene Seymour':{'Lady in the Water':3.0,'Snakes on a Plane':3.5,'Just My Luck':1.5,'Superman Returns':5.0,'The Night Listener':3.0,'You, Me and Dupree':3.5},
'Michael Phillips':{'Lady in the Water':2.5,'Snakes on a Plane':3.0,'Superman Returns':3.5,'The Night Listener':4.0},
'Claudia Puig':{'Snakes on a Plane':3.5,'Just My Luck':3.0,'The Night Listener':4.5,'Superman Returns':4.0,'You, Me and Dupree':2.5},
'Mick LaSalle':{'Lady in the Water':3.0,'Snakes on a Plane':4.0,'Just My Luck':2.0,'Superman Returns':3.0,'The Night Listener':3.0,'You,Me and Dupree':2.0},
'Jack Matthews':{'Lady in the Water':3.0,'Snakes on a Plane':4.0,'The Night Listener':3.0,'Superman Returns':5.0,'You,Me and Dupree':3.5},
'Toby':{'Snakes on a Plane':4.5,'You ,Me and Dupree':1.0,'Superman Returns':4.0}
}

#from recommendations import critics

#print critics['Lisa Rose']['Lady in the Water']

#####################################################]


#欧几里得距离评价
#以经过人们一致评价的物品为坐标轴，将参与的【评价的人绘制图中，考察彼此间的距离远近
#偏好空间，求欧几里得距离

#0-1
from math import sqrt

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
#recommendations.
#print sim_distance(critics,'Lisa Rose','Gene Seymour')



#皮尔逊相关度评价
#使用皮尔逊相关系数
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
#import recommendations
#reload(recommendations)
#print sim_pearson(recommendations.critics,'Lisa Rose','Gene Seymour')


#以指定的人员，给其他人员打分，选出相似的人员

#从反映偏好的字典中返回最佳匹配者
#返回结果的个数和相似度函数均为可选参数
from PearsonCorrelationEvaluation import sim_pearson

def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other)for other in prefs
            if other!=person]

    #对列表进行排序，评价值最高者排在最前面
    scores.sort()
    scores.reverse()
    return scores[0:n]


#test
#import recommendations
#reload(recommendations)
print topMatches(critics,'Lisa Rose',n=3)



#推荐物品
#相似度*评价值；求总和;在除以评论过的评论者的相似度之和
#from PearsonCorrelationEvaluation import sim_pearson

#利用所有其他人的评价值的加权平均，为某人提供建议
def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        #不和自己进行比较
        if other==person:continue
        sim=similarity(prefs,person,other)

        #忽略评价值为零或小于零的情况
        if sim<=0:continue
        for item in prefs[other]:
            #只对自己还没有看过的影片进行评价
            if item not in prefs[person] or prefs[person][item]==0:
                #相似度*评价值
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim

                #相似度之和.因为不是所有人对所有物品进行评分，所以是基于item的
                simSums.setdefault(item,0)
                simSums[item]+=sim

    #建立归一化列表,字典
    rankings=[(total/simSums[item],item)for item ,total in totals.items()]

    #返回排序列表
    rankings.sort()
    rankings.reverse()
    return rankings

#test
#import recommendations
#reload(recommendations)
print getRecommendations(critics,'Toby')



#匹配物件
def transformPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item,{})

            #
            result[item][person]=prefs[person][item]
    return result

#test
#import recommendations
#import recommend_items
#import similarity
#reload(recommendations)
movies=transformPrefs(critics)
print topMatches(movies,'Lady in the Water')
#以影片推影评人
print getRecommendations(movies,'Just My Luck')
                    









    
