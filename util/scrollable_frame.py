import tkinter as tk

class ScrollableFrame(tk.Frame):
    def __init__(self, parent, bg_color, scrollbar_color="#2C3F59", scrollbar_width=15):
        super().__init__(parent)

        self.canvas = tk.Canvas(self, bg=bg_color, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview, 
                                      bg=scrollbar_color, troughcolor=scrollbar_color, 
                                      activebackground=scrollbar_color, bd=0, width=scrollbar_width)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollable_frame = tk.Frame(self.canvas, bg=bg_color)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")