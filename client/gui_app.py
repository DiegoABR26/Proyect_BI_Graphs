from tkinter import ttk, font
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import util.util_imagenes as util_img
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_CURSOR_ENCIMA, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_LATERAL
import util.util_ventana as util_ventana
from .frames import Trabajador,Sedes,Pagos

class Frame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen('./imagenes/logotipo.png', (100, 100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.frames = {}
        for F in (Trabajador, Sedes,Pagos):
            frame = F(self.cuerpo_principal)
            self.frames[F]=frame

        self.controles_menu_lateral()


        
    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Gráficos Tesis Proyect')
        self.iconbitmap("./imagenes/logotipo.ico")
        w, h = 1200, 600
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill=tk.BOTH)

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def controles_barra_superior(self):
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text='BYG RESGUARDO')
        self.labelTitulo.config(fg="#fff", font={'Roboto', 15}, bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome, command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="white")
        self.buttonMenuLateral.pack(side=tk.LEFT)

    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)

        # Etiqueta de perfil lateral
        self.labelPerfil = tk.Label(self.menu_lateral, image=self.logo, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        self.buttonTrabajador = tk.Button(self.menu_lateral, command=self.show_frame(Trabajador))
        self.buttonSede = tk.Button(self.menu_lateral,command=self.show_frame(Sedes))
        self.buttonPagos = tk.Button(self.menu_lateral,command=self.show_frame(Pagos))

        buttons_info = [
            ('Trabajador', '\uf109', self.buttonTrabajador),
            ('Sede', '\uf109', self.buttonSede),
            ('Pagos', '\uf109', self.buttonPagos),
        ]

        for text, icon, button in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f'  {icon}   {text}', anchor="w", font=font_awesome, bd=0, bg=COLOR_MENU_LATERAL,
                      fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg='white')

    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg='white')

    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')
    def show_frame(self, frame_name):
        print("entre")
        frame = self.frames[frame_name]
        print(frame)
        frame.tkraise()