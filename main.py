from test import test
class Coche:
    ruedas = 4

    def __init__(self, color="", aceleracion=None):
        if color:
            self.color = test(color)
        else:
            self.color = "rojo"
            print("Se definió el color del coche como rojo por default")

        if aceleracion:
            self.aceleracion = aceleracion
        else:
            self.aceleracion = 20
            print("Se definió la aceleracion del coche como 20 por default")

        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += self.aceleracion

    def frenar(self):
        v = self.velocidad - self.aceleracion
        if v < 0:
            v = 0.0
        self.velocidad = v

    def __str__(self):
        return f"La velocidad del coche de color {coche1.color} es {coche1.velocidad}"


class CocheVolador(Coche):

    ruedas = 6

    def __init__(self, color, aceleracion, esta_volando=False):
        super().__init__(color, aceleracion)
        self.esta_volando = esta_volando

    def vuela(self):
        self.esta_volando = True

    def aterriza(self):
        self.esta_volando = False

print("Ejemplo Programacion Orientada Objetos")

coche1 = Coche(color="rojo", aceleracion=20)
print(coche1)
coche1.acelerar()
print(coche1)
for i in range(10):
    coche1.acelerar()
print(coche1)

'''
def limpiezaDeDF(df):
    df = quitarAcentos(df, "col1")
    return quitarCaracteresASCI(df)

def quitarCaracteresASCI(df):
    return df

def quitarAcentos(df, col=""):
    return df[col].replace({"á":"a"})

import pandas as pd
class Modelo(object):
    def __init__(self, df=None):
        if df is not None:
            self.df = df
        else:
            self.df = pd.DataFrame()

    def preprocesamiento(self, df=None):
        if not self.df and df is not None:
            self.df = df
        self.df = limpiezaDeDF(self.df)


def main_objeto():
    df = pd.DataFrame()
    modelo = Modelo(df)
    modelo.preprocesamiento()
    modelo.entrenamiento()
    modelo.prediccion()
    modelo.metricas()
    return


def preprocesamiento(df = None):
    if df is not None:
      return limpiezaDeDF(df)
    else:
        return None

def main():
    df = pd.DataFrame()
    df = preprocesamiento(df)
    df = entrenamiento(df)
'''