

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
import recommendations
import recommend_items
import similarity
movies=transformPrefs(recommendations.critics)
print similarity.topMatches(movies,'Lady in the Water')
#以影片推影评人
print recommend_items.getRecommendations(movies,'Just My Luck')
                    



