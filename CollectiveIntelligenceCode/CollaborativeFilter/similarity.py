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
import recommendations
print topMatches(recommendations.critics,'Lisa Rose',n=3)
