import tkinter as tk
import config as cfg
import customtkinter
from config import *
from config import COLOR_CUERPO_PRINCIPAL
from datalayer import services
from .graphs import Graficos

class Trabajador(tk.Frame):
      def __init__(self, parent, controller):
            super().__init__(parent)
            self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
            self.init_widgets_trabajador()

      def init_widgets_trabajador(self):
            self.frame_top =tk.Frame(master=self)
            self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

            self.frames_trabajador_top = {}

            for F in range(4):
                  frame = tk.Frame(master=self.frame_top,bg="#5F4A87")
                  self.frames_trabajador_top[F] = frame
                  frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
                  tk.Label(frame,text="Aquí estoy f{}".format(F), bg="#5F4A87").pack(side=tk.TOP)
            
            self.frame1_top = tk.Frame(self.frames_trabajador_top[0], bg="#5F4A87")
            self.frame1_top.pack(side=tk.BOTTOM, fill=tk.BOTH, expand= True)

            self.frames_trabajador_bottom = {}

            self.frame_bottom =tk.Frame(master=self)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )


            for F in range(4):
                  frame = tk.Frame(master=self.frame_bottom,bg="#5F4A87")
                  self.frames_trabajador_bottom[F] = frame
                  frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
                  tk.Label(frame,text="Aquí estoy f{}".format(F), bg="blue").pack(side=tk.TOP)
            
            self.frame1_bottom = tk.Frame(self.frames_trabajador_bottom[0], bg="black")
            self.frame1_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand= True)
            
class Pagos(tk.Frame):
        def __init__(self, parent, controller):
              super().__init__(parent)
              self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
              self.init_widgets_Pagos()

        def init_widgets_Pagos(self):
            self.frame_top =tk.Frame(master=self, bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
            
            self.frames_pagos_top = {}#array de los frames del top

            for F in range(3): #creamos los 4 frames que contiene el frame top
                  frame = customtkinter.CTkFrame(master=self.frame_top,fg_color="#5F4A87",border_width=1, border_color='#E5BEEC')
                  self.frames_pagos_top[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT ,fill=tk.BOTH, expand = True)

           

            self.frame_bottom =tk.Frame(master=self,bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )

            self.frames_pagos_bottom = {}#array de los frames del bottom

            for F in range(3):#creamos los 4 frames que contiene el frame bottom
                  frame = customtkinter.CTkFrame(master=self.frame_bottom,fg_color="#5F4A87",border_width=1, border_color='#E5BEEC')
                  self.frames_pagos_bottom[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT, fill=tk.BOTH, expand = True)

            self.frame_table = tk.Frame(master= self.frames_pagos_bottom[0])
            self.frame_table.pack(side=tk.BOTTOM, fill=tk.BOTH, expand= True)

            table_columns = ["Id", "Hora inicio", "Hora Final", "Cantidad Hrs Trabajadas", "Actividad"] 

            table_data = services.consulta_horario()

            Graficos.create_grafico_table(self.frame_table,table_columns,table_data)
            


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
     

  
    