import pandas as pd
import numpy as np

serie_amigos = ["pedro", "santiago", "Farfan", "javipollas", "nigger", "Aiko", "Tilin"]
print("----- Serie listado de amigos NC 0113 -----")
amigos = pd.Series(serie_amigos)
print(amigos)

serie_billetes = [20, 50, 100, 200, 500, 1000]
print("----- Serie listado valor de billetes MX NC 0113 -----")
billetes = pd.Series(serie_billetes)
print(billetes)

serie_billetes = [20, 50, 100, 200, 500, 1000]
serie_letras = ("veinte", "cincuenta", "cien", "doscientos", "quinientos", "mil")
print("----- Serie listado valor de billetes MX NC 0113 -----")
tablabilletes = pd.Series(serie_billetes, index=serie_letras)
print(tablabilletes)

# Diccionario dataframe
# Diccionarios de valor monedas y nombre
print("datos de diccionarios a dataframe en pandas")
dic_monedas = {
    "serie_billetes": [20, 50, 100, 200, 500, 1000],
    "serie_letras": ("veinte", "cincuenta", "cien", "doscientos", "quinientos", "mil")
}

tablabilletes = pd.DataFrame(dic_monedas, index=["A", "B", "C", "D", "E", "F"])
print(tablabilletes)

print("casa de cambio de Santiago Pacheco NC = 0113")