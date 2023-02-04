import tkinter as tk
import random

def draw_movies(movies, n):
    drawn = random.sample(movies, n)
    return drawn

def add_movie():
    movie = entry.get()
    movies.append(movie)
    entry.delete(0, tk.END)
    listbox.insert(tk.END, movie)

def draw():
    results = draw_movies(movies, int(spin.get()))
    results_label["text"] = "Results: " + ", ".join(results)

root = tk.Tk()
root.geometry("300x300")
root.configure(bg="grey")
root.title("Movie Drawer")

frame = tk.Frame(root, bg="grey")
frame.pack(padx=10, pady=10)

movies = []

entry = tk.Entry(frame, bg="grey", fg="white")
entry.grid(row=0, column=0)

add_button = tk.Button(frame, text="Add", command=add_movie, bg="grey", fg="white")
add_button.grid(row=0, column=1)

listbox = tk.Listbox(frame, bg="grey", fg="white")
listbox.grid(row=1, column=0, columnspan=2)

spin = tk.Spinbox(frame, from_=1, to=100, bg="grey", fg="white")
spin.grid(row=2, column=0)

draw_button = tk.Button(frame, text="Draw", command=draw, bg="grey", fg="white")
draw_button.grid(row=2, column=1)

results_label = tk.Label(frame, text="", bg="grey", fg="white")
results_label.grid(row=3, column=0, columnspan=2)

root.mainloop()
