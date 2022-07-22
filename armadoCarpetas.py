from genericpath import isdir
import os

def lecturaJSON(pathJson):
    import json
    from tkinter import messagebox
    import logging
    logger = logging.getLogger('armadoCarpetas.lecturaJSON')  
    
    try:
        with open(pathJson,"r", encoding="utf-8") as j:
            diccionario = json.load(j) 
    except FileNotFoundError  as error:
        logger.error("Hubo un error al leer el archivo JSON: %s"%error)
    else:
        return diccionario
        
    
def diccionarioEsqueleto(pathJson = os.path.dirname(os.path.abspath(__file__))+'\\esqueleto.json'):
    #if not listadoDocumentos:
    dicEsqueleto = lecturaJSON(pathJson)
    
    return dicEsqueleto
    
    
    
def nroProyecto(directorio = None):
    import os 
    
    if directorio != None:
        with os.scandir(directorio) as proyectos:
            #obtengo los nombres de los archivos dentro de directorio que:
            #son directorios, tienen un guín (es decir, respetan el estándar)
            #y además se les quita un posible espacio al inicio del nombre
            proyectos = [proyecto.name.lstrip() for proyecto in proyectos if proyecto.is_dir() and proyecto.name.find('-')>-1]      #lista filtrada de los elementos dentro del directorio que son dir (carpetas)
        proyectos.sort()    #ordeno lista alfabeticamente
        if proyectos:
            ultimoProyecto = proyectos[-1]  #tomo el último nombre del proyecto
            indiceGuion = ultimoProyecto.find('-')      #busco el índice del guion que separa al estándar 'XX - Nombre del proyecto'
            ultimoProyecto = int(ultimoProyecto[:indiceGuion]) 
        else:
            #no hay proyectos
            ultimoProyecto = 0
            
        nroProyecto = ultimoProyecto + 1
    return f"{nroProyecto:02d}"    #devuelve un formato de números de dos dígitos si o si
            
def nombreArchivosCreados():
        pass

def creacionArchivos(dicArchivo):
    from os import scandir 
    import logging 
    logger = logging.getLogger('armadoCarpetas.creacionArchivos')
    archivoFullPath = ''
    if dicArchivo:
        acronimo = dicArchivo["acronimo"]
        pathArchivosDefault =  os.path.dirname(os.path.abspath(__file__)) +'\\archivosDefault'
        listadoArchivosDefault = [arch.name for arch in scandir(pathArchivosDefault) if arch.is_file() and not arch.name.startswith(u'~$')]
        for archivo in listadoArchivosDefault:
            if acronimo in archivo[:archivo.find('.')]:
                archivoFullPath = pathArchivosDefault + '\\' + archivo
    else:
        logger.error(u'No se encontró un listado de documentos de referencia para copiar')
        archivoFullPath = ''
    return archivoFullPath
    


def creacionSubFicheros(fichero, nombreCarpeta):
    import os 
    import logging 
    from shutil import copy2
    logger = logging.getLogger('armadoCarpetas.creacionSubFicheros')
    numeroSubCarpeta = 0
    for subFichero in fichero["contenido"].values():
        #print(subFichero)
        if subFichero["tipo"] == "Carpeta":
            nombreSubCarpeta = nombreCarpeta + u'%s - %s\\'%(f"{numeroSubCarpeta:02d}",subFichero["nombre"])
            try:
                os.mkdir(nombreSubCarpeta)
                logger.info('Creación de la carpeta %s'%(nombreSubCarpeta))
                #Si la subcarpeta tiene contenido, vuelve a llamar a la función para volver a crear o una carpeta dentro o un archivo
                if subFichero["contenido"]:
                    creacionSubFicheros(subFichero,nombreSubCarpeta)

                    
                numeroSubCarpeta += 1
            except OSError as error:
                logger.error('Error al generar la carpeta %s: %s'%(nombreSubCarpeta, error))
                
        if subFichero["tipo"] == "Archivo":
            logger.info('Creación de la carpeta %s'%(nombreCarpeta))
            archivoFullPath = creacionArchivos(subFichero)
            
            if archivoFullPath != '':
                copy2(archivoFullPath,nombreCarpeta)
            else:
                logger.warning('No se pudo copiar el archivo que corresponde a %s'%subFichero)



               
def creaProyectoDefault(dicEsqueleto, carpetaProyecto):
    from tkinter import messagebox
    import logging
    logger = logging.Logger('armadoCarpetas.creaProyectoDefault')
    try:
        if dicEsqueleto:
            os.mkdir(carpetaProyecto)
            numeroCarpeta = 0
            for fichero in dicEsqueleto.values():
                if fichero["tipo"] == "Carpeta":
                    nombreCarpeta = carpetaProyecto + u'%s - %s\\'%(f"{numeroCarpeta:02d}",fichero["nombre"])
                    os.mkdir(nombreCarpeta)
                    
                    creacionSubFicheros(fichero, nombreCarpeta)
                    numeroCarpeta += 1
            
            messagebox.showinfo(title="Mensaje", message="Creación exitosa")
            logger.info(u"Creación exitosa del proyecto en el path %s"%(carpetaProyecto))
    except OSError as error:
        messagebox.showerror(title="Error", message="Hubo un error al generar el proyecto: %s"%error)
        logger.error("Hubo un error al generar el proyecto: %s"%error)


  
def creacionCarpetas(nombreProyecto = None, directorio = None, listadoDocumentos = None):
    import os 
    from tkinter import messagebox    
    import logging
    from excel import lecturaExcel
    from listadoDocumentos import chequeoFormato
    logger = logging.getLogger('armadoCarpetas.creacionCarpetas')

    logger.info(u'Está por crear un proyecto')
    numeroProyecto = nroProyecto(directorio)
    carpetaProyecto = directorio +'\\%s - %s\\'%(numeroProyecto,nombreProyecto) 
    
    ##--------------------------------------------
    # ACÁ AGREGAR LÓGICA DE LECTURA DE LISTADO DE DOCUMENTOS. SI TRAE EL DICCIONARIO
    #QUE ELIGA EL PATH DEFAULT, SINO SE SELECCIONA LA OPCIÓN O SI EL LISTADO DE DOCS NO EXISTE O SE GENERA UN ERROR
    #AVISAR Y PROPONER GENERAR DEFAULT
    dicListadoDocumentos = lecturaExcel(listadoDocumentos) if listadoDocumentos else None
    pathJson = 'json\\esqueleto1.json'
    dicEsqueleto = diccionarioEsqueleto(pathJson)    
    if not dicListadoDocumentos:
        pathJson2 = 'json\\esqueleto2.json'
        dicDocGenDefault = diccionarioEsqueleto(pathJson2)
        dicEsqueleto["carpeta02"] = dicDocGenDefault["carpeta02"]
    else:
        dicEsqueleto["carpeta02"] = dicListadoDocumentos["carpeta02"]
        
    print("El diccionario esqueleto es \n \n \n %s"%dicEsqueleto)
    creaProyectoDefault(dicEsqueleto, carpetaProyecto)
        #creaProyectoDefault(dicListadoDocumentos, carpetaProyecto)
    
    #------------------------------------------    

    #creaProyectoDefault(dicListadoDocumentos, carpetaProyecto)
           


            
                    

            
            
