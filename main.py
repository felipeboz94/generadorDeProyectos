
def main():
    from grafica import mainGUI
    import logging
    from iniciaLog import iniciaLog 
    
    iniciaLog()
    logger = logging.getLogger('main.main')
    logger.info(u'¡INICIO DE LA APLICACIÓN!')

    mainGUI()
main()

#falta corregir nombres de carpetas de documentación generada
#ver lógica para armar nombres de archivos
#agregar documentos estándar
