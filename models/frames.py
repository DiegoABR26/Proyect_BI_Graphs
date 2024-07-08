import pandas as pd
import tkinter as tk
import config as cfg
import customtkinter as ctk
from config import *
from datalayer import services,db_connection
from .graphs import Graficos
from datetime import date, datetime


class Trabajador(tk.Frame):
      def __init__(self, parent, controller):
            super().__init__(parent)
            self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
            self.init_widgets_trabajador()
            self.line_chart_canvas = None
            self.line_chart_ax = None
            self.circular_chart_canvas = None
            self.circular_chart_ax = None
            self.table = None
      
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

            self.circular_chart_canvas, self.circular_chart_ax = Graficos.create_grafico_circular(
                  self.frame_bottom_circular, labels, data, "Trabajadores Pagados por Periodo", "Estados")


            self.frame_bottom_table = tk.Frame(master=self.frames_trabajador_bottom[1])
            self.frame_bottom_table.pack(padx=5,pady=5,fill=tk.BOTH,expand=True)

            table_columns = ["NUMERO","DNI", "NOMBRE", "MONTO", "Estado"]
            table_data = db_connection.ejecutar_usp_Trabajadores_cancelados('042024')
            self.table = Graficos.create_grafico_table(self.frame_bottom_table, table_columns, table_data)

class Pagos(tk.Frame):
      
      def __init__(self, parent, controller):
            super().__init__(parent)
            self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
            self.periodos = []
            self.option_selected = tk.StringVar()
            self.option_selected.trace_add('write', self.update_chart)  # Detectar cambios en la opción seleccionada
            self.asignar_variables_general()
            self.cuerpo_principal()
            self.init_widgets_Pagos()
            self.line_chart_canvas = None
            self.line_chart_ax = None
            self.circular_chart_canvas = None
            self.circular_chart_ax = None
            self.table = None

      def asignar_variables_general(self):
            month = date.today().month#  Tenemos que colocar que extraiga la fecha de hoy
            year = date.today().year#  Tenemos que colocar que extraiga la fecha de hoy
            periodo='0{}{}'.format(month,year)
            if len(str(month)) == 2:
                  periodo='{}{}'.format(month,year)
            else:
                  periodo='0{}{}'.format(month,year)
            global dframeCancelados_actual
            global dframeCancelados_periodo
            global data_cancelados

            data_cancelados = db_connection.ejecutar_usp_Trabajadores_cancelados(periodo)
            dframeCancelados_actual = pd.DataFrame(
                              data = db_connection.ejecutar_usp_Trabajadores_cancelados(periodo),
                              columns=["NUMERO","DNI","NOMBRE","MONTO","ESTADO"])
            dframeCancelados_periodo = pd.DataFrame(
                              data=dframeCancelados_actual,
                              columns=["NUMERO","DNI","NOMBRE","MONTO","ESTADO"])
            dframeCancelados_periodo["PERIODO"] = periodo
            
            self.periodos.append(periodo)
            j = 1
            while month > 0 and j < 7:
                  i = 1
                  month -= i

                  if len(str(month)) == 2:
                        periodo='{}{}'.format(month,year)
                  else:
                        periodo='0{}{}'.format(month,year)

                  data_cancelados_periodo = db_connection.ejecutar_usp_Trabajadores_cancelados(periodo)#cambiar valor hard
                  data_cancelados_periodo = pd.DataFrame(
                        data=db_connection.ejecutar_usp_Trabajadores_cancelados(periodo),
                        columns=["NUMERO","DNI","NOMBRE","MONTO","ESTADO"]
                        )
                  data_cancelados_periodo["PERIODO"] = periodo
                  dframeCancelados_periodo = pd.concat([dframeCancelados_periodo, data_cancelados_periodo],ignore_index=True)
                  self.periodos.append(periodo)
                  if month == 0:
                        year -= 1
                        month = 12
                  j += 1
      def cuerpo_principal(self):
            self.cuerpo_principal_top=ctk.CTkFrame(master=self, fg_color="white")
            self.cuerpo_principal_top.pack(padx=5,pady=5, anchor = "w" ,side=tk.TOP)
            #realizar la creación de un input tipo 
            self.option_menu = ctk.CTkOptionMenu(self.cuerpo_principal_top,
                                                 values = self.periodos,
                                                 fg_color="#F5E89D",
                                                 text_color="black",
                                                 button_color="#F5E88C",
                                                 button_hover_color="#F5E874",
                                                 variable = self.option_selected  #Asociar la variable
                                                 )
            self.option_menu.grid(row=0,column=0,padx=5,pady=5)
            self.option_selected.set(self.periodos[0])
            
            #Creamos el Label que contiene el valor máximo
            self.frame_dialog = ctk.CTkFrame(master=self.cuerpo_principal_top, fg_color="#F5D971",border_width=1,border_color="white")
            self.frame_dialog.grid(row=0,column=1,padx=5,pady=5)


            ctk.CTkLabel(master=self.frame_dialog,
                              text="MONTO TOTAL DE PAGOS: ${}".format(dframeCancelados_actual["MONTO"].sum()),
                              text_color="black", width=10, height=30
                        ).grid(row=0,column=0,padx=5,pady=5)

      def init_widgets_Pagos(self):
            #Creamos el FRAME PADRE_TOP
            self.frames_pagos_top = {}#array de los frames del top
            self.frame_top = tk.Frame(master=self, bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
            
            for F in range(1): #creamos 1 frame que contiene el frame top(modificamos el número de recuadros requeridos)
                  frame = ctk.CTkFrame(master=self.frame_top, fg_color="#FFFFFF")
                  self.frames_pagos_top[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.TOP ,fill=tk.BOTH, expand = True)

            #Creamos el Frame que almacenará nuestro gráfico de barras
            self.frame_top_barras = ctk.CTkFrame(master=self.frames_pagos_top[0],fg_color="white")
            self.frame_top_barras.pack(padx=3,pady=3,side=tk.TOP, fill=tk.BOTH, expand= True)

            labels = self.periodos
            montos_max = []

            for periodo in self.periodos:
                  filter_period = dframeCancelados_periodo["PERIODO"] == periodo
                  period_filtered = dframeCancelados_periodo[filter_period]
                  result = period_filtered["MONTO"].sum()
                  montos_max.append(result)

            self.line_chart_canvas, self.line_chart_ax = Graficos.create_grafico_line(
                        self.frame_top_barras, montos_max, labels, "", "MONTOS", "Grafico De Lineas")
            
            ##SECCIÓN INFERIOR

            #Creamos el FRAME PADRE_BOTTOM
            self.frames_pagos_bottom = {}#array de los frames del bottom
            self.frame_bottom =tk.Frame(master=self,bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )

            for F in range(2):#creamos los 2 frames que contiene el frame bottom
                  frame = ctk.CTkFrame(master=self.frame_bottom,fg_color="white",border_width=1, border_color='#E5BEEC')
                  self.frames_pagos_bottom[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT, fill=tk.BOTH, expand = True)

            #Creamos el frame que contendrá nuestra tabla
            self.frame_table = tk.Frame(master= self.frames_pagos_bottom[0])
            self.frame_table.pack(padx=3,pady=3,side=tk.TOP, fill=tk.BOTH, expand= True)

            table_columns = ["NUMERO","DNI", "NOMBRE", "MONTO", "Estado"]
            table_data = data_cancelados
            self.table = Graficos.create_grafico_table(self.frame_table, table_columns, table_data)

            self.frame_bottom_circular = tk.Frame(master=self.frames_pagos_bottom[1], background="white")
            self.frame_bottom_circular.pack(padx=3,pady=3,side=tk.RIGHT, fill=tk.BOTH, expand= True)
                                                                
            labels=["Pagado","No Pagado","Pendiente"]

            self.circular_chart_canvas, self.circular_chart_ax = Graficos.create_grafico_circular(
                  self.frame_bottom_circular, labels, dframeCancelados_actual["ESTADO"].value_counts(), "Trabajadores Pagados por Periodo", "Estados")

      def update_chart(self, *args):
            selected_period = self.option_selected.get()
            
            data_cancelados = db_connection.ejecutar_usp_Trabajadores_cancelados(selected_period)
            dframeCancelados = pd.DataFrame(data_cancelados)


            for widget in self.frame_dialog.winfo_children():
                  widget.destroy()

            ctk.CTkLabel(self.frame_dialog,
                              text="MONTO TOTAL DE PAGOS: S/.{}".format(dframeCancelados[3].sum()),
                              text_color="black", width=10, height=30
                        ).grid(row=0,column=0,padx=5,pady=5)
            #Grafico Circular

            labels = ["Pagado", "No Pagado", "Pendiente"]

            for widget in self.frame_bottom_circular.winfo_children():
                  widget.destroy()
            
            self.circular_chart_canvas, self.circular_chart_ax = Graficos.create_grafico_circular(
                  self.frame_bottom_circular, labels, dframeCancelados[4].value_counts(), "Trabajadores Pagados por Periodo", "Estados")
            
            #Tabla
            #Creamos el frame que contendrá nuestra tabla
            for widget in self.frame_table.winfo_children():
                  widget.destroy()

            table_columns = ["NUMERO","DNI", "NOMBRE", "MONTO", "Estado"]
            table_data = data_cancelados
            self.table = Graficos.create_grafico_table(self.frame_table, table_columns, table_data)

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
     

  
    