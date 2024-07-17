import tkinter as tk
import customtkinter as ctk

class CustomOptionMenu(ctk.CTkOptionMenu):
    def __init__(self, *args, dropdown_height=10, **kwargs):
        super().__init__(*args, **kwargs)
        self.dropdown_height = dropdown_height

    def _create_dropdown(self):
        self._dropdown = ctk.CTkToplevel(self)
        self._dropdown.wm_overrideredirect(True)
        self._dropdown.configure(bg=self._fg_color)

        frame = ctk.CTkFrame(self._dropdown, bg=self._fg_color)
        frame.pack()

        canvas = tk.Canvas(frame, height=self.dropdown_height, bg=self._fg_color)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ctk.CTkFrame(canvas, bg=self._fg_color)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        for i, value in enumerate(self._values):
            button = ctk.CTkButton(scrollable_frame, text=value, command=lambda val=value: self._set_value(val))
            button.pack(fill="x", padx=2, pady=2)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self._dropdown.update_idletasks()

        self._dropdown.geometry(f"{self._dropdown.winfo_width()}x{self.dropdown_height}+{self.winfo_rootx()}+{self.winfo_rooty() + self.winfo_height()}")

    def _set_value(self, value):
        self._current_value.set(value)
        self._dropdown.destroy()
        self._dropdown = None
        if self._command:
            self._command(value)