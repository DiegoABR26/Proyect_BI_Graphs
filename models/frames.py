import pandas as pd
import tkinter as tk
import config as cfg
import customtkinter as ctk
from config import *
from datalayer import services,db_connection
from .graphs import Graficos
from datetime import date, datetime
from util import CustomOptionMenu

class Trabajador(tk.Frame):
      def __init__(self, parent, controller):
            super().__init__(parent)
            self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
            self.dfdatos_trabajadores = pd.DataFrame(
                        data = db_connection.ejecutar_sp("usp_ListaTrabajadores"),
                        columns=["ID", "DNI","NOMBRE","HORARIO","CONTRATO","FECHA_INICIO","ESTADO","FECHA_FIN","SEDE","CORREO","NUMERO"])
            self.init_widgets_trabajador()
      
      def init_widgets_trabajador(self):
            #Inicializamos los Frames Top
            self.frames_trabajador_top = {}

            self.frame_top =tk.Frame(master=self, bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

            for F in range(3): #creamos los 4 frames que contiene el frame top
                  frame = ctk.CTkFrame(master=self.frame_top,fg_color="#2C3F59",border_width=3, border_color='white')
                  self.frames_trabajador_top[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT ,fill=tk.BOTH, expand = True)          

##SECCIÓN INFERIOR
            #Inicializamos los Frames bottom
            self.frames_trabajador_bottom = {}

            self.frame_bottom =tk.Frame(master=self, bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )

            for F in range(3):#creamos los 4 frames que contiene el frame bottom
                  frame = ctk.CTkFrame(master=self.frame_bottom,fg_color="#2C3F59",border_width=3, border_color='white')
                  self.frames_trabajador_bottom[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT, fill=tk.BOTH, expand = True)

            self.frame_bottom_circular = tk.Frame(master=self.frames_trabajador_bottom[0])
            self.frame_bottom_circular.pack(padx=5,pady=5,fill=tk.BOTH,expand=True)            
            #self.circular_chart_canvas, self.circular_chart_ax = Graficos.create_grafico_circular(
            #      self.frame_bottom_circular, labels, data, "Trabajadores Pagados por Periodo", "Estados")


            self.frame_bottom_table = tk.Frame(master=self.frames_trabajador_bottom[1])
            self.frame_bottom_table.pack(padx=5,pady=5,fill=tk.BOTH,expand=True)

            #table_columns = ["NUMERO","DNI", "NOMBRE", "MONTO", "Estado"]
            #table_data = db_connection.ejecutar_usp_Trabajadores_cancelados('042024')
            #self.table = Graficos.create_grafico_table(self.frame_bottom_table, table_columns, table_data)

class Pagos(tk.Frame):
      
      def __init__(self, parent, controller):
            super().__init__(parent)
            self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
            self.periodos = []
            self.option_selected = tk.StringVar()
            self.option_selected.trace("w", self.update_chart)  # Detectar cambios en la opción seleccionada
            self.period_mapping = {}
            self.asignar_variables_general()
            self.cuerpo_principal()
            self.init_widgets_Pagos()

      def asignar_variables_general(self):
            month = date.today().month#  Tenemos que colocar que extraiga la fecha de hoy
            year = date.today().year#  Tenemos que colocar que extraiga la fecha de hoy
            current_period = f'{month:02}{year}'

            global dframeCancelados_actual
            global dframeCancelados_periodo
            global data_cancelados

            data_cancelados = db_connection.ejecutar_sp_con_params("usp_Trabajadores_cancelados","@ID_PERIODO=?",current_period)
            dframeCancelados_actual = pd.DataFrame(
                              data = data_cancelados,
                              columns=["DNI","NOMBRE","MONTO","ESTADO"])
            dframeCancelados_periodo = dframeCancelados_actual.copy()
            dframeCancelados_periodo["PERIODO"] = current_period
            
            self.periodos.append(current_period)
            self.period_mapping[current_period] = self.format_period(current_period)

            for _ in range(6):
                  month -= 1
                  if month == 0:
                        year -= 1
                        month = 12
                  periodo = f'{month:02}{year}'
                  data_cancelados_periodo = db_connection.ejecutar_sp_con_params("usp_Trabajadores_cancelados","@ID_PERIODO=?",periodo)#cambiar valor hard
                  data_cancelados_periodo = pd.DataFrame(
                        data=data_cancelados_periodo,
                        columns=["DNI","NOMBRE","MONTO","ESTADO"]
                        )
                  data_cancelados_periodo["PERIODO"] = periodo
                  dframeCancelados_periodo = pd.concat([dframeCancelados_periodo, data_cancelados_periodo],ignore_index=True)
                  self.periodos.append(periodo)
                  self.period_mapping[periodo] = self.format_period(periodo)

      def format_period(self, period):
            month = int(period[:2])
            year = period[2:]
            return datetime(year=int(year), month=month, day=1).strftime('%b-%Y')

            
      def cuerpo_principal(self):
            self.cuerpo_principal_top=ctk.CTkFrame(master=self, fg_color="#2C3F59")
            self.cuerpo_principal_top.pack(padx=5,pady=5, anchor = "w" ,side=tk.TOP)

            #realizar la creación de un input tipo 
            self.option_menu = ctk.CTkOptionMenu(self.cuerpo_principal_top,
                                                 values = [self.period_mapping[period] for period in self.periodos],
                                                 fg_color="#F5E89D",
                                                 text_color="black",
                                                 button_color="#F5E88C",
                                                 button_hover_color="#F5E874",
                                                 variable = self.option_selected  #Asociar la variable
                                                 ,width=20, height=40
                                                 )
            self.option_menu.grid(row=0,column=0,padx=5,pady=5)
            self.option_selected.set(self.periodos[0])
            
            #Creamos el Label que contiene el valor máximo
            self.frame_dialog = ctk.CTkFrame(master=self.cuerpo_principal_top, fg_color="#F2AF5C")
            self.frame_dialog.grid(row=0,column=1,padx=5,pady=5)

            ctk.CTkLabel(master=self.frame_dialog,
                              text="MONTO TOTAL DE PAGOS REALIZADO EN EL PERIODO ACTUAL: S/ {}".format(dframeCancelados_actual["MONTO"].sum()),
                              text_color="black", width=10, height=30
                        ).grid(row=0,column=0,padx=5,pady=5)

      def init_widgets_Pagos(self):
            #Creamos el FRAME PADRE_TOP
            self.frames_pagos_top = {}#array de los frames del top
            self.frame_top = tk.Frame(master=self, bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)
            
            for F in range(1): #creamos 1 frame que contiene el frame top(modificamos el número de recuadros requeridos)
                  frame = ctk.CTkFrame(master=self.frame_top, fg_color="#2C3F59")
                  self.frames_pagos_top[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.TOP ,fill=tk.BOTH, expand = True)

            #Creamos el Frame que almacenará nuestro gráfico de barras
            self.frame_top_barras = ctk.CTkFrame(master=self.frames_pagos_top[0],fg_color="#2C3F59")
            self.frame_top_barras.pack(padx=3,pady=3,side=tk.TOP, fill=tk.BOTH, expand= True)

            labels = [self.period_mapping[period] for period in self.periodos]
            montos_max = []

            for periodo in self.periodos:
                  filter_period = dframeCancelados_periodo["PERIODO"] == periodo
                  period_filtered = dframeCancelados_periodo[filter_period]
                  result = period_filtered["MONTO"].sum()
                  montos_max.append(result)

            self.fig_line, self.ax_line, self.canvas_line = Graficos.create_grafico_line(
                        self.frame_top_barras, montos_max, labels, "", "MONTOS", "GRÁFICO DE LINEAS")
            
            ##SECCIÓN INFERIOR

            #Creamos el FRAME PADRE_BOTTOM
            self.frames_pagos_bottom = {}#array de los frames del bottom
            self.frame_bottom =tk.Frame(master=self,bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )

            for F in range(2):#creamos los 2 frames que contiene el frame bottom
                  frame = ctk.CTkFrame(master=self.frame_bottom,fg_color="#2C3F59",border_width=3, border_color='black')
                  self.frames_pagos_bottom[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT, fill=tk.BOTH, expand = True)

            #Creamos el frame que contendrá nuestra tabla
            self.frame_table = tk.Frame(master= self.frames_pagos_bottom[0])
            self.frame_table.pack(padx=3,pady=3,side=tk.TOP, fill=tk.BOTH, expand= True)

            table_columns = ["DNI", "NOMBRE", "MONTO", "Estado"]
            table_data = data_cancelados
            self.table = Graficos.create_grafico_table(self.frame_table, table_columns, table_data)

            #Creamos el frame que contendrá nuestra pie chart
            self.frame_bottom_circular = tk.Frame(master=self.frames_pagos_bottom[1], background="white")
            self.frame_bottom_circular.pack(padx=3,pady=3,side=tk.RIGHT, fill=tk.BOTH, expand= True)
                                                                
            labels=["No Pagado","Pagado","Pendiente"]
            self.fig_pie, self.ax_pie, self.wedges, self.autotexts, self.canvas_pie = Graficos.create_grafico_circular(
                  self.frame_bottom_circular, labels, dframeCancelados_actual["ESTADO"].value_counts(), "Trabajadores Pagados por Periodo", "Estados")

      def update_chart(self, *args):

            selected_period = None
            
            for period, formatted_period in self.period_mapping.items():
                  if formatted_period == self.option_selected.get():
                        selected_period = period
                        break
            if not selected_period:
                  return
            
            data_cancelados = db_connection.ejecutar_sp_con_params("usp_Trabajadores_cancelados","@ID_PERIODO=?",selected_period)
            dframeCancelados = pd.DataFrame(data_cancelados)

            for widget in self.frame_dialog.winfo_children():
                  widget.destroy()
                  
            ctk.CTkLabel(self.frame_dialog,
                              text="MONTO TOTAL DE PAGOS REALIZADO EN EL PERIODO ACTUAL: S/ {}".format(dframeCancelados[2].sum()),
                              text_color="black", width=10, height=30
                        ).grid(row=0,column=0,padx=5,pady=5)
            
            #Grafico Circular

            labels = ["No Pagado", "Pagado",  "Pendiente"]

            Graficos.update_grafico_circular(self.ax_pie, 
                                             self.wedges, 
                                             self.autotexts, 
                                             self.canvas_pie, 
                                             labels, 
                                             dframeCancelados[3].value_counts(),
                                             "Trabajadores Pagados por Periodo",
                                             "Estados")
            
            #Creamos el frame que contendrá nuestra tabla
            Graficos.update_grafico_table(self.table, data_cancelados)

class Sedes(tk.Frame):
      def __init__(self, parent, controller):
            super().__init__(parent)
            self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
            self.id_sede = []
            self.nombre_sedes_mapping={}
            self.option_selected = tk.StringVar()
            self.dfdatos_trabajadores = pd.DataFrame(
                        data = db_connection.ejecutar_sp("usp_ListaTrabajadores"),
                        columns=["ID", "DNI","NOMBRE","HORARIO","CONTRATO","FECHA_INICIO","ESTADO","FECHA_FIN","SEDE","CORREO","NUMERO"])
            self.cuerpo_principal()
            self.init_widgets_sedes()
            self.option_selected.trace("w", self.update_chart)
      
      def cuerpo_principal(self):
            self.cuerpo_principal_top=ctk.CTkFrame(master=self, fg_color="#2C3F59")
            self.cuerpo_principal_top.pack(padx=5,pady=5, anchor = "w" ,side=ctk.TOP)

            self.sedes = pd.DataFrame(data=db_connection.ejecutar_sp("usp_ListarSedes"),
                                      columns=["ID_SEDES","NOMBRE_SEDE","ACTIVO"])

            self.id_sede = self.sedes["ID_SEDES"].values.tolist()
            self.nombre_sede = self.sedes["NOMBRE_SEDE"].values.tolist()

            for id_sede in self.id_sede:
                  self.nombre_sedes_mapping[id_sede] = self.nombre_sede[id_sede-1]

            #realizar la creación de un input tipo 
            self.option_menu = CustomOptionMenu.CustomOptionMenu(self.cuerpo_principal_top,
                                                 values = [self.nombre_sedes_mapping[sede] for sede in self.id_sede],
                                                 fg_color="#F5E89D",
                                                 dynamic_resizing=False,
                                                 text_color = "black",
                                                 button_color = "#F5E88C",
                                                 button_hover_color = "#F5E874",
                                                 dropdown_fg_color = "#F5E89D",
                                                 dropdown_hover_color = "#3E4A59",
                                                 dropdown_text_color = "black",
                                                 dropdown_font = ("Arial", 12),
                                                 dropdown_height = 10,  # Límite de altura del desplegable
                                                 variable = self.option_selected,#Asociar la variable
                                                 width=200, height=40
                                                 )
            self.option_menu.grid(row=0,column=0,padx=5,pady=5)
            self.option_selected.set(self.nombre_sede[0])

            self.frame_export_excel = ctk.CTkFrame(master= self.cuerpo_principal_top,fg_color="#2C3F59",width=300, height=40)
            self.frame_export_excel.grid(row=0,column=1,padx=5,pady=5)

            self.export_excel_trabxsede = ctk.CTkButton(master=self.frame_export_excel, 
                                                        fg_color="#F5E88C", 
                                                        text="Exportar Excel",
                                                        text_color="black",
                                                        width=300, 
                                                        height=40,
                                                        font=("Arial",15),
                                                        hover_color="#F5E874",border_color="#F5E874",border_width=3)
            self.export_excel_trabxsede.pack(side=ctk.TOP, expand= True, fill = ctk.BOTH)

      def init_widgets_sedes(self):
            self.frames_sedes_top = {}#array de los frames del top
            self.frame_top =tk.Frame(master=self,bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

            for F in range(3): #creamos 1 frame que contiene el frame top(modificamos el número de recuadros requeridos)
                  frame = ctk.CTkFrame(master=self.frame_top, fg_color="#2C3F59", border_width=3,border_color="black")
                  self.frames_sedes_top[F] = frame
                  frame.pack(pady=5,padx=5,side=tk.RIGHT ,fill=tk.BOTH, expand = True)
                  
            ##SECCIÓN INFERIOR

            #Creamos el FRAME PADRE_BOTTOM
            self.frames_sedes_bottom = {}#array de los frames del bottom
            self.frame_bottom =tk.Frame(master=self,bg=COLOR_CUERPO_PRINCIPAL)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )

            for F in range(2):#creamos los 2 frames que contiene el frame bottom
                  frame = ctk.CTkFrame(master=self.frame_bottom,fg_color="#2C3F59", border_width=3,border_color="black")
                  self.frames_sedes_bottom[F] = frame
                  frame.pack(pady=1,padx=1,side=tk.RIGHT, fill=tk.BOTH, expand = True)

            #Creamos el frame que contendrá nuestra tabla
            self.frame_table = tk.Frame(master= self.frames_sedes_bottom[0],background="#2C3F59")
            self.frame_table.pack(padx=3,pady=3,side=tk.TOP, fill=tk.BOTH, expand= True)

            # Filtrar el DataFrame para las columnas requeridas
            table_columns = ["DNI", "NOMBRE", "SEDE", "ESTADO"]
            df_filtered = self.dfdatos_trabajadores[table_columns]

            # Convertir el DataFrame a una lista de listas
            table_data = df_filtered.values.tolist()

            # Crear la tabla con los datos filtrados
            self.table = Graficos.create_grafico_table(self.frame_table, table_columns, table_data)


            #Creamos el frame que contendrá nuestro gráfico de barras
            self.frame_bar_chart = tk.Frame(master= self.frames_sedes_bottom[1], background="#2C3F59")
            self.frame_bar_chart.pack(side=tk.LEFT, fill=tk.BOTH, expand= True)

            # Crear horizontal_bar_chart con los datos de las sedes
            sede_counts = self.dfdatos_trabajadores["SEDE"].value_counts()

            Graficos.create_grafico_bar_horizontal(self.frame_bar_chart,x_data=sede_counts.values,y_data=sede_counts.index,
                        xlabel='Cantidad de Trabajadores',
                        ylabel='Sede',
                        title='Cantidad de Trabajadores por Sede')
            
      def update_chart(self, *args):

            selected_sede = None
            
            for id_sede, nombre_sede in self.nombre_sedes_mapping.items():
                  if nombre_sede == self.option_selected.get():
                        selected_sede = id_sede
                        break
            if not selected_sede:
                  return

            dfdatos_trabajadores = pd.DataFrame(
                        data = db_connection.ejecutar_sp_con_params("usp_ListaTrabajadores","@SEDE=?",selected_sede),
                        columns=["ID", "DNI","NOMBRE","HORARIO","CONTRATO","FECHA_INICIO","ESTADO","FECHA_FIN","SEDE","CORREO","NUMERO"])
            
            table_columns = ["DNI", "NOMBRE", "SEDE", "ESTADO"]
            listdatos_trabajadores = dfdatos_trabajadores[table_columns]


            Graficos.update_grafico_table(self.table, listdatos_trabajadores.values.tolist())



            #for widget in self.frame_dialog.winfo_children():
            #      widget.destroy()
            
            #Grafico Circular

            #labels = ["No Pagado", "Pagado",  "Pendiente"]

            #Graficos.update_grafico_circular(self.ax_pie, 
            #                                 self.wedges, 
            #                                 self.autotexts, 
            #                                self.canvas_pie, 
            #                                 labels, 
            #                                 dframeCancelados[4].value_counts(),
            #                                 "Trabajadores Pagados por Periodo",
            #                                 "Estados")
            
            #Creamos el frame que contendrá nuestra tabla
            #Graficos.update_grafico_table(self.table, data_cancelados)
     

  
    