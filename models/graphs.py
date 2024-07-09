import numpy as np
from tkinter import ttk
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graficos():
      def __init__():
         super().__init__()

      def create_grafico_line(frame, data, labels, xlabel, ylabel, title):#(frame, data, labels, xlabel, ylabel, title, canvas=None, ax=None):
            fig = Figure(figsize=(5, 2), dpi=100, facecolor="#2C3F59")
            ax = fig.add_subplot(111, facecolor = "#2C3F59")
            ax.plot(labels, data, marker = "o", color= "#F25244")
            ax.set_title(title, fontsize=10, color="white")
            ax.set_xlabel(xlabel, color="white")
            ax.set_ylabel(ylabel, color="white")

            ax.tick_params(axis='x', colors="white")
            ax.tick_params(axis='y', colors="white")

            # Añadir anotaciones a los puntos
            for i in range(len(data)):
                  ax.annotate(f'{data[i]}', (labels[i], data[i]), textcoords="offset points", xytext=(0,10), ha='center', color="white")


            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            return fig, ax, canvas


      def create_grafico_circular(frame, labels, data, title, title_legend="leyenda"):#(frame, labels, data, title, title_legend="leyenda", canvas=None, ax=None):
            fig, ax = plt.subplots(figsize=(5, 2), subplot_kw=dict(aspect="equal"), facecolor="#2C3F59")
            colors = ["#6698F6", "#6EE1F8", "#F7FAA3"]
            wedgeprops = {"edgecolor": "white", "linewidth": 1}
            wedges, texts, autotexts = ax.pie(data, 
                                          autopct=lambda pct: f"{pct:.1f}%\n({int(np.round(pct / 100. * np.sum(data))):d})",
                                          textprops=dict(color="black"),
                                          colors=colors,
                                          wedgeprops=wedgeprops)
            ax.legend(wedges, labels, title=title_legend, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
            plt.setp(autotexts, size=8, weight="bold")
            ax.set_title(title, color="white")

            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            def on_hover(event):
                  hovered = False
                  for i, wedge in enumerate(wedges):
                        if wedge.contains_point([event.x, event.y]):
                              angle = (wedge.theta2 + wedge.theta1) / 2  # Calculate the middle angle of the wedge
                              x_offset = 0.1 * np.cos(np.deg2rad(angle))  # Calculate the x offset
                              y_offset = 0.1 * np.sin(np.deg2rad(angle))  # Calculate the y offset
                              wedge.set_center((x_offset, y_offset))  # Move the wedge center
                              wedge.set_radius(1.1)  # Highlight the hovered wedge by moving it outwards
                              autotexts[i].set_fontsize(12)  # Increase the font size of the text
                              canvas.draw()
                              hovered = True
                        else:
                              wedge.set_radius(1.0)  # Reset all wedges to their original position
                              wedge.set_center((0, 0))  # Reset center to original position
                              autotexts[i].set_fontsize(8)  # Reset font size of the text
                  if not hovered:
                        for autotext in autotexts:
                              autotext.set_fontsize(8)  # Ensure all text is reset to normal size if not hovered
                        canvas.draw()

            canvas.mpl_connect("motion_notify_event", on_hover)
            return fig, ax, wedges, autotexts, canvas
      
      def update_grafico_circular(ax, wedges, autotexts, canvas, labels, data, title, title_legend,):
        ax.clear()
        wedges, texts, autotexts = ax.pie(data, 
                                          autopct=lambda pct: f"{pct:.1f}%\n({int(np.round(pct / 100. * np.sum(data))):d})",
                                          textprops=dict(color="black"),
                                          colors=["#6698F6", "#6EE1F8", "#F7FAA3"],
                                          wedgeprops={"edgecolor": "white", "linewidth": 1})
        ax.legend(wedges, labels, title=title_legend, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        ax.set_title(title, color="white")
        
        def on_hover(event):
            hovered = False
            for i, wedge in enumerate(wedges):
                  if wedge.contains_point([event.x, event.y]):
                        angle = (wedge.theta2 + wedge.theta1) / 2  # Calculate the middle angle of the wedge
                        x_offset = 0.1 * np.cos(np.deg2rad(angle))  # Calculate the x offset
                        y_offset = 0.1 * np.sin(np.deg2rad(angle))  # Calculate the y offset
                        wedge.set_center((x_offset, y_offset))  # Move the wedge center
                        wedge.set_radius(1.1)  # Highlight the hovered wedge by moving it outwards
                        autotexts[i].set_fontsize(12)  # Increase the font size of the text
                        canvas.draw()
                        hovered = True
                  else:
                        wedge.set_radius(1.0)  # Reset all wedges to their original position
                        wedge.set_center((0, 0))  # Reset center to original position
                        autotexts[i].set_fontsize(8)  # Reset font size of the text
            if not hovered:
                  for autotext in autotexts:
                        autotext.set_fontsize(8)  # Ensure all text is reset to normal size if not hovered
                  canvas.draw()
                        
        canvas.mpl_connect("motion_notify_event", on_hover)
        ax.figure.canvas.draw()

      def create_grafico_table(frame, table_columns, table_data):
            table = ttk.Treeview(master=frame, columns=table_columns, show='headings')
            for column in table_columns:
                  table.heading(column=column, text=column)
                  table.column(column=column, width=70)
            if len(table_data) > 0:
                  for row_data in table_data:
                        table.insert(parent="", index="end", values=row_data)
            else:
                  table.insert(parent="", index="end", values="No hay data que mostrar")
            style = ttk.Style()
            style.theme_use('default')
            style.configure("Treeview.Heading", background="#F28B50", fieldbackground="black", foreground="white")
            style.configure("Treeview", background="#2C3F59", fieldbackground="#2C3F59", foreground="white")
            style.map('Treeview', background=[("selected", "#F28B50")], foreground=[("selected", "white")])
            style.map('Treeview.Heading', background=[("selected", "black")], foreground=[("selected", "white")])
            table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            return table
      
      def update_grafico_table(table, table_data):
        for i in table.get_children():
            table.delete(i)
        for row_data in table_data:
            table.insert(parent="", index="end", values=row_data)          
          
