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
    def __init__(self, presenter):
        super().__init__()
        self.presenter = presenter
        self.label = tk.Label(self, text="0", font=("Arial", 20))
        self.label.pack()
        self.button = tk.Button(self, text="Increment", command=self.presenter.increment)
        self.button.pack()

    def update_display(self, value):
        self.label.config(text=str(value))

# Presenter
class CounterPresenter:
    def __init__(self):
        self.model = CounterModel()
        self.view = CounterView(self)

    def increment(self):
        self.model.increment()
        self.view.update_display(self.model.get_value())

    def run(self):
        self.view.mainloop()

# Run the application
if __name__ == "__main__":
    CounterPresenter().run()
