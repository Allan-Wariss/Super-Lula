from OpenGL.GL import *

class BulletObject:
    def __init__(self, x, y, velocidade_y=0.03, color=[1, 1, 1]):
        self.x = x
        self.y = y
        self.velocidade_y = velocidade_y  # Positivo sobe (jogador), negativo desce (inimigo)
        self.color = color
        
        # Geometria simples para o tiro (um retângulo pequeno)
        self.vertices = [
            [-0.01, -0.03],
            [ 0.01, -0.03],
            [ 0.01,  0.03],
            [-0.01,  0.03]
        ]
        self.faces = [[0, 1, 2], [0, 2, 3]]

    def update(self):
        # Move o tiro na vertical
        self.y += self.velocidade_y

    def draw(self):
        glColor3fv(self.color)
        glBegin(GL_TRIANGLES)
        for f in self.faces:
            for vid in f:
                vx = self.vertices[vid][0] + self.x
                vy = self.vertices[vid][1] + self.y
                glVertex2f(vx, vy)
        glEnd()