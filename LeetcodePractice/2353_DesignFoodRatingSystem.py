class FoodRatings:
    list3 = []
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        for i in range(0 , len(foods)):
            self.list3.append([foods[i] , cuisines[i] , ratings[i]])
    def changeRating(self, food: str, newRating: int) -> None:
        for i in self.list3:
            if(i[0]==food):
                i[2] = newRating
                break
    def highestRated(self, cuisine: str) -> str:
        listHigh = []
        tempRating = 0
        for i in self.list3:
            if(i[1]==cuisine):
                if(i[2]>tempRating):
                    tempRating = i[2]
                    listHigh = []
                    listHigh.append(i[0])
                elif(i[2]==tempRating):
                    listHigh.append(i[0])
        listHigh.sort()
        if(listHigh == []):
            val = None
        else:
            val = listHigh[0]
        return val

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)