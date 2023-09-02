class Dessert:
    def __init__(self, name="", calories=0) -> None:
        self.__name = name
        self.__calories = calories

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def calories(self):
        return self.__calories
    
    @calories.setter
    def calories(self, calories):
        self.__calories = calories

    def is_healthy(self):
        if self.__calories < 200:
            return True
        else:
            return False
    
    def is_delicious(self):
        if Dessert:
            return True
    

example = Dessert("something", 150)
print(f'name: {example.name}; calories: {example.calories}; is healthy: {example.is_healthy()}; is delicious: {example.is_delicious()}')