import util.util_imagenes as util_img
import tkinter as tk
import config as cfg
import customtkinter
import pandas as pd
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
            self.init_widgets_Pagos()      

      def init_widgets_Pagos(self):
            data_cancelados = db_connection.ejecutar_usp_Trabajadores_cancelados('042024')

            #dframeCancelados = pd.DataFrame(data_cancelados)
            #suma = dframeCancelados[3].sum
            #print(suma)
            self.frame_top =tk.Frame(master=self, bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
            
            self.frames_pagos_top = {}#array de los frames del top

            for F in range(2): #creamos los 2 frames que contiene el frame top
                  frame = customtkinter.CTkFrame(master=self.frame_top, fg_color="#FFFFFF")
                  self.frames_pagos_top[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT ,fill=tk.BOTH, expand = True)

            
            self.frame_top_bar = customtkinter.CTkFrame(master=self.frames_pagos_top[0],fg_color="white")
            self.frame_top_bar.pack(padx=3,pady=3,side=tk.TOP, fill=tk.BOTH, expand= True)
            
            labels = ['012024', '022024', '032024', '042024', '052024']
            montos = [1000, 1500, 2000, 2500, 3000]
            Graficos.create_grafico_barras(self.frame_top_bar,montos, labels, "periodos","montos","grafico de barra")



            self.frame_top_left_option=customtkinter.CTkFrame(master=self.frames_pagos_top[1], fg_color="white")
            self.frame_top_left_option.pack(padx=5,pady=5,side=tk.TOP, fill = tk.BOTH)
            customtkinter.CTkOptionMenu(master=self.frame_top_left_option, 
                                        values=["casa","frijol","tuvieaja"],
                                        fg_color="#F5E89D",
                                        text_color="black",
                                        button_color="#F5E88C",
                                        button_hover_color="#F5E874"
                                        ).grid(
                                              row=0,
                                              column=0,
                                              padx=5,
                                              pady=5
                                              )


            self.frame_top_left_dialog = customtkinter.CTkFrame(master=self.frames_pagos_top[1], fg_color="#F5D971",border_width=1,border_color="white")
            self.frame_top_left_dialog.pack(padx=5,pady=5,side=tk.BOTTOM, fill = tk.BOTH)
            customtkinter.CTkLabel(master=self.frame_top_left_dialog,text="Monto Total de Pagos: $200",
                                    text_color="black"
                                    ).grid(
                                          row=1,
                                          column=0,
                                          padx=5,
                                          pady=5
                                          )

            self.frame_bottom =tk.Frame(master=self,bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )

            self.frames_pagos_bottom = {}#array de los frames del bottom

            for F in range(2):#creamos los 2 frames que contiene el frame bottom
                  frame = customtkinter.CTkFrame(master=self.frame_bottom,fg_color="white",border_width=1, border_color='#E5BEEC')
                  self.frames_pagos_bottom[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT, fill=tk.BOTH, expand = True)

            self.frame_table = tk.Frame(master= self.frames_pagos_bottom[0])
            self.frame_table.pack(padx=3,pady=3,side=tk.TOP, fill=tk.BOTH, expand= True)

            table_columns = ["NUMERO","DNI", "NOMBRE", "MONTO", "Estado"]

            table_data = data_cancelados

            Graficos.create_grafico_table(self.frame_table,table_columns,table_data)

            self.frame_bottom_circular = tk.Frame(master=self.frames_pagos_bottom[1], background="white")
            self.frame_bottom_circular.pack(padx=3,pady=3,side=tk.TOP, fill=tk.BOTH, expand= True)
                                            
            photo = util_img.leer_imagen_ctk('./imagenes/save.png', (30, 30))
            
            buttonGraphGenerator = customtkinter.CTkButton(self.frame_bottom_circular, fg_color="#9b2330", text="Visualizar", font=("Helvetica", 10), width=2, image=photo,
                                                           command=lambda: Graficos.create_grafico_circular(self.frame_bottom_circular, 
                                                                                                            labels, 
                                                                                                            data,
                                                                                                            "Trabajadores Pagados por Periodo","Estados",2))
            buttonGraphGenerator.pack(side=tk.LEFT, anchor="s")

            pagado = 0
            pendiente = 0
            no_pagado = 0
            for e in data_cancelados: 
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
     

  
    