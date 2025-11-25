#MAIN:
import pygame
import B_constantes as constantes
from C_personajes import Personajes #as en este caso renombraria la clase(lo que hace es renombrar lo que importamos)
from D_armas import Weapon
from E_texto import Damage_text
from G_mundo import Mundo
import os

pygame.init()
pygame.mixer.init()
ventana = pygame.display.set_mode((constantes.ANCHO,constantes.ALTO))#tiene que ir con doble parentesis
#cambiando el nombre del juego
pygame.display.set_caption("1°game")

def escalar_img(imagen,ancho,alto):
    imagen_escalada = pygame.transform.scale(imagen, (ancho,alto))
    return imagen_escalada
#esto escala una imagen la forma correcta es:
# def escalar_img(imagen,scala):
#     ancho = int(imagen.get_width()*scala)
#     alto = int(imagen.get_height()*scala)
#     imagen_escalada = pygame.transform.scale(imagen,(ancho,alto))
#     return  imagen_escalada

animaciones = []
for i in range(2):
    img = pygame.image.load(f"C:/Users/gabri/OneDrive/Desktop/ALE/python-ale/resumen_pygame/introducción/imagenes/personaje/player_{i}.png").convert_alpha()
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
dirrectorio_enegigos = r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ale\\resumen_pygame\\introducción\\imagenes\\enemigo"
tipos_enemigos = Nombre(dirrectorio_enegigos)
animaciones_enemigos = []

for eni in tipos_enemigos:
    lista_temp = []
    ruta_temp = f"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ale\\resumen_pygame\\introducción\\imagenes\\enemigo\\{eni}"
    num_animaciones = Contar(ruta_temp)
    for i in range(num_animaciones):
        img_enemigo = pygame.image.load(f"{ruta_temp}\\{i+1}.png").convert_alpha()
        img_enemigo = escalar_img(img_enemigo,constantes.ANCHO_ENEMIGOS,constantes.ALTO_ENEMIGOS)
        lista_temp.append(img_enemigo)
    animaciones_enemigos.append(lista_temp)

def Draw_grid():
    for i in range(16):
        # verticales
        pygame.draw.line(ventana,constantes.COLOR_LINE,(i*constantes.TILE_SIZE,0),(i*constantes.TILE_SIZE,constantes.ALTO))
        # horizontales
        pygame.draw.line(ventana,constantes.COLOR_LINE,(0,i*constantes.TILE_SIZE),(constantes.ANCHO,i*constantes.TILE_SIZE))

#creando al jugador de la clase personaje
player =  Personajes(constantes.SPAWN_NIVEL_0[0], constantes.SPAWN_NIVEL_0[1], animaciones,constantes.VIDA_PERSONAJE,1,constantes.ANCHO_PERSONAJE,constantes.ALTO_PERSONAJE)# son las coordenadas
#imagenes arco
img_arco = pygame.image.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\imagenes\\armas\\arco.png").convert_alpha()
img_arco_escalado = escalar_img(img_arco, constantes.ANCHO_ARMA, constantes.ALTO_ARMA)

#imagenes de la balas
img_balas = pygame.image.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\imagenes\\armas\\flecha.png").convert_alpha()
img_balas_escalado = escalar_img(img_balas, 35, 16)

#creando un arma de la clase weapon
arco = Weapon(img_arco_escalado,img_balas_escalado)

#carga imagenes de los items
pocion = pygame.image.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\items\\posion.png").convert_alpha()
pocion = escalar_img(pocion,constantes.ANCHO_POCION,constantes.ALTO_POCION)

monedas_images = []
ruta_monedas = r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\items\\moneda_"
num_monedas = 4
for i in range(num_monedas):
    img = pygame.image.load(fr"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\items\\moneda_{i}.png").convert_alpha()
    img = escalar_img(img,constantes.ANCHO_MONEDAS,constantes.ALTO_MONEDAS)
    monedas_images.append(img)

#fuentes
font = pygame.font.Font(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\imagenes\\fuente.ttf", 22)#el segundo valor es el tamaño
font_coins = pygame.font.Font(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\imagenes\\fuente.ttf", 18)
font_game_over = pygame.font.Font(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\imagenes\\fuente.ttf", 100)
font_reset = pygame.font.Font(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\imagenes\\fuente.ttf", 75)
font_sonido = pygame.font.Font(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\imagenes\\fuente.ttf", 25)
text_game_over = font_game_over.render("game over",True,constantes.COLOR_GAME_OVER)
text_reset = font_reset.render("reset",True,constantes.COLOR_BLANCO)
text_game = font_reset.render("play",True,constantes.COLOR_COINS)
text_exit = font_reset.render("exit",True,constantes.COLOR_COINS)
text_sonido = font_sonido.render("sonido True",True,constantes.COLOR_COINS)
text_you_won = font_game_over.render("you won",True,constantes.COLOR_COINS)
# bts the game
text_game_rect = text_game.get_rect(center=(constantes.ANCHO/2,constantes.ALTO/2))
text_exit_rect = text_exit.get_rect(center=(constantes.ANCHO/2,int(constantes.ALTO/4*3)))
text_sonido_rect = text_sonido.get_rect(center=(700,575))
def Ajustes():
    ventana.fill(constantes.COLOR_BG)
    dibujar_texto("mi primer juego",font_game_over,constantes.COLOR_DAMAGE,constantes.ANCHO/2,constantes.ALTO/2-150)
    btn_game_rect = pygame.draw.rect(ventana,constantes.COLOR_DAMAGE,(text_game_rect.left-10,text_game_rect.top,text_game_rect.width+20,text_game_rect.height))
    btn_exit_rect = pygame.draw.rect(ventana,constantes.COLOR_DAMAGE,(text_exit_rect.left-10,text_exit_rect.top,text_exit_rect.width+20,text_exit_rect.height))
    btn_sonido_rect = pygame.draw.rect(ventana,constantes.COLOR_DAMAGE,(text_sonido_rect.left-10,text_sonido_rect.top,text_sonido_rect.width+20,text_sonido_rect.height))
    ventana.blit(text_exit,text_exit_rect)
    ventana.blit(text_game,text_game_rect)
    ventana.blit(text_sonido,text_sonido_rect)# TypeErro
    pygame.display.update()
    return btn_game_rect ,btn_exit_rect ,btn_sonido_rect
#creando un grupo de sprites
grupo_damage_text = pygame.sprite.Group()
grupo_balas = pygame.sprite.Group()
#corazones
corazon_lleno = pygame.image.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\items\\corazon_lleno.png").convert_alpha()
corazon_lleno = escalar_img(corazon_lleno,constantes.ANCHO_CORAZONES,constantes.ALTO_CORAZONES)
corazon_medio = pygame.image.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\items\\corazon_medio.png").convert_alpha()
corazon_medio = escalar_img(corazon_medio,constantes.ANCHO_CORAZONES,constantes.ALTO_CORAZONES)
corazon_vacio = pygame.image.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\items\\corazon_vacio.png").convert_alpha()
corazon_vacio = escalar_img(corazon_vacio,constantes.ANCHO_CORAZONES,constantes.ALTO_CORAZONES)

def dibujar_texto(texto, font, color, x, y):
    superficie_texto = font.render(texto, True, color)
    ventana.blit(superficie_texto, superficie_texto.get_rect(center=(x, y)))
def Vida_player():
    c_medio = False
    for i in range(3):
        if player.vida >= ((i+1)*100):
            ventana.blit(corazon_lleno,(5+i*25,7))
        elif player.vida % 100 >0  and not c_medio:
            ventana.blit(corazon_medio,(5+i*25,7))
            c_medio = True
        else:
            ventana.blit(corazon_vacio,(5+i*25,7))
list_tiles = []
for i in range(Contar(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\tiles")):
    imagen = pygame.image.load(fr"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ALE\\resumen_pygame\\introducción\\tiles\\{i}.png")
    imagen = pygame.transform.scale(imagen,(constantes.TILE_SIZE,constantes.TILE_SIZE))
    list_tiles.append(imagen)
# creando un objeto Mundo
mundo = Mundo()
nivel = 0
mundo.Process_list(list_tiles,nivel,32,(monedas_images,[pocion]),animaciones_enemigos)

grupo_items = pygame.sprite.Group()
for items in mundo.list_items:
    grupo_items.add(items)
# controlar el frame rate(FPS)
reloj = pygame.time.Clock()
# pygame.mixer.music está pensado para música larga o de fondo, 
# y solo puede manejar una pista a la vez.
pygame.mixer.music.load(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ale\\resumen_pygame\\introducción\\sonidos\\ambiente.mp3")
# Reproducir música (loop=0 significa una vez, -1 significa infinito)
pygame.mixer.music.play(loops=-1)
# pygame.mixer.Sound() → crea un objeto de sonido a partir de un archivo.
sonido_pasos = pygame.mixer.Sound(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ale\\resumen_pygame\\introducción\\sonidos\\pasos.mp3")
sonido_puertas = pygame.mixer.Sound(r"C:\\Users\\gabri\\OneDrive\\Desktop\\ALE\\python-ale\\resumen_pygame\\introducción\\sonidos\\puertas.mp3")
sonido_puertas.set_volume(0.50)# 1 = 100%
# A diferencia de la música, los efectos de sonido pueden reproducirse varias veces y 
# en paralelo (por ejemplo, pasos + puertas al mismo tiempo).
# pygame.mixer.music → para música de fondo (solo una pista activa).
# pygame.mixer.Sound → para efectos cortos (pueden sonar simultáneamente).

# haciendo que no se cierre la ventana automaticamente
running = True
ajustes = True
sonido = True
juego_terminado = False
canal_pasos = pygame.mixer.Channel(0)
while running:
    if sonido:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
            sonido_fondo = True
        sonido_puertas.set_volume(0.25)
        sonido_pasos.set_volume(1.0)
        pygame.mixer.music.set_volume(0.5)
    else:
        sonido_puertas.stop()
        sonido_pasos.stop()
        pygame.mixer.music.stop()
        sonido_fondo = False
    if ajustes:
        text_sonido = font_sonido.render(f"sonido {sonido}",True,constantes.COLOR_COINS)
        btn_game_rect, btn_exit_rect, btn_sonido_rect = Ajustes()
        for event in pygame.event.get():
            event_type = event.type
            if event_type == pygame.QUIT:
                running = False
            elif event_type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and btn_game_rect.collidepoint(event.pos):
                    ajustes = False
                    mover_arriba = False
                    mover_abajo = False
                    mover_izquierda = False
                    mover_derecha = False
                if event.button == 1 and btn_exit_rect.collidepoint(event.pos):
                    running = False
                if event.button == 1 and btn_sonido_rect.collidepoint(event.pos):
                    sonido = not sonido
            elif event_type == pygame.KEYDOWN:
                if event.key ==  pygame.K_ESCAPE:
                    ajustes = False
                    mover_arriba = False
                    mover_abajo = False
                    mover_izquierda = False
                    mover_derecha = False
    else:
        # que vaya a 60 FPS
        reloj.tick(constantes.FPS)
        # fondo
        ventana.fill(constantes.COLOR_BG)
        mundo.Dibujar_mapa(ventana)
        #dibujar items
        grupo_items.draw(ventana)
        #dibujar texto
        grupo_damage_text.draw(ventana)
        #dibujar los corazones
        Vida_player()
        #dibujar el arma
        arco.draw(ventana)
        for ene in mundo.list_enemigos:
            ene.Draw(ventana)
        #dibujar al jugador
        player.Draw(ventana)
        #dibujar monedas y nivel
        dibujar_texto(f"coins: {player.monedas}",font_coins,constantes.COLOR_COINS,115,15)
        dibujar_texto(f"nivel {nivel+1}",font_coins,constantes.COLOR_BLANCO,constantes.ANCHO / 2,15)
        for event in pygame.event.get():
                #para cerrar el juego
                event_type = event.type
                if event_type == pygame.QUIT:#alt f4 o tocar la equis son eventos de quit
                    running = False
                #reconoce las tecla del teclado 
                elif event_type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        mover_arriba = True
                    if event.key == pygame.K_s:
                        mover_abajo = True
                    if event.key == pygame.K_a:
                        mover_izquierda = True
                    if event.key == pygame.K_d:
                        mover_derecha = True
                    if event.key ==  pygame.K_ESCAPE:
                        ajustes = True
                elif event_type == pygame.MOUSEBUTTONDOWN:
                    if player.vida == 0 or juego_terminado:
                        #collidepoint(event.pos) es la forma más directa de saber si el mouse 
                        # está sobre un rectángulo en Pygame.
                        if event.button == 1 and reset_rect.collidepoint(event.pos):
                            player.vida = constantes.VIDA_PERSONAJE
                            player.monedas = 0
                            player.shape.center = constantes.SPAWN_NIVEL_0
                            nivel = 0
                            juego_terminado = False
                            mundo.Reset_world((grupo_damage_text,grupo_balas,grupo_items))
                            mundo.Process_list(list_tiles,nivel,32,(monedas_images,[pocion]),animaciones_enemigos)
                            for items in mundo.list_items:
                                grupo_items.add(items)
                    elif event.button == 3: 
                        mundo.Cambiar_puerta(player)
                        if sonido:
                            sonido_puertas.play()
                    # 1 → Botón izquierdo
                    # 2 → Botón del medio (rueda)
                    # 3 → Botón derecho
                    # 4 → Scroll arriba
                    # 5 → Scroll abajo
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
        if sonido:
            if (mover_izquierda or mover_derecha or mover_arriba or mover_abajo):
                if not canal_pasos.get_busy():
                    canal_pasos.play(sonido_pasos)
            else:
                sonido_pasos.stop()
        if juego_terminado:
            text_you_won_rect = text_you_won.get_rect(center=(constantes.ANCHO/2,(constantes.ALTO/2)-150))
            ventana.blit(text_you_won,text_you_won_rect)
            text_reset_rect = text_reset.get_rect(center=(constantes.ANCHO/2,constantes.ALTO/3*2))
            reset_rect = pygame.draw.rect(ventana,constantes.COLOR_GAME_OVER,text_reset_rect)
            ventana.blit(text_reset,text_reset_rect)
        else:
            if player.vida != 0:
                # calcular el movimiento del jugador
                delta_x = 0
                delta_y = 0
                # en python es al reves los ejes
                if mover_arriba:
                    delta_y -= constantes.VELOCIDAD_PERSONAJE
                if mover_abajo:
                    delta_y += constantes.VELOCIDAD_PERSONAJE
                if mover_izquierda:
                    delta_x -= constantes.VELOCIDAD_PERSONAJE
                if mover_derecha:
                    delta_x += constantes.VELOCIDAD_PERSONAJE
                #funciones del jugador
                # mover al jugador
                posicion_ventana, nivel_completado = player.Movimiento_player(delta_x,delta_y,mundo.list_obstaculos,mundo.pass_tile,mundo.list_tiles_x_izquierda,mundo.list_tiles_x_derecha,mundo.list_tiles_y_arriba,mundo.list_tiles_y_abajo)
                if nivel_completado and not (mundo.list_enemigos or grupo_items):
                    if nivel == 0 :
                        nivel += 1
                        player.shape.center = constantes.SPAWN_NIVEL_1
                        mundo.Reset_world((grupo_damage_text,grupo_balas,grupo_items))
                        mundo.Process_list(list_tiles,nivel,32,(monedas_images,[pocion]),animaciones_enemigos)
                        for items in mundo.list_items:
                            grupo_items.add(items)
                    else:
                        juego_terminado = True
                mundo.Update_mundo(posicion_ventana)
                #actualizando al jugador
                player.Update()
                
                #funciones del enemigo
                #actualizar a los enemigos
                for ene in mundo.list_enemigos:
                    if ene.vida == 0:
                        mundo.list_enemigos.remove(ene)
                    else:
                        ene.Movimiento_enemigos(posicion_ventana,mundo.list_obstaculos,player)
                        ene.Update()
                    #print(ene.vida)  
                #actualiza el estado del arma
                bala = arco.update(player)
                if bala:
                    grupo_balas.add(bala)
                #dibujar balas
                for bala in grupo_balas:
                    bala.Draw_b(ventana)
                    dano,posicion_dano = bala.update_b(mundo.list_enemigos,mundo.list_obstaculos)
                    #print(grupo_balas)
                    if dano:
                        damage_text = Damage_text(posicion_dano.centerx ,posicion_dano.centery , str(dano), font ,constantes.COLOR_DAMAGE)
                        grupo_damage_text.add(damage_text)
                #actualizar daño
                grupo_damage_text.update(posicion_ventana)
                #actualizar items
                grupo_items.update(player,posicion_ventana)
            else:
                text_game_over_rect = text_game_over.get_rect(center=(constantes.ANCHO/2,(constantes.ALTO/2)-150))
                ventana.blit(text_game_over,text_game_over_rect)
                text_reset_rect = text_reset.get_rect(center=(constantes.ANCHO/2,constantes.ALTO/3*2))
                reset_rect = pygame.draw.rect(ventana,constantes.COLOR_GAME_OVER,text_reset_rect)
                ventana.blit(text_reset,text_reset_rect)
    pygame.display.update()
    #update():se usa para actualizar la pantalla con cualquier cambio realizado en los elementos gráficos
pygame.quit()
#linea 180:)