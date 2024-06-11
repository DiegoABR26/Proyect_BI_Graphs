import tkinter as tk
import config as cfg
import customtkinter
from config import *
from config import COLOR_CUERPO_PRINCIPAL
from datalayer import services,db_connection
from .graphs import Graficos


class Trabajador(tk.Frame):
      def __init__(self, parent, controller):
            super().__init__(parent)
            self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
            self.init_widgets_trabajador()

      def init_widgets_trabajador(self):
            self.frames_trabajador_top = {}

            self.frame_top =tk.Frame(master=self, bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

            for F in range(3): #creamos los 4 frames que contiene el frame top
                  frame = customtkinter.CTkFrame(master=self.frame_top,fg_color="#5F4A87",border_width=1, border_color='#E5BEEC')
                  self.frames_trabajador_top[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT ,fill=tk.BOTH, expand = True)          

            self.frames_trabajador_bottom = {}

            self.frame_bottom =tk.Frame(master=self, bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )

            for F in range(2):#creamos los 4 frames que contiene el frame bottom
                  frame = customtkinter.CTkFrame(master=self.frame_bottom,fg_color="#5F4A87",border_width=1, border_color='#E5BEEC')
                  self.frames_trabajador_bottom[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT, fill=tk.BOTH, expand = True)

            self.frame_bottom_circular = tk.Frame(master=self.frames_trabajador_bottom[0])
            self.frame_bottom_circular.pack(padx=5,pady=5,fill=tk.BOTH,expand=True)

            
            list = db_connection.ejecutar_usp_Trabajadores_cancelados('042024')

            for e in list:
                  pagado = 0
                  pendiente = 0
                  no_pagado = 0
                  if e[4] =="PAGADO":
                        pagado += 1
                  elif e[4] =="PENDIENTE":
                        pendiente += 1
                  elif e[4] =="NO PAGADO":
                        no_pagado +=1
                  
            labels=["Pagado","No Pagado","Pendiente"]
            data = [pagado, no_pagado, pendiente]
            Graficos.create_grafico_circular(self.frame_bottom_circular, labels, data)

            self.frame_bottom_table = tk.Frame(master=self.frames_trabajador_bottom[1])
            self.frame_bottom_table.pack(padx=5,pady=5,fill=tk.BOTH,expand=True)

            table_columns = ["NUMERO","DNI", "NOMBRE", "MONTO", "Estado"]

            table_data = db_connection.ejecutar_usp_Trabajadores_cancelados('042024')

            Graficos.create_grafico_table(self.frame_bottom_table,table_columns,table_data)

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

            for F in range(2):#creamos los 4 frames que contiene el frame bottom
                  frame = customtkinter.CTkFrame(master=self.frame_bottom,fg_color="#5F4A87",border_width=1, border_color='#E5BEEC')
                  self.frames_pagos_bottom[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT, fill=tk.BOTH, expand = True)

            self.frame_table = tk.Frame(master= self.frames_pagos_bottom[0])
            self.frame_table.pack(padx=3,pady=3,side=tk.TOP, fill=tk.BOTH, expand= True)

            table_columns = ["Id", "Hora inicio", "Hora Final", "Cantidad Hrs Trabajadas", "Actividad"] 

            table_data = services.consulta_horario()

            Graficos.create_grafico_table(self.frame_table,table_columns,table_data)

            self.frame_line = tk.Frame(master=self.frames_pagos_bottom[1])
            self.frame_line.pack(padx=3,pady=3,side=tk.TOP, fill=tk.BOTH, expand= True)

            Graficos.create_grafico_barras(self.frame_line)
            


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
     

  
    