from logging import root
from tkinter import *

def mainGUI():

    from tkinter import ttk
    import tkinter as tk
    from PIL import ImageTk, Image
    import os 
    
    import json
    import logging
    logger = logging.getLogger('grafica.mainGUI')  
    try:
        with open('json\\clientes.json',"r", encoding="utf-8") as j:
            diccionarioClientes = json.load(j) 
    except FileNotFoundError  as error:
        logger.error("Hubo un error al leer el archivo JSON: %s"%error)
        
    ventana = Tk()             #Crea la raíz
    ventana.title("Creador de proyectos")   #Título de la ventana
    ventana.resizable(0,0)     #Desactiva redimensión de la ventana
    
    frm = ttk.Frame(ventana, padding = 10)     #Hijo del root. No hace  nada
    frm.grid()
    
    #Defino variables string 
    raiz = tk.StringVar()
    listadoDocumentos = tk.StringVar()
    nombreProyecto = tk.StringVar()
    trabajo = tk.StringVar()
    cliente = tk.StringVar()
    
    #Defino entradas de texto con la asignación de las variables anteriores
    raizTxt = ttk.Entry(frm, textvariable= raiz)
    listadoDocumentosTxt = ttk.Entry(frm, textvariable = listadoDocumentos) 
    nombreProyectoTxt = ttk.Entry(frm, textvariable=nombreProyecto)
    clienteCMB = ttk.Combobox(frm, values=[value["nombre"] for value in diccionarioClientes.values()])
    trabajoCMB = ttk.Combobox(frm, values=["PR", "MAN", "RE"])
    #------------------------------------------------------------------------

    
    def seleccionarRaiz():
        from tkinter import filedialog
        directorio = filedialog.askdirectory()
        raiz.set(value = directorio)
        
    #------------------------------------------------------------------------           
        
    def seleccionarListado():
        from tkinter import filedialog
        listadoExcel = filedialog.askopenfilename()
        listadoDocumentos.set(value = listadoExcel)
        
    #------------------------------------------------------------------------ 
    
    def crearProyecto():
        from tkinter import messagebox
        from armadoCarpetas import creacionCarpetas
        import os 
        
        nombreProyecto = nombreProyectoTxt.get()
        directorio = raizTxt.get()
        listadoDocumentos = listadoDocumentosTxt.get()
        trabajo = trabajoCMB.get()
        clienteCompleto = clienteCMB.get()
        cliente = [diccionarioClientes[item]["acronimo"] for item in diccionarioClientes.keys() if diccionarioClientes[item]["nombre"] == clienteCompleto][0] 
        
        vuelta = 0
        auxVuelta = 0
        directorioActual = os.path.dirname(os.path.abspath(__file__))
        if cliente == '': 
            messagebox.showerror(title = "Error", message = u"Debe seleccionar un cliente")
            logger.error("No se seleccionó un cliente")
        elif trabajo == '':     
            messagebox.showerror(title = "Error", message = u"Debe seleccionar un tipo de trabajo")
            logger.error("No se seleccionó un trabajo")
        else:
            if directorio == None or directorio == '':
                vuelta = messagebox.askyesno(title = u"Atención", message = u"El proyecto se guardará en el directorio donde se está ejecutando este script: %s. ¿Desea continuar?"%directorioActual)
                auxVuelta += 1 if not vuelta else 0
                directorio = directorioActual        
            if (listadoDocumentos == None or listadoDocumentos  == '' ) and not auxVuelta:
                vuelta = messagebox.askyesno(title = u"Atención", message = u"No se eligió un listado de documentos. Se creará un proyecto default.  ¿Desea continuar?") 
                auxVuelta += 1 if not vuelta else 0
            if (nombreProyecto == None or nombreProyecto  == '') and not auxVuelta:
                nombreProyecto = 'pepito'
                vuelta = messagebox.askyesno(title = u"Atención", message = u"No escribió un nombre para el proyecto. Se creará un proyecto default de nombre: %s.  ¿Desea continuar?"%nombreProyecto) 
                auxVuelta += 1 if not vuelta else 0
                
            if not auxVuelta:
                messagebox.showinfo(title = "Mensaje", message = u"Se va a crear el proyecto: %s en %s"%(nombreProyecto, directorio))
                import datetime
                ahora = datetime.datetime.now()
                fecha = ahora.date()
                anio = fecha.strftime("%y")
                prefijo = cliente + '-' + trabajo + '-' + anio + '-' 
                creacionCarpetas(prefijo, nombreProyecto,directorio,listadoDocumentos)
            auxVuelta = 0
        


    #INSTANCIACIÓN DE OBJETOS                
    #print(cliente["nombre"] for cliente in diccionarioClientes.items())    
    ttk.Label(frm, text = 'Nombre:', justify = 'left').grid(column = 0, row = 0, columnspan = 1)
    nombreProyectoTxt.grid(column=1,row=0)
    ttk.Label(frm, text = 'Cliente:', justify = 'left').grid(column = 0, row = 1, columnspan = 1)
    clienteCMB.grid(column=1, row = 1, columnspan = 1, pady = 3)
    ttk.Label(frm, text = 'Tipo de trabajo:', justify = 'left').grid(column = 0, row = 2, columnspan = 1)
    trabajoCMB.grid(column=1, row = 2, columnspan = 1, pady= 3)
    
    ttk.Label(frm, text = 'Root: ').grid(column = 0, row = 3)
    raizTxt.grid(column = 1, row = 3)
    ttk.Button(frm, text = 'Buscar', command = seleccionarRaiz).grid(column = 2, row = 3, columnspan = 2)
    ttk.Label(frm, text = 'Listado de documentos: ').grid(column = 0, row = 4)
    listadoDocumentosTxt.grid(column = 1, row = 4)
    ttk.Button(frm, text = 'Buscar', command = seleccionarListado).grid(column = 2, row = 4, columnspan = 2)
    ttk.Button(frm, text = 'Crear', command=crearProyecto).grid(column = 2, row = 5, columnspan = 2)
    
    menubar = Menu(ventana)
    ventana.config(menu=menubar)
    file_menu = Menu(menubar)
    config_menu = Menu(menubar)
    help_menu = Menu(menubar)
    menubar.add_cascade(
    label="Archivo",
    menu=file_menu
)    
    file_menu.add_command(
    label='Salir',
    command=ventana.destroy,
)
    menubar.add_cascade(
    label="Configuración",
    menu=config_menu
)    
    config_menu.add_command(
    label='Editar archivos',
    
)
    config_menu.add_command(
    label='Editar clientes',
    
)
    menubar.add_cascade(
    label="Ayuda",
    menu=help_menu
)    
    help_menu.add_command(
    label='Instructivo',
    
)
    
    
    
    ventana.mainloop()