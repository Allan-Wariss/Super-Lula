from OpenGL.GL import *

class ShipObject:
    def __init__(self, x=0.0,y=-0.5):

        self.x = x
        self.y= y

        tamV0= [-0.1, -0.1]
        tamV1= [0.1, -0.1]
        tamV2= [0.1, 0.1]
        tamV3= [-0.1, 0.1]

        self.vertices = [
            tamV0,  # v0
            tamV1,   # v1
            tamV2,    # v2
            tamV3    # v3
        ]
        
        # mapeamento de textura
        # coodenadas da textura - padrão openGL
        self.uvs = [
            [0, 0],
            [1, 0],
            [1, 1],
            [0, 1]
        ]

        self.faces = [
            [0, 1, 2],
            [0, 2, 3]
        ]
        
        self.texId = 0               # cria o objeto sem nenhuma textura
        self.color = [1, 1, 0]

    def draw(self):
        glColor3fv(self.color)
        glBindTexture(GL_TEXTURE_2D, self.texId) # qual textura aplicar
        
        glBegin(GL_TRIANGLES)

        for f in self.faces:
            for vid in f:
                glTexCoord2fv(self.uvs[vid]) # coord de textura

                vx = self.vertices[vid][0] + self.x
                vy = self.vertices[vid][1] + self.y
                glVertex2f(vx, vy)

        glEnd()
        
        glBindTexture(GL_TEXTURE_2D, 0) # desativa