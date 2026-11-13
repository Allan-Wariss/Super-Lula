import glfw
from OpenGL.GL import *
from math import *
from shipObject import *
from enemyObject import *
from texture import *

enemy1 = EnemyObject()
ship = ShipObject()

velocidade = 0.025  
tiros_jogador = []  
espaco_pressionado_anteriormente = False

def init():
    glClearColor(0, 0, 0, 1.0)
    glEnable(GL_TEXTURE_2D)
    
    tex = Texture('textures/ship.png')
    enemy1.texId = tex.texId
    ship.texId = tex.texId

def update():
    pass

def render():
    glClear(GL_COLOR_BUFFER_BIT)
    
    ship.draw()
    enemy1.draw()
    
    for tiro in tiros_jogador:
        tiro.draw()

def calcular_distancia(x1, y1, x2, y2):
    return math.dist((x1, y1), (x2, y2))

def main():
    global espaco_pressionado_anteriormente
    glfw.init()
    window = glfw.create_window(700, 700, 'Jogo da Navinha', None, None)
    glfw.make_context_current(window)
    glfw.swap_interval(1)  
    
    init()    

    FPS_ALVO = 60.0
    TEMPO_POR_ATUALIZACAO = 1.0 / FPS_ALVO
    
    last_time = glfw.get_time()
    acumulador = 0.0

    while not glfw.window_should_close(window):
        current_time = glfw.get_time()
        delta_tempo = current_time - last_time
        last_time = current_time
        
        acumulador += delta_tempo
        glfw.poll_events()

        while acumulador >= TEMPO_POR_ATUALIZACAO:
            
            # 1. Movimento da nave
            ship.mover(window=window, velocidade=velocidade)

            # 2. Lógica de tiro (Barra de Espaço)
            espaco_atual = glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS
            if espaco_atual and not espaco_pressionado_anteriormente:
                novo_tiro = ship.atirar()
                tiros_jogador.append(novo_tiro)
            espaco_pressionado_anteriormente = espaco_atual

            # 3. Atualiza posição dos tiros do jogador
            for tiro in tiros_jogador[:]:
                tiro.update()
                if tiro.y > 1.0:
                    tiros_jogador.remove(tiro)

            # 4. Verificação de colisão (Tiro do Jogador x Inimigo)
            if enemy1.ativo:
                for tiro in tiros_jogador[:]:
                    # Definimos a caixa delimitadora (AABB) do inimigo (tamanho -0.1 a +0.1 em x e y)
                    inimigo_xmin = enemy1.x - 0.1
                    inimigo_xmax = enemy1.x + 0.1
                    inimigo_ymin = enemy1.y - 0.1
                    inimigo_ymax = enemy1.y + 0.1

                    # Verifica se o tiro está dentro dos limites do inimigo
                    if (inimigo_xmin <= tiro.x <= inimigo_xmax) and (inimigo_ymin <= tiro.y <= inimigo_ymax):
                        enemy1.ativo = False       # O inimigo morre e some
                        tiros_jogador.remove(tiro) # O tiro some
                        break                      # Sai do loop de tiros para evitar erros

            # 5. Atualiza inimigo e lógica geral
            enemy1.update(x_min=-1.0, x_max=1.0)
            update()

            acumulador -= TEMPO_POR_ATUALIZACAO

        render()
        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == '__main__':
    main()