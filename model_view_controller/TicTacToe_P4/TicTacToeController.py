
from TicTacToeView import TicTacToeView
from TicTacToeView_Canvas import TicTacToeView_Canvas
from TicTacToeView_ASCII import TicTacToeView_ASCII
from TicTacToeModel import TicTacToeModel

# TicTacToeController.py
# spring 2025
# prof. lehman
# CS382 Visual Programming P4
# demonstrates MVC architecture
# model, view, controller

# *** do not change this file, other than selecting one of three views

class TicTacToeController:
    def __init__(self):
        
        self.model = TicTacToeModel()
        
        # pick ONE of the following Views
        # self.view = TicTacToeView_ASCII(self) # pass reference to self
        # self.view = TicTacToeView(self) # pass reference to self
        self.view = TicTacToeView_Canvas(self) # pass reference to self
        

    # tell model to process selection
    def handle_selection(self, row, col):
        
        if self.model.is_game_over() == False:
            
            # pass row, col to model
            self.model.play_xo(self.model.get_turn(), row, col)
            
            # return value from model and tell view to update
            self.view.update_board( row, col, self.model.get_board_value(row, col) )
            
            # update view status (called after each selction and for reset)
            self.update_status()
             
    # use model game logic for updating view status
    def update_status(self):
        
        if self.model.is_game_over() == True:
            winner = self.model.get_winner()
            if winner == "N":
                msg = "Cat Wins!"
            else:
                msg = f"{winner} Wins!"
        else:
            turn = self.model.get_turn().upper()
            msg = f"Player {turn}'s turn"    
             
        # tell view to update status
        self.view.update_status( msg )
        
    # reset game
    def reset_game(self):
        # tell model to reset
        self.model.reset_game()
        
        # update status (also called after each selection)
        self.update_status()
        
        # tell view to update board 
        for r in range(0,3):
            for c in range(0,3):
                self.view.update_board( r, c, self.model.get_board_value(r, c) )
                
    # tell view to run and start getting selections
    def run(self):
        self.view.run()
        
        