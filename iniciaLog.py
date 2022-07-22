def iniciaLog():
    import logging
    
    logging.basicConfig(filename='creadorDeProyectos.log', filemode = 'a', encoding='utf-8', level = logging.DEBUG , format = '%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    