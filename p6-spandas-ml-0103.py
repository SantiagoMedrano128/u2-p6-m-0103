import pandas as pd
import numpy as np

serie_amigos =["Pedro", "Morgan", "Farfan", "El Adrian", "Jesse", "Nava", "Mario"]
print(" --- Serie listado de amigos NC 0103 --- ")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes =[20,50,100,200,500,1000]
print(" --- Serie listado de billetes MX NC 0103 --- ")
billetes=pd.Series(serie_billetes)
print(billetes)

serie_billetes =[20,50,100,200,500,1000]
serie_bletras = ["veinte","cincuenta","cien","doscientos","quinientos","mil"]
print(" --- Serie listado nombre y valor de billetes MX NC 0103 --- ")
tablabilletes=pd.Series(serie_billetes, serie_bletras)
print(tablabilletes)
# diccionario dataframe
# diccionariop de valor monedas y nombre
print("datos de diccionario a DataFrame en pandas")
dic_monedas={
    "serie_billetes" :[20,50,100,200,500,1000],
    "serie_bletras" :["veinte","cincuenta","cien","doscientos","quinientos","mil"]
}

tablabilletes=pd.DataFrame(dic_monedas, index= ["A","B","C","D","E","F"])
print(tablabilletes)

print("Casa de cambio de Santiago Medrano NL 0103")