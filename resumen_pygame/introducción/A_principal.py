#MAIN:

import pygame
import B_constantes as constantes
from C_personajes import Personajes #as en este caso renombraria la clase(lo que hace es renombrar lo que importamos)
from D_armas import Weapon
from E_texto import Damage_text
from F_items import Item
import os

pygame.init()
ventana = pygame.display.set_mode((constantes.ANCHO,constantes.ALTO))#tiene que ir con doble parentesis

def escalar_img(imagen,ancho,alto):
    imagen_escalada = pygame.transform.scale(imagen, (ancho,alto))
    return imagen_escalada
#esto no escala una imagen la forma correcta es:
# def escalar_img(imagen,scala):
#     ancho = int(imagen.get_width()*scala)
#     alto = int(imagen.get_height()*scala)
#     imagen_escalada = pygame.transform.scale(imagen,(ancho,alto))
#     return  imagen_escalada

animaciones = []
for i in range(2):
    img = pygame.image.load(f"C:/Users/gabri/OneDrive/Desktop/ALE/python=ale/resumen_pygame/introducción/imagenes/personaje/player_{i}.png").convert_alpha()
    img = escalar_img(img,constantes.ANCHO_PERSONAJE,constantes.ALTO_PERSONAJE)
    animaciones.append(img)

#funcion para contar elementos
def Contar(directorio):
    return len(os.listdir(directorio))
#print(Contar("C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ale\\resumen_pygame\\introducción\\imagenes\\enemigo"))

#funcion listar nombres de elementos
def Nombre(directorio):
    return os.listdir(directorio)

#enemigos
dirrectorio_enegigos = r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ale\\resumen_pygame\\introducción\\imagenes\\enemigo"
tipos_enemigos = Nombre(dirrectorio_enegigos)
animaciones_enemigos = []

for eni in tipos_enemigos:
    lista_temp = []
    ruta_temp = f"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ale\\resumen_pygame\\introducción\\imagenes\\enemigo\\{eni}"
    num_animaciones = Contar(ruta_temp)
    for i in range(num_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temp}\\{i+1}.png").convert_alpha()
        img_enemigo = escalar_img(img_enemigo,constantes.ANCHO_ENEMIGOS,constantes.ALTO_ENEMIGOS)
        lista_temp.append(img_enemigo)
    animaciones_enemigos.append(lista_temp)
    
#creando al jugador de la clase personaje
player =  Personajes(50, 50, animaciones,constantes.VIDA_PERSONAJE)#son las coordenadas

#crear un enemigo de la clase personaje
Espinaria = Personajes(400,300,animaciones_enemigos[0],constantes.VIDA_ESPINARIA)#estoy llamando a una lista que esta adentro de otra lista
Esporador = Personajes(200,200,animaciones_enemigos[1],constantes.VIDA_ESPORADOR)
Espinaria_2 = Personajes(100,250,animaciones_enemigos[0],constantes.VIDA_ESPINARIA)

#creando una lista de enemigos
lista_enemigos = []
lista_enemigos.append(Espinaria)
lista_enemigos.append(Esporador)
lista_enemigos.append(Espinaria_2)
#print(lista_enemigos)

#imagenes arco
img_arco = pygame.image.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ALE\\resumen_pygame\\introducción\\imagenes\\armas\\arco.png").convert_alpha()
img_arco_escalado = escalar_img(img_arco, constantes.ANCHO_ARMA, constantes.ALTO_ARMA)

#imagenes de la balas
img_balas = pygame.image.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ALE\\resumen_pygame\\introducción\\imagenes\\armas\\flecha.png").convert_alpha()
img_balas_escalado = escalar_img(img_balas, 35, 16)

#creando un arma de la clase weapon
arco = Weapon(img_arco_escalado,img_balas_escalado)

#carga imagenes de los items
pocion = pygame.image.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ALE\\resumen_pygame\\introducción\\items\\posion.png").convert_alpha()
pocion = escalar_img(pocion,constantes.ANCHO_POCION,constantes.ALTO_POCION)

monedas_images = []
ruta_monedas = r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ALE\\resumen_pygame\\introducción\\items\\moneda_"
num_monedas = 4
for i in range(num_monedas):
    img = pygame.image.load(fr"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ALE\\resumen_pygame\\introducción\\items\\moneda_{i}.png").convert_alpha()
    img = escalar_img(img,constantes.ANCHO_MONEDAS,constantes.ALTO_MONEDAS)
    monedas_images.append(img)
    
#cambiando el nombre del juego
pygame.display.set_caption("1°game")

#fuentes
font = pygame.font.Font(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ALE\\resumen_pygame\\introducción\\imagenes\\fuente.ttf", 22)#el segundo valor es el tamaño
font_coins = pygame.font.Font(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ALE\\resumen_pygame\\introducción\\imagenes\\fuente.ttf", 18)
#creando un grupo de sprites
grupo_damage_text = pygame.sprite.Group()
grupo_balas = pygame.sprite.Group()
grupo_items = pygame.sprite.Group()

#objeto items
moneda = Item(100,100,0,monedas_images)
pocion = Item(150,150,1,[pocion])

grupo_items.add(pocion)
grupo_items.add(moneda)
#corazones
corazon_lleno = pygame.image.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ALE\\resumen_pygame\\introducción\\items\\corazon_lleno.png").convert_alpha()
corazon_lleno = escalar_img(corazon_lleno,constantes.ANCHO_CORAZONES,constantes.ALTO_CORAZONES)
corazon_medio = pygame.image.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ALE\\resumen_pygame\\introducción\\items\\corazon_medio.png").convert_alpha()
corazon_medio = escalar_img(corazon_medio,constantes.ANCHO_CORAZONES,constantes.ALTO_CORAZONES)
corazon_vacio = pygame.image.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python=ALE\\resumen_pygame\\introducción\\items\\corazon_vacio.png").convert_alpha()
corazon_vacio = escalar_img(corazon_vacio,constantes.ANCHO_CORAZONES,constantes.ALTO_CORAZONES)

def dibujar_texto(texto,font,color,x,y):
    img = font.render(texto,True,color)
    ventana.blit(img,(x,y))
    
def Vida_player():
    c_medio = False
    for i in range(3):
        if player.vida >= ((i+1)*100):
            ventana.blit(corazon_lleno,(5+i*25,5))
        elif player.vida % 100 >0  and not c_medio:
            ventana.blit(corazon_medio,(5+i*25,5))
            c_medio = True
        else:
            ventana.blit(corazon_vacio,(5+i*25,5))
            
#definir las variables de movimiento
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#controlar el frame rate(FPS)
reloj = pygame.time.Clock()
#haciendo que no se cierre la ventana automaticamente
run = True
while run:
    #que vaya a 60 FPS
    reloj.tick(constantes.FPS)
    #cambiando el color del fondo
    ventana.fill(constantes.COLOR_BG)
    #calcular el movimiento del jugador
    delta_x = 0
    delta_y = 0
    #en python es al reves los ejes
    if mover_arriba:
        delta_y -= constantes.VELOCIDAD_PERSONAJE
    if mover_abajo:
        delta_y += constantes.VELOCIDAD_PERSONAJE
    if mover_izquierda:
        delta_x -= constantes.VELOCIDAD_PERSONAJE
    if mover_derecha:
        delta_x += constantes.VELOCIDAD_PERSONAJE
    #funciones del jugador
    #mover al jugador
    player.movimiento(delta_x,delta_y)
    #dibujar al jugador
    
    player.draw(ventana)
    #actualizando al jugador
    
    player.update()
    #funciones del enemigo
    #actualizar a los enemigos
    for ene in lista_enemigos:
        ene.update()
        #print(ene.vida)
    #dibujar a los enemigo
    for ene in lista_enemigos:
        ene.draw(ventana)
    
    for event in pygame.event.get():
        #para cerrar el juego
        if event.type == pygame.QUIT:#alt f4 o tocar la equis son eventos de quit
            run = False
        #reconoce las tecla del teclado 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            #para cuando se suelta las teclas
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False

    #dibujar el arma
    arco.draw(ventana)  
    #actualiza el estado del arma
    bala = arco.update(player)
    if bala:
        grupo_balas.add(bala)
    #dibujar balas
    for bala in grupo_balas:
        bala.Draw_b(ventana)
        dano,posicion_dano = bala.update_b(lista_enemigos)
        #print(grupo_balas)
        if dano:
            damage_text = Damage_text(posicion_dano.centerx ,posicion_dano.centery , str(dano), font ,constantes.COLOR_DAMAGE)
            grupo_damage_text.add(damage_text)
    #actualizar daño
    grupo_damage_text.update()
    
    #dibujar texto
    grupo_damage_text.draw(ventana)
    
    #dibujar los corazones
    Vida_player()
    
    #dibujar monedas
    dibujar_texto(f"coins: {player.monedas}",font_coins,constantes.COLOR_COINS,85,3)
    #actualizar items
    grupo_items.update(player)
    
    #dibujar items
    grupo_items.draw(ventana)
    pygame.display.update()
    #update():se usa para actualizar la pantalla con cualquier cambio realizado en los elementos gráficos
pygame.quit()
#linea 180:)