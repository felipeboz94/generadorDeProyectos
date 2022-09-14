
def main():
    from grafica_ import constructorVentana
    import logging
    from iniciaLog import iniciaLog 
    
    iniciaLog()
    logger = logging.getLogger('main.main')
    logger.info(u'¡INICIO DE LA APLICACIÓN!')

    constructorVentana()
main()

#agregar documentos estándar
#agregar un menú para ver json de clientes, json de archivos y poder editarlos
#agregar menú de ayuda
#ahí ya sale la versión 1.0.0
