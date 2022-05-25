class Coche:
    ruedas = 4

    def __init__(self, color,aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelerar(self):
        self.velocidad += self.aceleracion

    def frenar(self):
        v = self.velocidad - self.aceleracion
        if v < 0:
            v = 0.0
        self.velocidad = v



print("Ejemplo Programacion Orientada Objetos")

coche1 = Coche(color="rojo", aceleracion=20)
print(f"La velocidad del coche1 es {coche1.velocidad}")
coche1.acelerar()
print(f"La velocidad del coche1 es {coche1.velocidad}")
for i in range(10):
    coche1.acelerar()
print(f"La velocidad del coche1 de color {coche1.color} es {coche1.velocidad}")

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


