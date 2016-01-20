#可用来在构造数据集


#有时会报错 ，连接不到这个网站
#返回xml格式的数据
#import pydelicious
#pydelicious.get_popular(tag='programming')

from pydelicious import get_popular,get_userposts,get_urlposts
import time

"""
将得到一个包含若干个用户数据的字典
"""
def initializeUserDict(tag,count=5):
    user_dict={}
    #获取前count个最受欢迎的链接张贴记录
    for p1 in get_popular(tag=tag)[0:count]:
        #查找所有张贴该链接的用户
        for p2 in get_urlposts(p1['href']):
            user=p2['user']
            user_dict[user]={}
    return user_dict


"""
填充用户评价值
"""
def fillItems(user_dict):
    all_items={}
    #查找所有用户都提交过的链接
    for user in user_dict:
        for i in range(3):
            try:
                posts=get_userposts(user)
                break
            except:
                print "Failed user "+user+", retrying"
                time.sleep(4)
        for post in posts:
            url=post['href']
            user_dict[user][url]=1.0
            all_items[url]=1

    #用0填充缺失的项
    for ratings in user_dict.values():
        for item in all_items:
            if item not in ratings:
                ratings[item]=0.0



#test
rom deliciousrec import *
delusers=initializeUserDict('programming')
#这是添加自己的账号
delusers['tsegaran']={}
fillItems(delusers)








                
