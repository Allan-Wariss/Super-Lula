from OpenGL.GL import *

class EnemyObject:
    def __init__(self, x=0.0, y=0.8):
        self.x = x
        self.y = y
        self.speed = 0.005  # Ajuste se necessário para o passo fixo
        self.ativo = True   # <--- Flag para indicar se o inimigo está vivo

        tamV0 = [-0.07, -0.07]
        tamV1 = [0.07, -0.07]
        tamV2 = [0.07, 0.07]
        tamV3 = [-0.07, 0.07]

        self.vertices = [tamV0, tamV1, tamV2, tamV3]
        
        self.uvs = [
            [0, 1],
            [1, 1],
            [1, 0],
            [0, 0]
        ]

        self.faces = [
            [0, 1, 2],
            [0, 2, 3]
        ]
        
        self.texId = 0
        self.color = [1, 1, 0]

    def update(self, x_min, x_max):
        # Se estiver morto, não faz nada
        if not self.ativo:
            return

        self.x += self.speed

        if self.x >= x_max:
            self.x = x_max
            self.speed *= -1
        elif self.x <= x_min:
            self.x = x_min
            self.speed *= -1

    def draw(self):
        # Se estiver morto, não desenha na tela
        if not self.ativo:
            return

        glColor3fv(self.color)
        glBindTexture(GL_TEXTURE_2D, self.texId)
        
        glBegin(GL_TRIANGLES)
        for f in self.faces:
            for vid in f:
                glTexCoord2fv(self.uvs[vid])
                vx = self.vertices[vid][0] + self.x
                vy = self.vertices[vid][1] + self.y
                glVertex2f(vx, vy)
        glEnd()
        
        glBindTexture(GL_TEXTURE_2D, 0)