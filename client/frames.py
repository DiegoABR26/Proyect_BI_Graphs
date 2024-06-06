import tkinter as tk
import config as cfg 
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_CURSOR_ENCIMA, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_LATERAL
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Trabajador(tk.Frame):
    def __init__(self, parent, controller):
          super().__init__(parent)
          self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
          self.init_widgets_trabajador()


    def init_widgets_trabajador(self):
        self.frame_top =tk.Frame(master=self)
        self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

        self.frame_top_inf = tk.Frame(master=self.frame_top,bg="blue")
        self.frame_top_inf.pack(side=tk.LEFT, fill=tk.BOTH, expand = True)

        self.frame_bottom =tk.Frame(master=self)
        self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )

        self.frame1 = tk.Frame(master=self.frame_bottom,bg="red")
        self.frame1.pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)

        tk.Label(self.frame1, text="Gráficos 1").pack(side=tk.TOP)
        self.frame_trabajador1 = tk.Frame(self.frame1, bg="blue")
        self.frame_trabajador1.pack(side=tk.TOP)
        create_line_chart(self.frame_trabajador1)

        self.frame2 = tk.Frame(master=self.frame_bottom,bg="black")
        self.frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
          
        tk.Label(self.frame2, text="Gráficos 2").pack(side=tk.TOP)
        self.frame_trabajador2 = tk.Frame(self.frame2, bg="blue")
        self.frame_trabajador2.pack(side=tk.TOP)
        create_line_chart(self.frame_trabajador2)

        self.frame3 = tk.Frame(master=self.frame_bottom, bg="red")
        self.frame3.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)        

        tk.Label(self.frame3, text="Gráficos 3").pack(side=tk.TOP)
        self.frame_trabajador3 = tk.Frame(self.frame3, bg="white")
        self.frame_trabajador3.pack(side=tk.TOP)
        create_line_chart(self.frame_trabajador3)



class Pagos(tk.Frame):
        def __init__(self, parent, controller):
              super().__init__(parent)
              self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
              self.init_widgets_Pagos()

        def init_widgets_Pagos(self):
            self.frame_top =tk.Frame(master=self)
            self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

            self.frame_bottom_detail = tk.Frame(master=self.frame_top,background="red")
            self.frame_bottom_detail.pack(side=tk.LEFT, fill=tk.BOTH, expand = True)

            self.frame_bottom =tk.Frame(master=self)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )

            self.frame_boframe_bottom_detailttom_inf = tk.Frame(master=self.frame_bottom,background="blue")
            self.frame_bottom_detail.pack(side=tk.RIGHT, fill=tk.BOTH, expand = True) 

class Sedes(tk.Frame):
        def __init__(self, parent, controller):
              super().__init__(parent)
              self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
              self.init_widgets_sedes()

        def init_widgets_sedes(self):  
            self.frame_top =tk.Frame(master=self)
            self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

            self.frame_top_inf = tk.Frame(master=self.frame_top,background="green")
            self.frame_top_inf.pack(side=tk.LEFT, fill=tk.BOTH, expand = True)

            self.frame_bottom =tk.Frame(master=self)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )

            self.frame_bottom_inf = tk.Frame(master=self.frame_bottom,background="yellow")
            self.frame_bottom_inf.pack(side=tk.RIGHT, fill=tk.BOTH, expand = True) 

              



def create_line_chart(frame):
      # Datos de ejemplo - reemplaza esto con la consulta a la base de datos
      periodos = ['012024', '022024', '032024', '042024', '052024']
      montos = [1000, 1500, 2000, 2500, 3000]

      # Crear la figura de matplotlib
      fig = Figure(figsize=(2, 2), dpi=111)
      ax = fig.add_subplot(111)
      ax.plot(periodos, montos)

      ax.set_xlabel('PERIODO', fontsize=1)
      ax.set_ylabel('MONTO',fontsize=1)
      ax.set_title('Monto por Periodo',fontsize=10)

      # Crear el canvas de tkinter para la figura de matplotlib
      canvas = FigureCanvasTkAgg(fig, master=frame)
      canvas.draw()
      canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
  
    