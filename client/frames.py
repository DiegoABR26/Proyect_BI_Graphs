import tkinter as tk
import config as cfg 
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_CURSOR_ENCIMA, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_LATERAL
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
                  frame = tk.Frame(master=self.frame_top,bg="red")
                  self.frames_trabajador_top[F] = frame
                  frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
                  tk.Label(frame,text="Aquí estoy f{}".format(F), bg="blue").pack(side=tk.TOP)
            
            self.frame1_top = tk.Frame(self.frames_trabajador_top[0], bg="black")
            self.frame1_top.pack(side=tk.BOTTOM, fill=tk.BOTH, expand= True)
            Graficos.create_line_chart(self.frame1_top)

            self.frames_trabajador_bottom = {}

            self.frame_bottom =tk.Frame(master=self)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )


            for F in range(4):
                  frame = tk.Frame(master=self.frame_bottom,bg="red")
                  self.frames_trabajador_bottom[F] = frame
                  frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
                  tk.Label(frame,text="Aquí estoy f{}".format(F), bg="blue").pack(side=tk.TOP)
            
            self.frame1_bottom = tk.Frame(self.frames_trabajador_bottom[0], bg="black")
            self.frame1_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand= True)
            Graficos.create_line_chart(self.frame1_bottom)
            

class Pagos(tk.Frame):
        def __init__(self, parent, controller):
              super().__init__(parent)
              self.configure(bg=cfg.COLOR_CUERPO_PRINCIPAL)
              self.init_widgets_Pagos()

        def init_widgets_Pagos(self):
            self.frame_top =tk.Frame(master=self)
            self.frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand = True)

            self.frames_pagos_top = {}

            for F in range(4):
                  frame = tk.Frame(master=self.frame_top,bg="red")
                  self.frames_pagos_top[F] = frame
                  frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
                  tk.Label(frame,text="Aquí estoy f{}".format(F), bg="blue").pack(side=tk.TOP)
            
            self.nuevo_frame = tk.Frame(self.frames_pagos_top[0], bg="black")
            self.nuevo_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand= True)

            self.frames_pagos_bottom = {}

            self.frame_bottom =tk.Frame(master=self)
            self.frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand = True )


            for F in range(4):
                  frame = tk.Frame(master=self.frame_bottom,bg="red")
                  self.frames_pagos_bottom[F] = frame
                  frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand = True)
                  tk.Label(frame,text="Aquí estoy f{}".format(F), bg="blue").pack(side=tk.TOP)
            
            self.nuevo_frame = tk.Frame(self.frames_pagos_bottom[0], bg="black")
            self.nuevo_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand= True)

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
     

  
    