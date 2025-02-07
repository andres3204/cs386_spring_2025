# counter_mvc.py
# spring 2025
# prof. lehman
#
# simulates a simple up/down counter
# demonstrates MVC (model, view, controller) pattern
#
# views (x2) - GUI view, ASCII view
# controller (x1)
# model (x1)
#
#
import tkinter as tk

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


# GUI View
class CounterView():

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        
        # GUI interface
        self.main = tk.Tk()
        self.main.title("MVC Demo - Counter")
        self.main.geometry("300x100")
        self.main.label = tk.Label(self.main, text="0", font=("Arial", 20))
        self.main.label.pack()
        self.main.button = tk.Button(self.main, text="Increment", command=self.handle_increment)
        self.main.button.pack(side="left",padx=40)
        self.main.button = tk.Button(self.main, text="Decrement", command=self.handle_decrement)
        self.main.button.pack(side="left")
        
    def run(self):
        self.mainloop() #wait for clicks
    
    # process input
    def handle_increment(self):
        self.controller.increment()
    
    def handle_decrement(self):
        self.controller.decrement()

    # update data from model
    def update(self, value):
        self.main.label.config(text=str(value))


# ASCII View
class CounterView_ASCII():

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        
    # update data from model
    def update(self, value):
        print(f"Counter: {value}")
        
    # handle input
    def run(self):
        while True:
            action = input("Enter action (+ add, - sub, q quit): ")
            
            if action == "q":
                break # I know crazy to see Prof. Lehman using a break :-)
            elif action == "+":
                self.controller.increment()                    
            elif action == "-":
                self.controller.decrement()        
            else:
                print("Error: invalid action")


# Controller
class CounterController:
    def __init__(self):
        self.model = CounterModel()
        
        # pick One of the View's
        self.view = CounterView(self)
        #self.view = CounterView_ASCII(self)
    
    def increment(self):
        self.model.increment()
        self.view.update(self.model.get_value())

    def decrement(self):
        self.model.decrement()
        self.view.update(self.model.get_value())
        
    def run(self):
        self.view.run()
        
# Run the application
if __name__ == "__main__":
    test1 = CounterController()
    test1.run()
