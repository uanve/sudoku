import tkinter as tk
from tkinter.filedialog import asksaveasfile as save_as
from random import randint
from PIL import Image, ImageTk
from initial_solution import *

num_size = 70
GAME_SPEED = 1



class Sudoku(tk.Canvas):
    def __init__(self):
        super().__init__(
            width=9*num_size, height=11*num_size, background="white", highlightthickness=0
        )

        self.grid = [[0 for i in range(9)] for i in range(9)]
        self.create_grid()
        self.create_game()
        
        self.position = (0,0)

        self.bind("<Button-1>", self.click)
        self.bind_all("<Key>", self.key_press)
        self.bind('<Button-3>', self.delete_cell)
        self.hint_state = (False,1) #False: hints disable; #1
        self.current_trial = (0,0)

        self.pack()

        # self.after(GAME_SPEED, self.backtracking)

    def create_grid(self):
        self.create_rectangle(0, 0, 9*num_size, 9*num_size, outline="#525d69")
        # horizontal lines
        self.create_line(0,1*num_size,9*num_size,1*num_size,dash=(4, 2))
        self.create_line(0,2*num_size,9*num_size,2*num_size,dash=(4, 2))
        self.create_line(0,3*num_size,9*num_size,3*num_size)
        self.create_line(0,4*num_size,9*num_size,4*num_size,dash=(4, 2))
        self.create_line(0,5*num_size,9*num_size,5*num_size,dash=(4, 2))
        self.create_line(0,6*num_size,9*num_size,6*num_size)
        self.create_line(0,7*num_size,9*num_size,7*num_size,dash=(4, 2))
        self.create_line(0,8*num_size,9*num_size,8*num_size,dash=(4, 2))
        

        # vertical lines
        self.create_line(1*num_size,0,1*num_size,9*num_size,dash=(4, 2))
        self.create_line(2*num_size,0,2*num_size,9*num_size,dash=(4, 2))
        self.create_line(3*num_size,0,3*num_size,9*num_size)
        self.create_line(4*num_size,0,4*num_size,9*num_size,dash=(4, 2))
        self.create_line(5*num_size,0,5*num_size,9*num_size,dash=(4, 2))
        self.create_line(6*num_size,0,6*num_size,9*num_size)
        self.create_line(7*num_size,0,7*num_size,9*num_size,dash=(4, 2))
        self.create_line(8*num_size,0,8*num_size,9*num_size,dash=(4, 2))

    def create_game(self):
        grid = self.grid
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    self.create_text((i+0.5)*num_size,(j+0.5)*num_size,text=str(grid[i][j]))
        

       
        
        self.button = tk.Button(text='save', command=self.file_save,height=1)
        self.button.place(x=7.15*num_size,y=9.5*num_size)
     


    def file_save(self):
    
        f = save_as(mode='w', defaultextension=".txt")
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        
        for j in range(9):
            for i in range(9):
                if i<8:
                    f.write(str(self.grid[i][j])+'\t')
                else:
                    f.write(str(self.grid[i][j]))
            if j<8:
                f.write('\n')

        f.close()
        root.destroy()
            

            
    def click(self,event):

        click_coordenates = (event.x//num_size, event.y//num_size)
        if click_coordenates[1]<9:
            self.delete('click_rectangle')
            
            self.position = click_coordenates
            X,Y = self.position
            x,y = X*num_size, Y*num_size

            self.create_rectangle(x+5,y+5,x+num_size-5,y+num_size-5,outline='red',tag='click_rectangle')
        
            

                
    def move_square(self,move):
        self.delete('click_rectangle')
        X,Y = self.position
        if move=='Down':
            Y+=1
        elif move=='Up':
            Y-=1
        elif move=='Right':
            if X < 8:
                X+=1
            else:
                X = 0
                Y+=1
        elif move=='Left':
            if X > 0:
                X-=1
            else:
                X = 8
                Y-=1
        self.position = (X,Y)
        x,y = X*num_size, Y*num_size
        self.create_rectangle(x+5,y+5,x+num_size-5,y+num_size-5,outline='red',tag='click_rectangle')


    def key_press(self,event):
        if event.keysym in ['Up','Down','Right','Left']:
            self.move_square(event.keysym)
        
        else:
            numb = int(event.char)
        
            X,Y = self.position
            self.create_text((X+0.5)*num_size,(Y+0.5)*num_size,text=numb, fill='gray',tag='{}_{}'.format(X,Y)) 
            self.grid[X][Y] = numb
            print("({},{}) added: correct =".format(X,Y),is_correct(self.grid))
        


    def delete_cell(self,event):
        X,Y = self.position
               
        self.delete('{}_{}'.format(X,Y))
        self.grid[X][Y] = 0
        



        
root = tk.Tk()
root.title("Sudoku")
root.resizable(False, False)
root.tk.call("tk", "scaling", 4.0)

board = Sudoku()

root.mainloop()