
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
data = pd.read_csv("top50.csv")
def danceabilitygrph(data):
    plt.figure(figsize=(17, 6))
    plt.bar([*(range(1, 51))], np.array(data.Danceability), color="green")
    plt.xticks([*range(1, 51)])
    plt.yticks([*range(0, 91, 5)])
    plt.xlabel("Track Number")
    plt.ylabel("Danceability")
    plt.title("Danceability Values of 50 songs")
    plt.show()
def genres_energy_levels(data):
    genre_energy = np.array(data.groupby(["Genre"])["Energy"].sum())
    genre_values = np.array(data.groupby(["Genre"])["Genre"].size())
    genre_energy_avarege = []
    genre_types = []
    i = 0
    for typ in np.array(data.Genre):
        if typ not in genre_types:
            genre_types.append(typ)
    genre_types = np.array(sorted(genre_types))
    while i < len(genre_values):
        genre_energy_avarege.append(round(genre_energy[i] / genre_values[i], 2))
        i += 1
    plt.figure(figsize=(17, 6))
    plt.bar(genre_types, genre_energy_avarege, color="blue")
    plt.xticks(fontsize=7, rotation=25 )
    plt.yticks([*range(0, 91,5)])
    plt.xlabel("Genders", labelpad=-7)
    plt.ylabel("Avarage of Energy")
    plt.title("Avarage Energy Levels of Genres")
    plt.show()
window = tk.Tk()
window.title("KOU AI PYTHON - MUSTAFA AY")
window.geometry("750x150")
button2 = tk.Button(text=" Avarage Energy Levels of Genres ", width=35, height=4,
                    command=lambda: genres_energy_levels(data))
button2.place(relx=0.50, rely=0.25)
button1 = tk.Button(text="Danceability Values of 50 songs  ", width=35, height=4,
                    command=lambda: danceabilitygrph(data))
button1.place(relx=0.1, rely=0.25)
window.mainloop()




