import tkinter as tk
import time
from PIL import ImageTk, Image

from logic import *


def missionaries_on_left(state):
    return state.ml


def cannibals_on_left(state):
    return state.cl


def is_boat_on_left(state):
    return state.sl


def missionaries_on_right(state):
    return state.mr


def cannibals_on_right(state):
    return state.cr


def main():
    solver = Solver()
    solver.solve()
    solution_states = solver.solution

    # Initialize the root window
    root = tk.Tk()
    root.title("Missionaries and Cannibals")
    root.geometry("1000x600")

    # Define image sizes for missionaries and cannibals
    missionary_image_size = (50, 50)
    cannibal_image_size = (50, 50)
    ship_image_size = (90, 50)

    original_image1 = Image.open("Priest.jpg")
    priest_resized_image = original_image1.resize(missionary_image_size)
    original_image2 = Image.open("R.jpeg")
    cannibal_resized_image = original_image2.resize(cannibal_image_size)
    original_image3 = Image.open("sailing-ship-25.jpg")
    ship_resized_image = original_image3.resize(ship_image_size)

    # Load and resize images
    missionary_image = ImageTk.PhotoImage(priest_resized_image)
    cannibal_image = ImageTk.PhotoImage(cannibal_resized_image)
    ship_image = ImageTk.PhotoImage(ship_resized_image)

    # Create frames for displaying sides of the river
    left_frame = tk.Frame(root)
    right_frame = tk.Frame(root)

    # Place frames side-by-side
    left_frame.pack(side="left")
    right_frame.pack(side="right")

    # Labels for displaying river and boat
    river_label = tk.Label(root,
                           text="-----------------------------------RIVER-------------------------------------------",
                           font=("Arial", 20))
    boat_label = tk.Label(root, image=ship_image, width=ship_image_size[0], height=ship_image_size[1])

    # Function to update the GUI with game state
    def update_gui(state):
        # Clear existing images
        for widget in left_frame.winfo_children():
            widget.destroy()
        for widget in right_frame.winfo_children():
            widget.destroy()

        # Display missionaries and cannibals on appropriate sides
        for i in range(missionaries_on_left(state)):
            tk.Label(left_frame, image=missionary_image, width=missionary_image_size[0],
                     height=missionary_image_size[1]).pack()
        for i in range(cannibals_on_left(state)):
            tk.Label(left_frame, image=cannibal_image, width=cannibal_image_size[0],
                     height=cannibal_image_size[1]).pack()
        for i in range(missionaries_on_right(state)):
            tk.Label(right_frame, image=missionary_image, width=missionary_image_size[0],
                     height=missionary_image_size[1]).pack()
        for i in range(cannibals_on_right(state)):
            tk.Label(right_frame, image=cannibal_image, width=cannibal_image_size[0],
                     height=missionary_image_size[1]).pack()

        # Update boat position
        boat_label.pack(side="left" if is_boat_on_left(state) else "right")
        river_label.pack(side="left")

        # Loop through solution states and update GUI

    for state in solution_states:
        update_gui(state)
        time.sleep(3)
        root.update()

        # Display the solution and prevent window closure
    tk.Label(root, text="Solution complete!", font=("Arial", 15)).pack()
    root.mainloop()


if __name__ == "__main__":
    main()
