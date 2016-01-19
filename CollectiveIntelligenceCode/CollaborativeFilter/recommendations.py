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

print critics['Lisa Rose']['Lady in the Water']

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
print sim_distance(critics,'Lisa Rose','Gene Seymour')
    
