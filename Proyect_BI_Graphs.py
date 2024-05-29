import tkinter as tk
from client.gui_app import Frame 

def main ():
    root = tk.Tk()

    root.title('Proyect_BI')
    ##root.iconbitmap('img/Nombre de archivo .ico')

    root.resizable(0,0)

    app = Frame(root = root)

    app.mainloop() ##final de la ejecución de nuestra aplicación
    

    pass
if __name__ == '__main__':
    main()