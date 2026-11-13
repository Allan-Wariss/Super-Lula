from PIL import Image
from OpenGL.GL import *

class Texture:
    def __init__(self, fileName):
        img = Image.open(fileName)                  # abre uma imagem
        img = img.transpose(Image.FLIP_TOP_BOTTOM)  # inverte a imagem verticalmente
        imgData = img.convert("RGBA").tobytes()      # converte a imagem para um vetor de bytes

        self.texId = glGenTextures(1)  # criar textura
        glBindTexture(GL_TEXTURE_2D, self.texId)    # torna ela ativa
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST) 

        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE) # subtituir a cor ou combinar?

        glTexImage2D(
            GL_TEXTURE_2D,                          # tipo alvo de textura
            0,                                      # nível de mipmap
            GL_RGBA,                                 # formato interno de armazenamento
            img.width,                              # largura da imagem em pixels
            img.height,                             # altura da imagem em pixels
            0,                                      # borda
            GL_RGBA,                                 # formato dos dados da imagem
            GL_UNSIGNED_BYTE,
            imgData
        )

        glBindTexture(GL_TEXTURE_2D, 0)             # desativa. Ativa apenas quando for usar