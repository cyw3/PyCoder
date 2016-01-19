
#推荐物品
#相似度*评价值；求总和;在除以评论过的评论者的相似度之和
from PearsonCorrelationEvaluation import sim_pearson

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
import recommendations
print getRecommendations(recommendations.critics,'Toby')
