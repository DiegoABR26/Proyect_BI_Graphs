import pandas as pd
import tkinter as tk
import config as cfg
import customtkinter as ctk
from config import *
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
                  frame = ctk.CTkFrame(master=self.frame_top,fg_color="#5F4A87",border_width=1, border_color='#E5BEEC')
                  self.frames_trabajador_top[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT ,fill=tk.BOTH, expand = True)          

            self.frames_trabajador_bottom = {}

            self.frame_bottom =tk.Frame(master=self, bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )

            for F in range(2):#creamos los 4 frames que contiene el frame bottom
                  frame = ctk.CTkFrame(master=self.frame_bottom,fg_color="#5F4A87",border_width=1, border_color='#E5BEEC')
                  self.frames_trabajador_bottom[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT, fill=tk.BOTH, expand = True)

            self.frame_bottom_circular = tk.Frame(master=self.frames_trabajador_bottom[0])
            self.frame_bottom_circular.pack(padx=5,pady=5,fill=tk.BOTH,expand=True)

            
            list = db_connection.ejecutar_usp_Trabajadores_cancelados('042024')
            
            pagado = 0
            pendiente = 0
            no_pagado = 0
            for e in list: 
                 # print(e[4])
                  if e[4] =="PAGADO":
                        pagado += 1
                  elif e[4] =="PENDIENTE":
                        pendiente += 1
                  elif e[4] =="NO PAGADO":
                        no_pagado +=1
                  
            labels=["Pagado","No Pagado","Pendiente"]
            data = [pagado, no_pagado, pendiente]
            Graficos.create_grafico_circular(self.frame_bottom_circular, labels, data,"Trabajadores Pagados por Periodo")

            self.frame_bottom_table = tk.Frame(master=self.frames_trabajador_bottom[1])
            self.frame_bottom_table.pack(padx=5,pady=5,fill=tk.BOTH,expand=True)

            table_columns = ["NUMERO","DNI", "NOMBRE", "MONTO", "Estado"]

            table_data = db_connection.ejecutar_usp_Trabajadores_cancelados('042024')

            Graficos.create_grafico_table(self.frame_bottom_table,table_columns,table_data)

class Pagos(tk.Frame):
      
      def __init__(self, parent, controller):
            super().__init__(parent)
            self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
            self.option_selected = tk.StringVar()
            self.cuerpo_principal()
            self.init_widgets_Pagos()


      def cuerpo_principal(self):
            self.cuerpo_principal_top=ctk.CTkFrame(master=self, fg_color="white")
            self.cuerpo_principal_top.pack(padx=5,pady=5, anchor = "w" ,side=tk.TOP)
            valores=["casa","frijol","tuvieaja"],
            self.option_selected.set("casadefrijo")
            #realizar la creación de un input tipo 
            ctk.CTkOptionMenu(self.cuerpo_principal_top,self.option_selected,*valores,
                                    fg_color="#F5E89D",
                                    text_color="black",
                                    button_color="#F5E88C",
                                    button_hover_color="#F5E874",
                                    height=30
                                    ).grid(
                                              row=0,
                                              column=0,
                                              padx=5,
                                              pady=5
                                              )
            self.data_cancelados = db_connection.ejecutar_usp_Trabajadores_cancelados('042024')
            dframeCancelados = pd.DataFrame(self.data_cancelados)
            
            self.frame_dialog = ctk.CTkFrame(master=self.cuerpo_principal_top, fg_color="#F5D971",border_width=1,border_color="white")
            self.frame_dialog.grid(row=0,column=1,padx=5,pady=5)

            ctk.CTkLabel(master=self.frame_dialog,
                              text="MONTO TOTAL DE PAGOS: ${}".format(dframeCancelados[3].sum()),
                              text_color="black", width=10, height=30
                        ).grid(
                              row=0,
                              column=0,
                              padx=5,
                              pady=5
                              )

      def init_widgets_Pagos(self):
            #realizar la creación de una variable

            self.frame_top = tk.Frame(master=self, bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
            
            self.frames_pagos_top = {}#array de los frames del top

            for F in range(1): #creamos los 2 frames que contiene el frame top
                  frame = ctk.CTkFrame(master=self.frame_top, fg_color="#FFFFFF")
                  self.frames_pagos_top[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.TOP ,fill=tk.BOTH, expand = True)

            self.frame_top_barras = ctk.CTkFrame(master=self.frames_pagos_top[0],fg_color="white")
            self.frame_top_barras.pack(padx=3,pady=3,side=tk.TOP, fill=tk.BOTH, expand= True)
            
            labels = ['012024', '022024', '032024', '042024', '052024']
            montos = [23455, 23434, 23353, 35454, 345456]
            Graficos.create_grafico_line(self.frame_top_barras,montos, labels, "periodos","montos","Grafico De Lineas")

##SECCIÓN INFERIOR
            self.frames_pagos_bottom = {}#array de los frames del bottom

            self.frame_bottom =tk.Frame(master=self,bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )

            for F in range(2):#creamos los 2 frames que contiene el frame bottom
                  frame = ctk.CTkFrame(master=self.frame_bottom,fg_color="white",border_width=1, border_color='#E5BEEC')
                  self.frames_pagos_bottom[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT, fill=tk.BOTH, expand = True)

            self.frame_table = tk.Frame(master= self.frames_pagos_bottom[0])
            self.frame_table.pack(padx=3,pady=3,side=tk.TOP, fill=tk.BOTH, expand= True)

            table_columns = ["NUMERO","DNI", "NOMBRE", "MONTO", "Estado"]
            table_data = self.data_cancelados
            Graficos.create_grafico_table(self.frame_table,table_columns,table_data)

            self.frame_bottom_circular = tk.Frame(master=self.frames_pagos_bottom[1], background="white")
            self.frame_bottom_circular.pack(padx=3,pady=3,side=tk.RIGHT, fill=tk.BOTH, expand= True)
                                                        
            pagado = 0
            pendiente = 0
            no_pagado = 0
            for e in self.data_cancelados: 
                 # print(e[4])
                  if e[4] =="PAGADO":
                        pagado += 1
                  elif e[4] =="PENDIENTE":
                        pendiente += 1
                  elif e[4] =="NO PAGADO":
                        no_pagado +=1
                  
            labels=["Pagado","No Pagado","Pendiente"]
            data = [pagado, no_pagado, pendiente]

            Graficos.create_grafico_circular(self.frame_bottom_circular, labels, data,"Trabajadores Pagados por Periodo","Estados")


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
     

  
    