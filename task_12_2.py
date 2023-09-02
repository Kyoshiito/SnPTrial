from dataclasses import dataclass
from task_11_2 import Dessert


@dataclass
class JellyBean(Dessert):
    flavor: str = ""

    def is_delicious(self):
        if self.flavor != 'black licorice':
            return True
        else:
            return False
        

ex = JellyBean('something2', 190, 'black licorice')
ex2 = JellyBean('something3', 350, 'some flavor???')

print(f'name: {ex.name}; calories: {ex.calories}; flavor: {ex.flavor}; is healthy: {ex.is_healthy()}; is delicious: {ex.is_delicious()}')
print(f'name: {ex2.name}; calories:{ex2.calories}; flavor: {ex2.flavor}; is healthy: {ex2.is_healthy()}; is delicious: {ex2.is_delicious()}')
