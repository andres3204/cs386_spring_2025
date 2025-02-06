import tkinter as tk

# Model
class CounterModel:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def get_value(self):
        return self.value

# View
class CounterView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        
        self.title("Model View Controller")
        self.geometry("300x100")
        self.label = tk.Label(self, text="0", font=("Arial", 20))
        self.label.pack()
        self.button = tk.Button(self, text="Increment", command=self.controller.increment)
        self.button.pack()

    def update(self, value):
        self.label.config(text=str(value))

# Controller
class CounterController:
    def __init__(self):
        self.model = CounterModel()
        self.view = CounterView(self)
    
    def increment(self):
        self.model.increment()
        self.view.update(self.model.get_value())

    def run(self):
        self.view.mainloop()

# Run the application
if __name__ == "__main__":
    CounterController().run()
