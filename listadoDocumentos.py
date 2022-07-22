
def chequeoFormato(diccionario = None):
    import re
    import logging
    logger = logging.Logger('listadoDocumentos.chequeoFormato')

    #las llaves {x,y} indica x el mínimo número de caracteres permitidos e y el máximo
    formato = '.{3,4}-.{2,3}-.{2,2}-.{2,2}-.{4,4}-.{2,4}-.{3,3}' 
    reg = re.compile(formato)
    documentosNoFormateados = []
    try:
        for documento in diccionario:
            nroDoc = diccionario[documento]["numero"]
            titulo = diccionario[documento]["titulo"]
            
            if nroDoc == None:
                nroDoc = ""
            if reg.match(nroDoc) is None:
                logger.warning("El documento %s - %s no coincide con el formato Tree"%(nroDoc, titulo))  
                documentosNoFormateados.append(documento)
    except:
        logger.error("No hay un diccionario que chequear")
        
    return documentosNoFormateados
                
     
def armadoEsqueletoDocGenerada(diccionario = None):
    import re
    import logging
    logger = logging.Logger('listadoDocumentos.armadoEsqueletoDocGenerada')
    diccionario = {1: {'titulo': 'Listado de documentos', 'numero': 'LDC-PR-22-02-0201-LD-001', 'formato': None}, 2: {'titulo': 'Memoria de relevamiento de cargas', 'numero': 'LDC-PR-22-02-0202-MC-001', 'formato': None}, 3: {'titulo': 'Memoria de dimensionamiento de paneles y disposición', 'numero': 'LDC-PR-22-02-0202-MC-002', 'formato': None}, 4: {'titulo': 'Memoria de dimensionamiento de inversores: distintos casos, incluir baterías', 'numero': 'LDC-PR-22-02-0202-MC-003', 'formato': None}, 5: {'titulo': 'Memoria de cálculo de conductores', 'numero': 'LDC-PR-22-02-0202-MC-004', 'formato': None}, 6: {'titulo': 'Memoria de cálculo de protecciones', 'numero': 'LDC-PR-22-02-0202-MC-005', 'formato': None}, 7: {'titulo': 'Típico de montaje de paneles', 'numero': 'LDC-PR-22-02-0203-TM-001', 'formato': None}, 8: {'titulo': 'Esquema unifilar general', 'numero': 'LDC-PR-22-02-0204-EE-001', 'formato': None}, 9: {'titulo': 'Topográfico y unifilar de tablero de Administración', 'numero': 'LDC-PR-22-02-0204-EE-002', 'formato': None}, 10: {'titulo': None, 'numero': None, 'formato': None}, 11: {'titulo': 'Topográficos y unifilar de tablero de campo ', 'numero': 'LDC-PR-22-02-0204-EE-004', 'formato': None}, 12: {'titulo': 'Topográfico y unifilar de tablero nuevo (si hace falta)', 'numero': 'LDC-PR-22-02-0204-EE-005', 'formato': None}, 13: {'titulo': 'Listado de conductores', 'numero': 'LDC-PR-22-02-0205-LC-001', 'formato': None}, 14: {'titulo': 'Listado de materiales y equipos', 'numero': 'LDC-PR-22-02-0206-LM-001', 'formato': None}, 15: {'titulo': 'Layout de canalizaciones', 'numero': 'LDC-PR-22-02-0207-CA-001', 'formato': None}, 16: {'titulo': 'Típico de canalizaciones y  cámaras subterráneas desde paneles a tablero ', 'numero': 'LDC-PR-22-02-0207-CA-002', 'formato': None}, 17: {'titulo': 'Informe de procedimientos a realizar frente a EPE-CAMMESA', 'numero': 'LDC-PR-22-02-0208-INF-001', 'formato': None}, 18: {'titulo': 'Informe de factibilidad ambiental', 'numero': 'LDC-PR-22-02-0208-INF-002', 'formato': None}, 19: {'titulo': 'Análisis de factibilidad técnica-económica', 'numero': 'LDC-PR-22-02-0208-INF-003', 'formato': None}, 20: {'titulo': 'Pliego de especificaciones técnicas (tener en cuenta la obra civil para hacer el cable subterráneo y las cámaras)', 'numero': 'LDC-PR-22-02-0209-PET-001', 'formato': None}}
    documentosNoFormateados = chequeoFormato(diccionario)
    print(documentosNoFormateados)
    try:
        for documento in diccionario:
            nroDoc = diccionario[documento]["numero"]
            titulo = diccionario[documento]["titulo"]
            formato = diccionario[documento]["formato"]
            segmentos = re.split('-',nroDoc)    #parte el numero
            listaSubCarpetas = []
            if nroDoc not in listaSubCarpetas:
                listaSubCarpetas.append(nroDoc)
            
            print(nroDoc)
            print(segmentos)
            print(titulo)
            print(formato)
            
    except:
        logger.error("No hay un diccionario que chequear")
        