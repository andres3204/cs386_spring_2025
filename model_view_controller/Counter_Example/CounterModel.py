# CounterModel.py

# Model
class CounterModel:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1
          
    def decrement(self):
        self.count -= 1
        
    def get_value(self):
        return self.count
    
if __name__ == "__main__":  
    wins = CounterModel()
    wins.increment
    print("wins = ", wins.get_value())
