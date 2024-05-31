from tkinter import ttk, font
from client.db_connection import obtener_datos
from util import util_ventana as util_ventana
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import util.util_imagenes as util_img
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_CURSOR_ENCIMA,COLOR_CUERPO_PRINCIPAL,COLOR_MENU_LATERAL

class Frame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen('./imagenes/logotipo.png',(100,100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()

    def config_window(self):
        #Configuración inicial de la ventana
        self.title('Gráficos Tesis Proyect')
        self.iconbitmap("./imagenes/logotipo.ico")
        w,h = 1200,600
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        self.barra_superior = tk.Frame(
            self, bg = COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(sid=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame(self, bg = COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both',expand=False)
        
        self.cuerpo_principal = tk.Frame(self, bg = COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both',expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)
        
        #Etiqueta de titulo
        self.labelTitulo = tk.Label(self.barra_superior, text='BYG RESGUARDO')
        self.labelTitulo.config(fg = "#fff",font={'Roboto',15},bg=COLOR_BARRA_SUPERIOR,pady=10,width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        #botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font = font_awesome,command= self.toggle_panel,bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)
    
    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        #Etiqueta de perfil lateral
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.logo,bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP,pady=10)

        self.buttonTrabajador = tk.Button(self.menu_lateral)
        self.buttonSede = tk.Button(self.menu_lateral)
        self.buttonPagos = tk.Button(self.menu_lateral)
        buttons_info = [
            ('Trabajador','\uf109',self.buttonTrabajador),
            ('Sede','\uf109',self.buttonSede),
            ('Pagos','\uf109',self.buttonPagos),
        ]

        for text, icon, button in buttons_info:
           self.configurar_boton_menu(button, text, icon, font_awesome,ancho_menu,alto_menu)

    def configurar_boton_menu(self,button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text = f'  {icon}   {text}',anchor="w", font=font_awesome,bd=0,bg=COLOR_MENU_LATERAL,
                      fg = "white",width = ancho_menu, height = alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)
    
    def bind_hover_events(self, button):
        #Asociar eventos ENter y Leave con la función dinámica
        button.bind("<Enter>", lambda event : self.on_enter(event,button))
        button.bind("<Leave>", lambda event : self.on_leave(event,button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')
        
    #def barra_menu(root):
        
    #barra_menu = tk.Menu(root)
    #root.config(menu = barra_menu,width = 300, height = 300)

    #menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    #barra_menu.add_cascade( label = 'Inicio', menu = menu_inicio)
    #barra_menu.add_cascade( label = 'Salir', command = root.destroy)





    