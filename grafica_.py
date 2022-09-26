from cgitb import text
from logging import root
from tkinter import *
from turtle import bgcolor
from setuptools import Command 
import tkinter as tk    
from tkinter import ttk
from tkinter import messagebox

def tabla(frm,data):
    filas = len(data)
    columnas = len(data[0])
    tabla = ttk.Treeview(frm)
    headers = data[0]
    #define our column
    tabla['columns'] = headers
    tabla.column("#0", width=0,  stretch=NO)
    tabla.heading("#0",text="",anchor=CENTER)
    for columna in data[0]:
        # format our column
        tabla.column(columna,anchor=CENTER, width=150)

        #Create Headings 
        tabla.heading(columna,text=columna,anchor=CENTER)
    id = 0
    for fila in data:
        
        if fila == headers:
            pass
        else:
            tabla.insert(parent='',index='end',iid=id,text='',
            values=fila)
            id += 1
    tabla.grid(column = 1, row = 0, columnspan = 2)  

    return tabla

def editaArchivosGUI(frmEA):
    import os 
    import json
    import logging
    logger = logging.getLogger('grafica.editaArchivosGUI')
    try:
        with open('json\\tipoArchivo.json',"r", encoding="utf-8") as j:
            diccionarioArchivos = json.load(j) 
    except FileNotFoundError  as error:
        logger.error("Hubo un error al leer el archivo JSON: %s"%error)  
    

    frmTab = ttk.Frame(frmEA)
    frmTab.grid(column = 0, row = 0)
    frmBotonera = ttk.Frame(frmEA)
    frmBotonera.grid(column = 1, row = 0)        
    data = []
    data.append(['Acrónimo','Nombre','Formato'])
    for key1 in diccionarioArchivos.keys():
        formato = diccionarioArchivos[key1]
        for key2 in formato.keys():
            id = formato[key2]
            data.append([id['acronimo'],id['nombre'],key1])
    tabArchivos = tabla(frmTab,data)
    
    #Defino variables string 
    acronimo = tk.StringVar()
    nombre = tk.StringVar()
    formato = tk.StringVar()
    #Defino entradas de texto con la asignación de las variables anteriores
    txtAcronimo = ttk.Entry(frmBotonera, textvariable = acronimo, state=DISABLED)
    txtAcronimo.grid(column = 5, row = 0, columnspan = 2) 
    txtNombre = ttk.Entry(frmBotonera, textvariable=nombre, state=DISABLED)
    txtNombre.grid(column = 5, row = 1, columnspan = 2)
    cmbFormato = ttk.Combobox(frmBotonera, values=["EXCEL", "WORD", "CAD","PROJECT","POWERPOINT","VISIO"],textvariable=formato, state=DISABLED)
    cmbFormato.grid(column = 5, row = 3, columnspan = 2)
    
    def cancelar():
        vaciarCajas()
        txtAcronimo['state']=DISABLED
        txtNombre['state']=DISABLED
        cmbFormato['state']=DISABLED       
    
    def habilitar():
        txtAcronimo['state']=NORMAL
        txtNombre['state']=NORMAL
        cmbFormato['state']=NORMAL
            
    def vaciarCajas():
        txtAcronimo.delete(0,END)
        txtNombre.delete(0,END)
        cmbFormato.delete(0,END) 
        
    def select_record():
        selected = tabArchivos.focus()
        dataSel = tabArchivos.item(selected,'values')
        vaciarCajas()
        txtAcronimo.insert(0,dataSel[0])
        txtNombre.insert(0,dataSel[1])
        cmbFormato.insert(0,dataSel[2]) 
    def clicker(e):
        select_record()
    tabArchivos.bind('<ButtonRelease-1>', clicker)
    
 
#------------------------------------------------------------------------
    #INSTANCIACIÓN DE OBJETOS               

    agregarBtn = ttk.Button(frmBotonera, text = 'Agregar')
    agregarBtn.grid(column = 5, row = 4, columnspan = 2)
    editarBtn = ttk.Button(frmBotonera, text = 'Editar',command=habilitar)
    editarBtn.grid(column = 5, row = 5, columnspan = 2)
    borrarBtn = ttk.Button(frmBotonera, text = 'Borrar')
    borrarBtn.grid(column = 5, row = 6, columnspan = 2)
    guardarBtn = ttk.Button(frmBotonera, text = 'Guardar')
    guardarBtn.grid(column = 5, row = 7, columnspan = 2)
    cancelarBtn = ttk.Button(frmBotonera, text = 'Cancelar', command = cancelar)
    cancelarBtn.grid(column = 5, row = 8, columnspan = 2)      
    
    
def editaClientesGUI(frmEC):
    import os 
    import json
    import logging
    import tkinter as tk    
    from tkinter import ttk
    logger = logging.getLogger('grafica.editaClientesGUI')
    try:
        with open('json\\clientes.json',"r", encoding="utf-8") as j:
            diccionarioClientes = json.load(j) 
    except FileNotFoundError  as error:
        logger.error("Hubo un error al leer el archivo JSON: %s"%error) 
    

    frmTab = ttk.Frame(frmEC)
    frmTab.grid(column = 0, row = 0)
    frmBotonera = ttk.Frame(frmEC)
    frmBotonera.grid(column = 1, row = 0)        
    data = []
    data.append(['Acrónimo','Nombre','Habilitado'])
    for key1 in diccionarioClientes.keys():
        id = diccionarioClientes[key1]
        data.append([id['acronimo'],id['nombre'],id['habilitado']])
    tabClientes = tabla(frmTab,data)


    #Defino variables string 
    acronimo = tk.StringVar()
    nombre = tk.StringVar()
    habilitado = tk.IntVar()
    modo = tk.StringVar()
    cmdAgregar = tk.IntVar()
    cmdEditar = tk.IntVar()
    #Defino entradas de texto con la asignación de las variables anteriores
    txtAcronimo = ttk.Entry(frmBotonera, textvariable = acronimo, state=DISABLED)
    txtAcronimo.grid(column = 5, row = 0, columnspan = 2) 
    txtNombre = ttk.Entry(frmBotonera, textvariable=nombre, state=DISABLED)
    txtNombre.grid(column = 5, row = 1, columnspan = 2)
    chkHabilitado = ttk.Checkbutton(frmBotonera, text='Habilitado',variable=habilitado, onvalue = 1, offvalue = 0, state=DISABLED)
    chkHabilitado.grid(column = 5, row = 2, columnspan = 2)
    chkHabilitado.setvar(value=1)
    cmdAgregar.set(1)
    cmdEditar.set(0)
    modo.set("")
    def cancelar():
        vaciarCajas()
        txtAcronimo['state']=DISABLED
        txtNombre['state']=DISABLED
        chkHabilitado['state']=DISABLED
        modo.set("")  
        
    def habilitar():
        txtAcronimo['state']=NORMAL
        txtNombre['state']=NORMAL
        chkHabilitado['state']=NORMAL
        
    def borrar():
        pass
    
    def agregar():
        cmdAgregar.set(1)
        cmdEditar.set(0)
        modo.set("Modo : Agregar")
        habilitar()
        
    def editar():
        cmdAgregar.set(0)
        cmdEditar.set(1)
        modo.set("Modo : Editar")
        habilitar()
    
    def guardar():
        print("cmdAgregar ",cmdAgregar.get() )
        print("cmdEditar ",cmdEditar.get() )
        if(cmdAgregar.get() and not cmdEditar.get()):
            if(acronimo.get() != None and nombre.get() != None):
                print("acronimo ", acronimo.get())
                print("data ", data)
                for lista in data:
                    if acronimo.get() in lista:
                        print('acronimo está dentro de data')
                        txtAcronimo.configure({"background": 'red'})
                        break
                    else:
                        print("acronimo no está dentro de data")
            else:
                logger.warning('Está queriendo guardar un cliente con un acrónimo o nombre nulo')
                messagebox.showwarning(title = 'Atención', message = 'Está queriendo guardar un cliente con un acrónimo o nombre nulo')
                #validaciones...
        elif(not cmdAgregar.get() and not cmdEditar.get()):
            print(acronimo.get(),nombre.get(),habilitado.get())
            #validaciones...
            texto = "guardarSobreJson()"
        messagebox.showinfo(title = "Aviso", message = "No hace nada por ahora")
    def vaciarCajas():
        txtAcronimo.delete(0,END)
        txtNombre.delete(0,END)
        habilitado.set(0)
        
    def select_record():
        selected = tabClientes.focus()
        dataSel = tabClientes.item(selected,'values')
        
        print(selected)
        print(dataSel)
        vaciarCajas()
        txtAcronimo.insert(0,dataSel[0])
        txtNombre.insert(0,dataSel[1])
        habilitado.set(int(dataSel[2]))
        
    def clicker(e):
        select_record()
    tabClientes.bind('<ButtonRelease-1>', clicker)
    
     #------------------------------------------------------------------------
    #INSTANCIACIÓN DE OBJETOS               

    agregarBtn = ttk.Button(frmBotonera, text = 'Agregar',command=agregar)
    agregarBtn.grid(column = 5, row = 4, columnspan = 2)
    editarBtn = ttk.Button(frmBotonera, text = 'Editar',command=editar)
    editarBtn.grid(column = 5, row = 5, columnspan = 2)
    borrarBtn = ttk.Button(frmBotonera, text = 'Borrar', command = borrar)
    borrarBtn.grid(column = 5, row = 6, columnspan = 2)
    guardarBtn = ttk.Button(frmBotonera, text = 'Guardar', command = guardar)
    guardarBtn.grid(column = 5, row = 7, columnspan = 2)    
    cancelarBtn = ttk.Button(frmBotonera, text = 'Cancelar', command = cancelar)
    cancelarBtn.grid(column = 5, row = 8, columnspan = 2)
    modoLabel = ttk.Label(frmBotonera, textvariable = modo)      
    modoLabel.grid(column = 5, row = 9, columnspan = 2)
    
def instructivoAyudaGUI(frmHelp):
    import logging
    logger = logging.getLogger('grafica.instructivoAyudaGUI') 
    pass


def creaproyectosGUI(frmCP):
    from tkinter import ttk
    import tkinter as tk
    from PIL import ImageTk, Image
    import os 
    import json
    import logging
    logger = logging.getLogger('grafica.creaproyectosGUI')  
    try:
        with open('json\\clientes.json',"r", encoding="utf-8") as j:
            diccionarioClientes = json.load(j) 
    except FileNotFoundError  as error:
        logger.error("Hubo un error al leer el archivo JSON: %s"%error)
           
    #Defino variables string 
    raiz = tk.StringVar()
    listadoDocumentos = tk.StringVar()
    nombreProyecto = tk.StringVar()
    trabajo = tk.StringVar()
    cliente = tk.StringVar()
    
    #Defino entradas de texto con la asignación de las variables anteriores
    raizTxt = ttk.Entry(frmCP, textvariable= raiz)
    listadoDocumentosTxt = ttk.Entry(frmCP, textvariable = listadoDocumentos) 
    nombreProyectoTxt = ttk.Entry(frmCP, textvariable=nombreProyecto)
    clienteCMB = ttk.Combobox(frmCP, values=[value["nombre"] for value in diccionarioClientes.values()])
    trabajoCMB = ttk.Combobox(frmCP, values=["PR", "MAN", "RE"])
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
    ttk.Label(frmCP, text = 'Nombre:', justify = 'left').grid(column = 0, row = 0, columnspan = 1)
    nombreProyectoTxt.grid(column=1,row=0)
    ttk.Label(frmCP, text = 'Cliente:', justify = 'left').grid(column = 0, row = 1, columnspan = 1)
    clienteCMB.grid(column=1, row = 1, columnspan = 1, pady = 3)
    ttk.Label(frmCP, text = 'Tipo de trabajo:', justify = 'left').grid(column = 0, row = 2, columnspan = 1)
    trabajoCMB.grid(column=1, row = 2, columnspan = 1, pady= 3)
    
    ttk.Label(frmCP, text = 'Root: ').grid(column = 0, row = 3)
    raizTxt.grid(column = 1, row = 3)
    ttk.Button(frmCP, text = 'Buscar', command = seleccionarRaiz).grid(column = 2, row = 3, columnspan = 2)
    ttk.Label(frmCP, text = 'Listado de documentos: ').grid(column = 0, row = 4)
    listadoDocumentosTxt.grid(column = 1, row = 4)
    ttk.Button(frmCP, text = 'Buscar', command = seleccionarListado).grid(column = 2, row = 4, columnspan = 2)
    ttk.Button(frmCP, text = 'Crear', command=crearProyecto).grid(column = 2, row = 5, columnspan = 2)
               
def mainGUI(frmMain):

    from tkinter import ttk
    import tkinter as tk
    from PIL import ImageTk, Image
    import os 
    import logging
    import webbrowser
    
    def callback():
        webbrowser.open_new("https://treeingenieria.com")
    
    logger = logging.getLogger('grafica.mainGUI')  
    logo = 'img\\tree.png'
    logo = ImageTk.PhotoImage(file = logo)
    #label_logo = ttk.Label(frmMain,image = logo).grid(column = 0, row = 4, columnspan = 2)
    titular = ttk.Label(frmMain, text = 'BIENVENIDO AL GENERADOR DE PROYECTOS', font = 'Calibri 13 bold',justify = 'center').grid(column = 0, row = 1, columnspan = 2)
    espacio1 = ttk.Label(frmMain).grid(column = 0, row = 2, columnspan = 2) 
    descripcion1 = ttk.Label(frmMain, text = 'La aplicación consta de generar el estándar TREE para la estructura de un trabajo.', font = 'Calibri 10 italic', justify = 'center').grid(column = 0, row = 3, columnspan = 2)
    descripcion2 = ttk.Label(frmMain, text = 'Es conveniente que tengas armado el listado de documentos para una estructura más exacta', font = 'Calibri 10 italic', justify = 'center').grid(column = 0, row = 4, columnspan = 2)

    espacio3 = ttk.Label(frmMain).grid(column = 0, row = 5, columnspan = 2) 
    espacio4 = ttk.Label(frmMain).grid(column = 0, row = 6, columnspan = 2)         
    url = ttk.Button(frmMain, text = 'https://treeingenieria.com', cursor='hand2', command = callback ).grid(column = 0, row = 7, columnspan = 2)  

    
def constructorVentana():

    from tkinter import ttk
    import tkinter as tk
    from PIL import ImageTk, Image
    import os 
    import logging
    logger = logging.getLogger('grafica.constructorVentana')  
    ventana = Tk()             #Crea la raíz
    ventana.title("Creador de proyectos")   #Título de la ventana
    ventana.resizable(0,0)     #Desactiva redimensión de la ventana
    #ventana.geometry('500x300')
    frmMain = ttk.Frame(ventana, padding = 10)     #Hijo del root
    frmCP = ttk.Frame(ventana, padding = 10)     #Hijo del root
    frmEA = ttk.Frame(ventana,padding = 10)
    frmEC = ttk.Frame(ventana,padding = 10)
    frmHelp = ttk.Frame(ventana,padding=10)
    
    def escondeFrames():
        frmMain.grid_forget()
        frmCP.grid_forget()
        frmEA.grid_forget()
        frmEC.grid_forget()
        frmHelp.grid_forget()
        
    def main():
        escondeFrames()
        frmMain.grid()
        mainGUI(frmMain)    
    
    def creaproyectos():
        escondeFrames()    
        frmCP.grid()
        creaproyectosGUI(frmCP)
    
    def editaArchivos():
        escondeFrames()    
        frmEA.grid()
        editaArchivosGUI(frmEA)
        
    def editaClientes():
        escondeFrames()    
        frmEC.grid()
        editaClientesGUI(frmEC)
        
    def instructivoAyuda():
        escondeFrames()    
        frmHelp.grid()
        instructivoAyudaGUI(frmHelp)
      
    #crea la ventana y le agrega el menú bar
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
    label='Inicio',
    command = main
) 
    file_menu.add_command(
    label='Nuevo',
    command = creaproyectos
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
    command = editaArchivos
    
)
    config_menu.add_command(
    label='Editar clientes',
    command = editaClientes
)
    menubar.add_cascade(
    label="Ayuda",
    menu=help_menu
)    
    help_menu.add_command(
    label='Instructivo',
    command = instructivoAyuda
    
)   
    main()
    ventana.mainloop()