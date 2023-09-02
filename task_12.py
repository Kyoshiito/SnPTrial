import task_11

class JellyBean(task_11.Dessert):
    def __init__(self, name="", calories=0, flavor="") -> None:
        super().__init__(name, calories)
        self.__flavor = flavor

    @property
    def flavor(self):
        return self.__flavor
    
    @flavor.setter
    def flavor(self, flavor):
        self.__flavor = flavor

    def is_delicious(self):
        if self.__flavor != 'black licorice':
            return super().is_delicious()
        else: 
            return False


ex = JellyBean('something2', 190, 'black licorice')
ex2 = JellyBean('something3', 350, 'some flavor???')

print(f'name: {ex.name}; calories: {ex.calories}; flavor: {ex.flavor}; is healthy: {ex.is_healthy()}; is delicious: {ex.is_delicious()}')
print(f'name: {ex2.name}; calories:{ex2.calories}; flavor: {ex2.flavor}; is healthy: {ex2.is_healthy()}; is delicious: {ex2.is_delicious()}')
