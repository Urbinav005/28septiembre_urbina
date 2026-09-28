import tkinter as tk

# 1. Crear la ventana principal (root)
root = tk.Tk()

# 2. Asignar un título
root.title("Prueba de Tkinter - Rodolfo")

# 3. Configurar el tamaño
root.geometry("350x150")

# 4. Crear y mostrar una etiqueta (label)
label = tk.Label(root, text="¡Hola! Tkinter funciona correctamente.")
label.pack(pady=40)

# 5. Iniciar la ventana
root.mainloop()