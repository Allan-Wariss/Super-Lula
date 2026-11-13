from OpenGL.GL import *

class Object:
    def __init__(self):
        self.vertices = [
            [-0.5, -0.5],  # v0
            [0.5, -0.5],   # v1
            [0.5, 0.5],    # v2
            [-0.5, 0.5]    # v3
        ]

        self.faces = [
            [0, 1, 2],
            [0, 2, 3]
        ]

        self.color = [1, 1, 0]

    def draw(self):
        glColor3fv(self.color)
        glBegin(GL_TRIANGLES)

        for f in self.faces:
            for vid in f:
                glVertex2fv(self.vertices[vid])

        glEnd()