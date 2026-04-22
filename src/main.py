import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def main():
    root = ctk.CTk()
    root.title("Spiral Generator")
    root.geometry("1200x700")

    left_panel = ctk.CTkFrame(root, width=300)
    left_panel.pack(side = "left", fill = "y", padx=10, pady=10)

    right_panel = ctk.CTkFrame(root)
    right_panel.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True)

    _create_label_slider(left_panel, "Length Limit", 200, 1001)
    _create_label_slider(left_panel, "Starting Length", 0.0000001, 1.1)
    _create_label_slider(left_panel, "Sample Size", 1, 10, 9)
    _create_label_slider(left_panel, "Starting Thickness", 0, 2)
    _create_label_slider(left_panel, "Initial Heading", 0, 360)
    _create_label_slider(left_panel, "Rotation Angle", 0, 360)
    _create_label_slider(left_panel, "Growth Rate", 0, 1)

    root.mainloop()

def _create_label_slider(left_panel, txt, start, end, step_ct=None):
    slider_label = ctk.CTkLabel(left_panel, text=txt)
    slider_label.pack(pady=(20, 0))

    angle_slider = ctk.CTkSlider(left_panel, from_=start, to=end, number_of_steps=step_ct)
    angle_slider.pack(pady=20)


if __name__ == "__main__":
    main()