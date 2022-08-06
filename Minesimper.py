from tkinter import *
import settings
import utils

root = Tk()

# Override the settings of the window
root.configure(bg="lightblue") # Sets background color
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')   # Sets window size
root.title("Mine-simper") # Sets title
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red', # Change later
    width=settings.WIDTH,
    height=utils.height_prct(25) 
)

top_frame.place(x=0, y=-0)

left_frame = Frame(
    root,
    bg='white', # Change later
    width=utils.width_prct(25),
    height=utils.height_prct(75) 
)

left_frame.place(x=0, y=utils.height_prct(25))


center_frame = Frame (
    root,
    bg='lightblue',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))


# Run the window
root.mainloop()