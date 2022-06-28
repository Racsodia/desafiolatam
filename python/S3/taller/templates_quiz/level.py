def choose_level(n_pregunta, p_level):
    
    # Construir lógica para escoger el nivel
    ##################################################
    if  p_level== 1:
        if n_pregunta == 1:
            return ("basicas")
        elif n_pregunta==2:
            return ("intermedias")
        elif n_pregunta==3:
            return ("avanzadas")
    if p_level==2:
        if n_pregunta ==1:
            return ("basicas")
        elif n_pregunta ==2:
            return ("basicas")
        elif n_pregunta ==3:
            return ("intermedias")
        elif n_pregunta ==4:
            return ("intermedias")
        elif n_pregunta==5:
            return ("avanzadas")
        elif n_pregunta==6:
            return ("avanzadas")
    if p_level==3:
        if n_pregunta ==1:
            return ("basicas")
        elif n_pregunta ==2:
            return ("basicas")
        elif n_pregunta ==3:
            return ("basicas")
        elif n_pregunta ==4:
            return ("intermedias")
        elif n_pregunta==5:
            return ("intermedias")
        elif n_pregunta==6:
            return ("intermedias")
        elif n_pregunta ==7:
            return ("avanzadas")
        elif n_pregunta==8:
            return ("avanzadas")
        elif n_pregunta==9:
            return ("avanzadas")
    
    
    ##################################################
    
if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # basicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 3)) # avanzadas
    print(choose_level(4, 3)) # intermedias