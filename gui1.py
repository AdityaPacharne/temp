import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def browse_file():
    print("Browse button clicked!")  # Placeholder function for browsing files

# Create the main window
root = tk.Tk()
root.title("VidTranscribe GUI")
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Set a simple background color (you can replace this with an actual background image)
background_color = "#ececec"
root.configure(bg=background_color)

# Load and resize images for "Select Model" and "Browse" button
select_model_image = Image.open("dropdown.jpg")
select_model_image = select_model_image.resize((200, 50))  # Resize as needed
select_model_photo = ImageTk.PhotoImage(select_model_image)

browse_image = Image.open("browse.jpg")
browse_image = browse_image.resize((100, 50))  # Resize as needed
browse_photo = ImageTk.PhotoImage(browse_image)

# Create a label for "Select Model" using the image
model_label = tk.Label(root, image=select_model_photo, bg=background_color)
model_label.place(relx=0.5, rely=0.5, anchor='center', y=-40)

# Create the dropdown menu (Combobox) and overlay it on top of the label
models = ['tiny.en', 'base.en', 'small.en', 'medium.en', 'large.en']
model_var = tk.StringVar(value=models[0])
model_dropdown = ttk.Combobox(root, textvariable=model_var, values=models, state='readonly')
model_dropdown.place(relx=0.5, rely=0.5, anchor='center', y=-20)

# Create a browse button using the image
browse_button = tk.Button(root, image=browse_photo, command=browse_file, borderwidth=0)
browse_button.place(relx=0.5, rely=0.7, anchor='center')

# Run the application
root.mainloop()

