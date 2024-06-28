from PIL import ImageTk, Image
import customtkinter as ctk
def leer_imagen_tk (path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))

def leer_imagen_ctk (path, size):
    return ctk.CTkImage(Image.open(path), size=(20, 20))
