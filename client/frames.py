import tkinter as tk
import config as cfg 


class Trabajador(tk.Frame):
    def __init__(self,parent):
          super().__init__(parent)
          self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)

    def init_widgets_trabajador(self):
        tk.Label(self.frame_trabajador, text="Hola mundo", bg="black", fg="black").pack(fill=tk.BOTH)

class Sedes(tk.Frame):
        def __init__(self, parent):
              super().__init__(parent)
              self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
    
        def init_widgets_sedes(self):  
            tk.Label(
                        self,
                        text="Adios mundo",
                        fg="black"
                    ).pack(
                          fill=tk.BOTH
                          )
class Pagos(tk.Frame):
        def __init__(self,parent):
              super().__init__(parent)
              self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)

        def init_widgets_Pagos(self):
              tk.Label(
                    self,
                    text="Pagos",
                    bg="red").pack(fill=tk.BOTH)
              

        # Frame for Pagos
 #       frame_pagos = tk.Frame(self.cuerpo_principal)
 #       label_pagos = tk.Label(frame_pagos, text="HOLA")
 #       label_pagos.pack(side=tk.RIGHT)
 #       self.frames['pagos'] = frame_pagos
 #       self.create_line_chart(frame_pagos)

        # Show the default frame
#    def create_line_chart(self, frame):
        # Datos de ejemplo - reemplaza esto con la consulta a la base de datos
 #       periodos = ['012024', '022024', '032024', '042024', '052024']
#        montos = [1000, 1500, 2000, 2500, 3000]

        # Crear la figura de matplotlib
#        fig = Figure(figsize=(5, 4), dpi=100)
 #       ax = fig.add_subplot(111)
  #      ax.plot(periodos, montos)

#        ax.set_xlabel('PERIODO')
#        ax.set_ylabel('MONTO')
#        ax.set_title('Monto por Periodo')

        # Crear el canvas de tkinter para la figura de matplotlib
#        canvas = FigureCanvasTkAgg(fig, master=frame)
#        canvas.draw()
#        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    