import tkinter as tk
from tkinter import messagebox
from collections import deque

# Inicialización de la cola y variables de control
queue = deque(maxlen=5)
steps = []
removed_numbers = []
step_count = 0

# Funciones de la aplicación
def add_number():
    global step_count
    number = entry.get()

    # Verifica que el número ingresado sea válido
    if not number.isdigit():
        messagebox.showwarning("Entrada inválida", "Por favor, ingrese un número válido.")
        return

    number = int(number)
    entry.delete(0, tk.END)

    # Verifica si el número ya está en la cola
    if number in queue:
        messagebox.showwarning("Número duplicado", f"El número {number} ya está en la cola.")
        return

    step_count += 1

    # Si la cola está llena, eliminar el primer elemento y mostrarlo en "Datos eliminados"
    if len(queue) == queue.maxlen:
        removed = queue.popleft()
        queue.append(number)
        removed_numbers.append(removed)
        step_text = f"Paso {step_count}: Se eliminó el número {removed} y se agregó el número {number}. Estado actual: {list(queue)}"
        
        # Actualizar la sección de datos eliminados y la visualización de la cola
        update_queue_display()
        update_removed_display()
    else:
        # Si no está llena, solo agregar el nuevo número
        queue.append(number)
        step_text = f"Paso {step_count}: Se agregó el número {number}. Estado actual: {list(queue)}"
        update_queue_display()

    steps.append(step_text)
    update_steps_display()

def update_queue_display():
    """Actualiza la visualización de la cola."""
    for widget in queue_container.winfo_children():
        widget.destroy()

    for num in queue:
        item = tk.Label(queue_container, text=num, width=4, height=2, bg="#4CAF50", fg="white", font=("Arial", 14))
        item.pack(side=tk.LEFT, padx=2)

def update_removed_display():
    """Actualiza la visualización de los datos eliminados."""
    for widget in removed_container.winfo_children():
        widget.destroy()

    for num in removed_numbers:
        item = tk.Label(removed_container, text=num, width=4, height=2, bg="red", fg="white", font=("Arial", 14))
        item.pack(side=tk.TOP, pady=2)

def update_steps_display():
    """Muestra los pasos realizados en el algoritmo FIFO."""
    steps_text.delete("1.0", tk.END)
    steps_text.insert(tk.END, "\n".join(steps))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Algoritmo FIFO (First In, First Out)")
root.geometry("800x400")
root.config(bg="#f0f0f0")

# Marco principal para organizar los elementos
main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack(pady=10, padx=10, fill="both", expand=True)

# Marco izquierdo para la cola y pasos
left_frame = tk.Frame(main_frame, bg="#f0f0f0")
left_frame.pack(side=tk.LEFT, fill="both", expand=True)

# Título
title = tk.Label(left_frame, text="Algoritmo FIFO (First In, First Out)", font=("Arial", 16), bg="#f0f0f0", fg="#333")
title.pack(pady=10)

# Sección de entrada de número
input_frame = tk.Frame(left_frame, bg="#f0f0f0")
input_frame.pack(pady=10)

entry = tk.Entry(input_frame, width=10, font=("Arial", 14))
entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(input_frame, text="Agregar", command=add_number, font=("Arial", 12), bg="#4CAF50", fg="white")
add_button.pack(side=tk.LEFT, padx=5)

# Contenedor de la cola
queue_container = tk.Frame(left_frame, bg="#f0f0f0")
queue_container.pack(pady=20)

# Sección de pasos
steps_label = tk.Label(left_frame, text="Paso a paso:", font=("Arial", 14), bg="#f0f0f0", fg="#333")
steps_label.pack(pady=5)

steps_text = tk.Text(left_frame, width=50, height=8, wrap="word", font=("Arial", 12))
steps_text.pack(pady=5)

# Marco derecho para "Datos eliminados"
right_frame = tk.Frame(main_frame, bg="#f0f0f0")
right_frame.pack(side=tk.LEFT, fill="y", padx=20)

removed_label = tk.Label(right_frame, text="Datos eliminados:", font=("Arial", 14), bg="#f0f0f0", fg="#333")
removed_label.pack(pady=5)

removed_container = tk.Frame(right_frame, bg="#f0f0f0")
removed_container.pack(pady=10)

# Iniciar la aplicación
root.mainloop()
