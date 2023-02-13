import imageio
import numpy as np

def gif_to_spritesheet(filename):
    # Wczytanie pliku gif jako listy obrazów
    frames = imageio.mimread(filename)

    # Konwersja obrazów na tablicę numpy
    frame_arrays = [np.array(frame) for frame in frames]

    # Połączenie wszystkich klatek w jedną tablicę
    sprite_sheet = np.concatenate(frame_arrays, axis=1)

    # Zapisanie wyniku jako obraz
    imageio.imwrite("spritesheet.png", sprite_sheet)

gifname = str(input("podaj nazwe pliku: "))
# Przykład użycia
gif_to_spritesheet(gifname)
