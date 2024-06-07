import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graficos():
     def __init__():
        super().__init__()

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


      def create_grafico_circular():
         plt.figure(figsize=[10,8])
         autos = ['Kia', 'Toyota', 'Nissan', 'Suzuki', 'Audi']
         venta = [10.5,15.3,14.2,16.1,9.8]
         destacar = (0.1,0,0,0,0)
         plt.style.use('ggplot')
         plt.title('Ventas de autos en EEUU')
         plt.pie(x=venta, explode=destacar,labels=autos,autopct='%.2f%%', shadow=True, startangle=20)
         plt.axis=('equal')
         plt.legend(loc='upper left')
         plt.show()