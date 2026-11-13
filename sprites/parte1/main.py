import glfw                    # Módulo para criação da janela e tratamento de eventos
from OpenGL.GL import *        # Módulo com as funções e constantes da OpenGL
from object import *

ship = Object()

# Função que define configurações iniciais
def init():
    glClearColor(0.9,0.9,0.9,1.0)                 # Define a cor de fundo da janela

# Atualiza a lógica do seu jogo
def update():
    pass

# Função que atualiza a renderização da cena
def render():
    glClear(GL_COLOR_BUFFER_BIT)                   # Limpa o buffer de cores com a cor de fundo
    ship.draw()

# Função Principal
def main():
    glfw.init()                                    # Inicializa a GLFW
    window = glfw.create_window(700,700,'Jogo da Navinha',None,None) # Cria a janela
    glfw.make_context_current(window)              # Associa o contexto OpenGL à janela
    
    init()                                         # Executa as configurações iniciais da OpenGL

    while not glfw.window_should_close(window):    # Enquanto a janela não for fechada (Laço Principal)
        glfw.poll_events()                         # Tratamento de eventos de entrada
        update()
        render()                                   # Atualiza o desenho no frame buffer
        glfw.swap_buffers(window)                  # Troca de buffers (Double Buffering)

    glfw.terminate()                               # Finaliza a GLFW

if __name__ == '__main__':
    main()           