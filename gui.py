# Interfaz gráfica
import tkinter as tk
from tkinter import ttk
from destinos_perfectos import generar_recomendacion

def recomendar_destinos():
    preferencias = preferencias_var.get() if preferencias_var.get() else None
    tipo_viaje = tipo_viaje_var.get() if tipo_viaje_var.get() else None
    presupuesto = presupuesto_var.get() if presupuesto_var.get() else None

    recomendaciones = generar_recomendacion(preferencias, tipo_viaje, presupuesto)

    resultado_var.set(", ".join(recomendaciones) if recomendaciones else "No hay recomendaciones disponibles")

ventana = tk.Tk()
ventana.title("Destinos Perfectos")

preferencias_var = tk.StringVar()
tipo_viaje_var = tk.StringVar()
presupuesto_var = tk.StringVar()
resultado_var = tk.StringVar()

ttk.Label(ventana, text="Preferencias:").grid(column=0, row=0)
preferencias_menu = ttk.Combobox(ventana, textvariable=preferencias_var)
preferencias_menu['values'] = ("aventura", "playa", "ciudad", "naturaleza", "cultura")
preferencias_menu.grid(column=1, row=0)

ttk.Label(ventana, text="Tipo de viaje:").grid(column=0, row=1)
tipo_viaje_menu = ttk.Combobox(ventana, textvariable=tipo_viaje_var)
tipo_viaje_menu['values'] = ("individual", "familiar", "grupal")
tipo_viaje_menu.grid(column=1, row=1)

ttk.Label(ventana, text="Presupuesto:").grid(column=0, row=2)
presupuesto_menu = ttk.Combobox(ventana, textvariable=presupuesto_var)
presupuesto_menu['values'] = ("bajo", "medio", "alto")
presupuesto_menu.grid(column=1, row=2)

ttk.Button(ventana, text="Recomendar Destino", command=recomendar_destinos).grid(column=1, row=3)

ttk.Label(ventana, text="Recomendaciones:").grid(column=0, row=4)
ttk.Label(ventana, textvariable=resultado_var).grid(column=1, row=4)

ventana.mainloop()
