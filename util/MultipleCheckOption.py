import tkinter as tk
import customtkinter as ctk

class MultipleCheckOption(tk.Frame):
    def __init__(self, parent, options, variable, dropdown_height=200, **kwargs):
        super().__init__(parent, **kwargs)
        self.variable = variable
        self.variable.set([])  # Initialize with an empty list
        self.options = options
        self.dropdown_height = dropdown_height

        self.button = ctk.CTkButton(self, text="Select Options", command=self._toggle_dropdown)
        self.button.pack(fill="x")

        self.dropdown = None

    def _toggle_dropdown(self):
        if self.dropdown is None:
            self._create_dropdown()
        else:
            self._close_dropdown()

    def _create_dropdown(self):
        self.dropdown = ctk.CTkToplevel(self)
        self.dropdown.wm_overrideredirect(True)
        self.dropdown.configure(bg="white")

        frame = ctk.CTkFrame(self.dropdown, bg="white")
        frame.pack()

        canvas = tk.Canvas(frame, height=self.dropdown_height, bg="white")
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ctk.CTkFrame(canvas, bg="white")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.checkbuttons = []
        self.var_list = []

        for option in self.options:
            var = tk.StringVar(value=option)
            cb = ctk.CTkCheckBox(scrollable_frame, text=option, variable=var, onvalue=option, offvalue="")
            cb.pack(fill="x", padx=2, pady=2)
            self.checkbuttons.append(cb)
            self.var_list.append(var)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.dropdown.update_idletasks()

        self.dropdown.geometry(f"{self.dropdown.winfo_width()}x{self.dropdown_height}+{self.winfo_rootx()}+{self.winfo_rooty() + self.winfo_height()}")

    def _close_dropdown(self):
        selected_values = [var.get() for var in self.var_list if var.get()]
        self.variable.set(selected_values)
        self.dropdown.destroy()
        self.dropdown = None

        # Update the button text with selected values or a placeholder if none are selected
        if selected_values:
            self.button.configure(text=", ".join(selected_values))
        else:
            self.button.configure(text="Select Options")