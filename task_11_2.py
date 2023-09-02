from dataclasses import dataclass, field


@dataclass
class Dessert:
    name: str = ""
    calories: int = 0
    
    def is_healthy(self):
        if self.calories <= 200:
            return True
        else:
            return False
        
    def is_delicious(self):
        if Dessert:
            return True
        

example = Dessert("something", 150)
#example2 = Dessert('somersby', 450)
print(f'name: {example.name}; calories: {example.calories}; is healthy: {example.is_healthy()}; is delicious: {example.is_delicious()}')
#print(f'name: {example2.name}; calories: {example2.calories}; is healthy: {example2.is_healthy()}; is delicious: {example2.is_delicious()}')