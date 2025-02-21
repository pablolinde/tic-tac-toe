# En este programa se ejecuta el juego del tres en raya.
# En esta versión el usuario introduce las cruces y los círculos

# Inicio del programa

# Importación de bibliotecas

import numpy as np
import clips

# Funciones
##################################################################################################
# Pregunta si queremos seguir jugando
def pregunta_otra_partida():

    # Variable de control interna
    respuesta_correcta = False
    
    while (respuesta_correcta == False):
    
        respuesta = input('¿Desea jugar otra partida? (valores permitidos: S,s,Sí,si, No, n)')
        if (respuesta == 'S') | (respuesta == 's')|(respuesta == 'Sí')|(respuesta == 'sí'):
            otra_partida_respuesta = True
            respuesta_correcta = True
        elif (respuesta == 'N') | (respuesta == 'n')|(respuesta == 'No')|(respuesta == 'no'):
            otra_partida_respuesta = False
            respuesta_correcta = True
        else:
            respuesta_correcta = False

    return otra_partida_respuesta

##################################################################################################


##################################################################################################
# Pregunta si empieza el usuario (cruces) o la máquina (círculos)
def pregunta_quien_empieza():

    # Variable de control interna
    respuesta_correcta = False
    
    while (respuesta_correcta == False):
    
        respuesta =  input('¿Quién empieza: usuario (cruces) o máquina (círculos). Usuario: U, u, máquina: M, m: ')

        if (respuesta == 'U') | (respuesta == 'u'):
            usuario = True
            respuesta_correcta = True
        elif (respuesta == 'M') | (respuesta == 'm'):
            usuario = False
            respuesta_correcta = True
        else:
            respuesta_correcta = False

    return usuario

##################################################################################################

##################################################################################################
# Muestra el tablero por pantalla
def muestra_tablero(cruces, circulos):
    num_casillas_x = 3
    num_casillas_y =3
    for indice_y in range(num_casillas_x):
        print('_________________', end = '\n')
        for indice_x in range(num_casillas_y):
            # Los índices van desde 0 hasta 2
            # indice_x recorre la coordenada x, indice_y la coordenada y
            indice_arg_x = indice_x
            indice_arg_y = indice_y
            valor = esta_presente_tablero(cruces, indice_arg_x, indice_arg_y)

            dibuja_cruz_circulo = True
            dibuja_cruz =  False
            if (valor == 1):
                # Se dibuja una cruz
                dibuja_cruz = True
            else:
                valor = esta_presente_tablero(circulos, indice_arg_x, indice_arg_y)
                if (valor == 1):
                    # Se dibuja un círculo
                    dibuja_cruz = False
                else:
                    dibuja_cruz_circulo = False
            
            dibuja_casilla_tablero(dibuja_cruz_circulo, dibuja_cruz, indice_arg_x, indice_arg_y)
    print('_________________', end = '\n')    

##################################################################################################

##################################################################################################
def esta_presente_tablero(vector_matriz, numero_casilla_x, numero_casilla_y):
    #posicion_lista = [numero_casilla_x, numero_casilla_y]
    #valor = lista.count(posicion_lista)

    # numero_casilla_x: de 0 a 2
    # numero_casilla_y: de 0 a 2
    valor = vector_matriz[numero_casilla_x, numero_casilla_y]
    
    return valor
##################################################################################################

##################################################################################################
def dibuja_casilla_tablero(dibuja_cruz_circulo,dibuja_cruz,indice_x,indice_y):

    if (dibuja_cruz_circulo):
        if (dibuja_cruz):
            simbolo_dib = 'X'
        else:
            simbolo_dib = 'O'
    else:
        simbolo_dib = ' '

    if (indice_x == 2):
        print(' %s  |' %(simbolo_dib), end = '\n') 
    else:
        print(' %s  |' %(simbolo_dib), end = ' ') 

##################################################################################################

##################################################################################################
def pregunta_coordenadas_tirada(tipo):


    if tipo == 'cruces':

        # Variable de control interna
        respuesta_correcta = False

        while (respuesta_correcta == False):
        
            #print('                    ', end = '\n')
            coord_x = input('Introduzca la coordenada x de %s [Rango 0-2]: ' %tipo)
            coord_x = int(coord_x)
            if (coord_x < 0) | (coord_x > 2):
                # Respuesta fuera del rango correcto
                respuesta_correcta = False
            else:
                # Respuesta en el rango correcto
                respuesta_correcta = True

        respuesta_correcta = False
        while (respuesta_correcta == False):
        
            coord_y = input('Introduzca la coordenada y de %s [Rango 0-2]: ' %tipo)
            coord_y = int(coord_y)
            if (coord_y < 0) | (coord_y > 2):
                # Respuesta fuera del rango correcto
                respuesta_correcta = False
            else:
                # Respuesta en el rango correcto
                respuesta_correcta = True


        coordenadas = [coord_x, coord_y]
        return coordenadas
    
    else:

        coordenadas = tirada_maquina(cruces, circulos)
        return coordenadas



##################################################################################################

##################################################################################################
# Guarda en el array (matriz) de numpy las posiciones de las cruces o de los círculos
# Devuelve el array (matriz) de numpy las posiciones de las cruces o de los círculos
def guarda_en_matriz(cruces, circulos, coordenadas_tirada, jugador_cruz):

    # Coordenadas de la tirada: para ser utilizadas como índices deben estar entre 0 y 2
    coord_x = coordenadas_tirada[0]
    coord_y = coordenadas_tirada[1]

    valor_guardado_cruces = cruces[coord_x, coord_y]
    valor_guardado_circulos = circulos[coord_x, coord_y]
    if ( (valor_guardado_cruces == 1) | (valor_guardado_circulos == 1) ):
        # Ya hay una casilla con una cruz o un círculo
        tirada_correcta = False
    else:
        if (jugador_cruz):
            cruces[coord_x, coord_y] = 1
        else:
            circulos[coord_x, coord_y] = 1
        tirada_correcta = True

    return cruces, circulos, tirada_correcta
##################################################################################################

##################################################################################################
# Determina si un jugador ha ganado: en ese caso devuelve ganador cruz= Tue ganador ó circulos=True
def determina_si_ganador(vector_matriz):

    # Inicialización de valores
    ganador = False

    # Transformamos cada lista de listas en una matriz
    traza_1 = np.trace(vector_matriz)
    if (traza_1 ==3):
        ganador = True

    traza_2 = np.trace(np.fliplr(vector_matriz))
    if (traza_2 ==3):
        ganador = True

    suma_filas = np.sum(vector_matriz, axis=1)
    if (3 in suma_filas):
        ganador = True

    suma_columnas = np.sum(vector_matriz, axis=0)
    if (3 in suma_columnas):
        ganador = True
    
    return ganador

##################################################################################################

##################################################################################################

def tirada_maquina(cruces, circulos):

    sys = clips.Environment()

    template_pos_cruz = """(deftemplate pos_cruz
        (slot coord_x (type INTEGER))           
        (slot coord_y (type INTEGER))
        (slot cruz_si (type INTEGER)))"""    

    template_pos_circle = """(deftemplate pos_circle
        (slot coord_x (type INTEGER))
        (slot coord_y (type INTEGER))
        (slot circle_si (type INTEGER)))"""   
    
    template_tirada_final = """(deftemplate tirada_final
    (slot coord_x (type INTEGER))
    (slot coord_y (type INTEGER)))"""   
    
    sys.build(template_pos_cruz)
    sys.build(template_pos_circle)
    sys.build(template_tirada_final)

    template_pos_cruz = sys.find_template('pos_cruz')
    template_pos_circle= sys.find_template('pos_circle')
    template_tirada_final = sys.find_template('tirada_final')
    
    for indice_x in range(3):
        for indice_y in range(3):
            coord_x_temp = indice_x
            coord_y_temp = indice_y
            valor_cruz = int(cruces[indice_x, indice_y])
            valor_circulo = int(circulos[indice_x, indice_y])     
            f1 = template_pos_circle.assert_fact(coord_x=indice_x, coord_y=indice_y, circle_si=valor_circulo)
            f2 = template_pos_cruz.assert_fact(coord_x=indice_x, coord_y=indice_y, cruz_si=valor_cruz)
    fact = sys.assert_string('(Tira maquina si)')

    #knowledge rules

    knowledge_rule_1 = """ 
    (defrule knowledge_rule_1
    (declare (salience 100))
    (pos_circle (coord_x ?x) (coord_y ?y) (circle_si 1))
    =>
    (assert (hay_un_circulo_en_la_casilla coord_x ?x coord_y ?y))
    )
    """

    knowledge_rule_2 = """ 
    (defrule knowledge_rule_2
    (declare (salience 100))
    (pos_cruz (coord_x ?x) (coord_y ?y) (cruz_si 1))
    =>
    (assert (hay_una_cruz_en_la_casilla coord_x ?x coord_y ?y))
    )
    """

    knowledge_rule_3 = """ 
    (defrule knowledge_rule_3
    (declare (salience 100))
    (pos_circle (coord_x ?x) (coord_y ?y) (circle_si 0))
    (pos_cruz (coord_x ?x) (coord_y ?y) (cruz_si 0))
    =>
    (assert (casilla_vacia ?x ?y)) 
    )
    """

    #init rules

    init_rule_1 = """
    (defrule init_rule_1
    (declare (salience 90))
    (casilla_vacia 1 1)
    =>
    (assert (tirada_final (coord_x 1) (coord_y 1))) 
    )
    """

    init_rule_2 = """
    (defrule init_rule_2
    (declare (salience 90))
    (pos_cruz (coord_x 1) (coord_y 1) (cruz_si 1))
    (casilla_vacia 0 2)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 2))) 
    )
    """

    #fill rules

    fill_rule_row = """
    (defrule fill_rule_row
    (declare (salience 80))
    (pos_circle (coord_x ?m) (coord_y ?y) (circle_si 1))
    (pos_circle (coord_x ?n) (coord_y ?y) (circle_si 1))
    (casilla_vacia ?i ?y)
    (test (!= ?m ?n ?i))
    =>
    (assert (tirada_final (coord_x ?i) (coord_y ?y))) 
    )
    """

    fill_rule_col = """
    (defrule fill_rule_col
    (declare (salience 80))
    (pos_circle (coord_x ?x) (coord_y ?m) (circle_si 1))
    (pos_circle (coord_x ?x) (coord_y ?n) (circle_si 1))
    (casilla_vacia ?x ?i)
    (test (!= ?m ?n ?i))
    =>
    (assert (tirada_final (coord_x ?x) (coord_y ?i))) 
    )
    """

    fill_rule_diag = """
    (defrule fill_rule_diag
    (declare (salience 80))
    (pos_circle (coord_x ?m) (coord_y ?m) (circle_si 1))
    (pos_circle (coord_x ?n) (coord_y ?n) (circle_si 1))
    (casilla_vacia ?i ?i)
    (test (!= ?m ?n ?i))
    =>
    (assert (tirada_final (coord_x ?i) (coord_y ?i))) 
    )
    """

    fill_rule_diag_sec_1 = """
    (defrule fill_rule_diag_sec_1
    (declare (salience 80))
    (pos_circle (coord_x 0) (coord_y 2) (circle_si 1))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (casilla_vacia 2 0)
    =>
    (assert (tirada_final (coord_x 2) (coord_y 0))) 
    )
    """

    fill_rule_diag_sec_2 = """
    (defrule fill_rule_diag_sec_2
    (declare (salience 80))
    (pos_circle (coord_x 2) (coord_y 0) (circle_si 1))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (casilla_vacia 0 2)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 2))) 
    )
    """

    #block rules

    bloq_rule_row = """
    (defrule bloq_rule_row
    (declare (salience 70))
    (pos_cruz (coord_x ?m) (coord_y ?y) (cruz_si 1))
    (pos_cruz (coord_x ?n) (coord_y ?y) (cruz_si 1))
    (casilla_vacia ?i ?y)
    (test (!= ?m ?n ?i))
    =>
    (assert (tirada_final (coord_x ?i) (coord_y ?y))) 
    )
    """

    bloq_rule_col = """
    (defrule bloq_rule_col
    (declare (salience 70))
    (pos_cruz (coord_x ?x) (coord_y ?m) (cruz_si 1))
    (pos_cruz (coord_x ?x) (coord_y ?n) (cruz_si 1))
    (casilla_vacia ?x ?i)
    (test (!= ?m ?n ?i))
    =>
    (assert (tirada_final (coord_x ?x) (coord_y ?i))) 
    )
    """

    bloq_rule_diag = """
    (defrule bloq_rule_diag
    (declare (salience 70))
    (pos_cruz (coord_x ?m) (coord_y ?m) (cruz_si 1))
    (pos_cruz (coord_x ?n) (coord_y ?n) (cruz_si 1))
    (casilla_vacia ?i ?i)
    (test (!= ?m ?n ?i))
    =>
    (assert (tirada_final (coord_x ?i) (coord_y ?i))) 
    )
    """

    bloq_rule_diag_sec_1 = """
    (defrule bloq_rule_diag_sec_1
    (declare (salience 70))
    (pos_cruz (coord_x 0) (coord_y 2) (cruz_si 1))
    (pos_cruz (coord_x 1) (coord_y 1) (cruz_si 1))
    (casilla_vacia 2 0)
    =>
    (assert (tirada_final (coord_x 2) (coord_y 0))) 
    )
    """

    bloq_rule_diag_sec_2 = """
    (defrule bloq_rule_diag_sec_2
    (declare (salience 70))
    (pos_cruz (coord_x 2) (coord_y 0) (cruz_si 1))
    (pos_cruz (coord_x 1) (coord_y 1) (cruz_si 1))
    (casilla_vacia 0 2)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 2))) 
    )
    """

    #double attack rules 


    first_double_attack_rule_1 = """
    (defrule first_double_attack_rule_1
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_cruz (coord_x 1) (coord_y 0) (cruz_si 1))
    (casilla_vacia 0 0)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 0))) 
    )
    """

    second_double_attack_rule_1 = """
    (defrule second_double_attack_rule_1
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_circle (coord_x 0) (coord_y 0) (circle_si 1))
    (pos_cruz (coord_x 1) (coord_y 0) (cruz_si 1))
    (pos_cruz (coord_x 2) (coord_y 2) (cruz_si 1))
    (casilla_vacia 0 2)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 2))) 
    )
    """

    first_double_attack_rule_2 = """
    (defrule first_double_attack_rule_2
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_cruz (coord_x 1) (coord_y 2) (cruz_si 1))
    (casilla_vacia 2 2)
    =>
    (assert (tirada_final (coord_x 2) (coord_y 2))) 
    )
    """

    second_double_attack_rule_2 = """
    (defrule second_double_attack_rule_2
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_circle (coord_x 2) (coord_y 2) (circle_si 1))
    (pos_cruz (coord_x 1) (coord_y 2) (cruz_si 1))
    (pos_cruz (coord_x 0) (coord_y 0) (cruz_si 1))
    (casilla_vacia 2 0)
    =>
    (assert (tirada_final (coord_x 2) (coord_y 0))) 
    )
    """

    first_double_attack_rule_3 = """
    (defrule first_double_attack_rule_3
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_cruz (coord_x 0) (coord_y 1) (cruz_si 1))
    (casilla_vacia 0 0)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 0))) 
    )
    """

    second_double_attack_rule_3 = """
    (defrule second_double_attack_rule_3
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_circle (coord_x 0) (coord_y 0) (circle_si 1))
    (pos_cruz (coord_x 0) (coord_y 1) (cruz_si 1))
    (pos_cruz (coord_x 2) (coord_y 2) (cruz_si 1))
    (casilla_vacia 2 0)
    =>
    (assert (tirada_final (coord_x 2) (coord_y 0))) 
    )
    """

    first_double_attack_rule_4 = """
    (defrule first_double_attack_rule_4
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_cruz (coord_x 2) (coord_y 1) (cruz_si 1))
    (casilla_vacia 2 2)
    =>
    (assert (tirada_final (coord_x 2) (coord_y 2))) 
    )
    """

    second_double_attack_rule_4 = """
    (defrule second_double_attack_rule_4
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_circle (coord_x 2) (coord_y 2) (circle_si 1))
    (pos_cruz (coord_x 2) (coord_y 1) (cruz_si 1))
    (pos_cruz (coord_x 0) (coord_y 0) (cruz_si 1))
    (casilla_vacia 0 2)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 2))) 
    )
    """

    first_double_attack_rule_5 = """
    (defrule first_double_attack_rule_5
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_cruz (coord_x 0) (coord_y 0) (cruz_si 1))
    (casilla_vacia 2 2)
    =>
    (assert (tirada_final (coord_x 2) (coord_y 2))) 
    )
    """

    second_double_attack_rule_5a = """
    (defrule second_double_attack_rule_5a
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_circle (coord_x 2) (coord_y 2) (circle_si 1))
    (pos_cruz (coord_x 0) (coord_y 0) (cruz_si 1))
    (pos_cruz (coord_x 2) (coord_y 1) (cruz_si 1))
    (casilla_vacia 0 2)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 2))) 
    )
    """

    second_double_attack_rule_5b = """
    (defrule second_double_attack_rule_5b
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_circle (coord_x 2) (coord_y 2) (circle_si 1))
    (pos_cruz (coord_x 0) (coord_y 0) (cruz_si 1))
    (pos_cruz (coord_x 1) (coord_y 2) (cruz_si 1))
    (casilla_vacia 2 0)
    =>
    (assert (tirada_final (coord_x 2) (coord_y 0))) 
    )
    """

    first_double_attack_rule_6 = """
    (defrule first_double_attack_rule_6
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_cruz (coord_x 0) (coord_y 2) (cruz_si 1))
    (casilla_vacia 2 0)
    =>
    (assert (tirada_final (coord_x 2) (coord_y 0))) 
    )
    """

    second_double_attack_rule_6a = """
    (defrule second_double_attack_rule_6a
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_circle (coord_x 2) (coord_y 0) (circle_si 1))
    (pos_cruz (coord_x 0) (coord_y 2) (cruz_si 1))
    (pos_cruz (coord_x 1) (coord_y 0) (cruz_si 1))
    (casilla_vacia 2 2)
    =>
    (assert (tirada_final (coord_x 2) (coord_y 2))) 
    )
    """

    second_double_attack_rule_6b = """
    (defrule second_double_attack_rule_6b
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_circle (coord_x 2) (coord_y 0) (circle_si 1))
    (pos_cruz (coord_x 0) (coord_y 2) (cruz_si 1))
    (pos_cruz (coord_x 2) (coord_y 1) (cruz_si 1))
    (casilla_vacia 0 0)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 0))) 
    )
    """

    first_double_attack_rule_7 = """
    (defrule first_double_attack_rule_7
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_cruz (coord_x 2) (coord_y 2) (cruz_si 1))
    (casilla_vacia 0 0)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 0))) 
    )
    """

    second_double_attack_rule_7a = """
    (defrule second_double_attack_rule_7a
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_circle (coord_x 0) (coord_y 0) (circle_si 1))
    (pos_cruz (coord_x 2) (coord_y 2) (cruz_si 1))
    (pos_cruz (coord_x 1) (coord_y 0) (cruz_si 1))
    (casilla_vacia 0 2)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 2))) 
    )
    """

    second_double_attack_rule_7b = """
    (defrule second_double_attack_rule_7b
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_circle (coord_x 0) (coord_y 0) (circle_si 1))
    (pos_cruz (coord_x 2) (coord_y 2) (cruz_si 1))
    (pos_cruz (coord_x 0) (coord_y 1) (cruz_si 1))
    (casilla_vacia 2 0)
    =>
    (assert (tirada_final (coord_x 2) (coord_y 0))) 
    )
    """

    first_double_attack_rule_8 = """
    (defrule first_double_attack_rule_8
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_cruz (coord_x 2) (coord_y 0) (cruz_si 1))
    (casilla_vacia 0 2)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 2))) 
    )
    """

    second_double_attack_rule_8a = """
    (defrule second_double_attack_rule_8a
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_circle (coord_x 0) (coord_y 2) (circle_si 1))
    (pos_cruz (coord_x 2) (coord_y 0) (cruz_si 1))
    (pos_cruz (coord_x 0) (coord_y 1) (cruz_si 1))
    (casilla_vacia 2 2)
    =>
    (assert (tirada_final (coord_x 2) (coord_y 2))) 
    )
    """

    second_double_attack_rule_8b = """
    (defrule second_double_attack_rule_8b
    (declare (salience 60))
    (pos_circle (coord_x 1) (coord_y 1) (circle_si 1))
    (pos_circle (coord_x 0) (coord_y 2) (circle_si 1))
    (pos_cruz (coord_x 2) (coord_y 0) (cruz_si 1))
    (pos_cruz (coord_x 1) (coord_y 2) (cruz_si 1))
    (casilla_vacia 0 0)
    =>
    (assert (tirada_final (coord_x 0) (coord_y 0))) 
    )
    """

    #random rule

    random_rule = """
    (defrule random_rule
    (declare (salience 10))
    (casilla_vacia ?x ?y)
    =>
    (assert (tirada_final (coord_x ?x) (coord_y ?y))) 
    )
    """

    sys.build(knowledge_rule_1)
    sys.build(knowledge_rule_2)
    sys.build(knowledge_rule_3)

    sys.build(init_rule_1)
    sys.build(init_rule_2)

    sys.build(fill_rule_row)
    sys.build(fill_rule_col)
    sys.build(fill_rule_diag)
    sys.build(fill_rule_diag_sec_1)
    sys.build(fill_rule_diag_sec_2)

    sys.build(bloq_rule_row)
    sys.build(bloq_rule_col)
    sys.build(bloq_rule_diag)
    sys.build(bloq_rule_diag_sec_1)
    sys.build(bloq_rule_diag_sec_2)

    sys.build(first_double_attack_rule_1)
    sys.build(second_double_attack_rule_1)
    sys.build(first_double_attack_rule_2)
    sys.build(second_double_attack_rule_2)
    sys.build(first_double_attack_rule_3)
    sys.build(second_double_attack_rule_3)
    sys.build(first_double_attack_rule_4)
    sys.build(second_double_attack_rule_4)
    sys.build(first_double_attack_rule_5)
    sys.build(second_double_attack_rule_5a)
    sys.build(second_double_attack_rule_5b)
    sys.build(first_double_attack_rule_6)
    sys.build(second_double_attack_rule_6a)
    sys.build(second_double_attack_rule_6b)
    sys.build(first_double_attack_rule_7)
    sys.build(second_double_attack_rule_7a)
    sys.build(second_double_attack_rule_7b)
    sys.build(first_double_attack_rule_8)
    sys.build(second_double_attack_rule_8a)
    sys.build(second_double_attack_rule_8b)

    sys.build(random_rule)

    sys.run()

    for f in sys.facts():
        print('Indice fact', f.index,':',f)
        if (f.template.name == 'tirada_final'):
            tir_1 = f['coord_x'] 
            tir_2 = f['coord_y']
            tirada = [tir_1, tir_2]
            input(' ') 
            return tirada


##################################################################################################

##################################################################################################
# Variable de control
otra_partida = True  # Controla si deseamos seguir jugando


while (otra_partida):

    # Variable de control
    fin_partida = False  # Controla si lapartida ha finalizado: bien porque 
                     # un jugador gana, bien porque no se pueda tirar más veces

    print('=========================================')
    print('Empezamos el juego')
    print('Las casillas se indican según coordenadas [x,y]')
    print('La posición superior izquierda es [0,0]')
    print('La posición inferior derecha es [2,2]')
    print('=========================================')

    usuario = pregunta_quien_empieza()

    # Inicialización de las posiciones donde hay cruces y círculos
    # Son arrays de numpy de 3 x 3 = matrices. Un uno en una posición 
    # indicará que hay una cruz o un círculo
    cruces = np.zeros(9, dtype=int).reshape(3, 3)
    circulos = np.zeros(9, dtype=int).reshape(3, 3)

    if (usuario == True):
        jugador_cruz = True
    else:
        jugador_cruz = False

    # Cuando num_tiradas es 9 y ninguno ha ganado entonces se ha llegado a un empate
    num_tiradas = 0
    empate = False

    while (fin_partida == False):

        if (jugador_cruz == True):
            tipo = 'cruces'
        else:
            tipo = 'circulos'

        if (num_tiradas == 9):
            empate = True
            fin_partida = True
            print('La partida ha terminado en empate')

        if (empate == False):
            
            # Se desarrolla la partida
            coordenadas_tirada = pregunta_coordenadas_tirada(tipo)

            print(coordenadas_tirada)

            resultado = guarda_en_matriz(cruces, circulos, coordenadas_tirada, jugador_cruz)
            cruces = resultado[0]    # Si la tirada no es correcta cruces no ha cambiado
            circulos = resultado[1]  # Si la tirada no es correcta cruces no ha cambiado
            tirada_correcta = resultado[2]
            
            print(tirada_correcta)

            if (tirada_correcta):

                 # Aumentamos el contador de tiradas
                num_tiradas += 1

                # Tirada correcta
                muestra_tablero(cruces, circulos)

                if (jugador_cruz == True):
                    # Determinamos si hay un ganadar
                    fin_partida = determina_si_ganador(cruces)
                    if (fin_partida):
                        print('El jugador de las cruces ha ganado')
                    jugador_cruz = False
                else:
                    fin_partida = determina_si_ganador(circulos)
                    if (fin_partida):
                        print('El jugador de los circulos ha ganado')
                    
                    jugador_cruz = True

            else:
                # Tirada no correcta
                print('La casilla ya está ocupada')

    otra_partida = pregunta_otra_partida()