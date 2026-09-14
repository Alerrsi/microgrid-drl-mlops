import pandas as pd
import os
from datetime import datetime

dataset = pd.read_csv(
    "~/Documentos/proyectos/microred/data/raw/household_power_consumption.txt",     
    sep=";",
    na_values=["?"]
    )

#conbinar celdas para formar un datetime
dataset["DateTime"] = dataset["Date"] + " " + dataset["Time"]

# transformar el valor a datetime
dataset["DateTime"] = pd.to_datetime(dataset["DateTime"])




# eliminar columnas no necearias

dataset = dataset.drop(columns=["Date", "Time"])

# ejecutar solo una vez
dataset = dataset.set_index("DateTime")

print(dataset.index)

# interpolación de valores nulos

def interpolar(x, x0, y0, x1, y1):
    return y0 + ((y1-y0)/(x1-x0))*(x-x0)


dataset.interpolate(method='time', inplace=True)

#eliminado de nulos en limites, donde no se pudo aplicar la interpolación
dataset.dropna(inplace=True)


# reducción de paso de minutos en horas
dataset_sampling = dataset.resample('h').mean()
#### Generación de columnas como hora, dia de la semana y mes
dataset_sampling["Month"] = dataset_sampling.index.month
dataset_sampling["Hour"]  = dataset_sampling.index.hour
dataset_sampling["Date_Of_Week"] = dataset_sampling.index.dayofweek


# guardar en csv


dataset_sampling.to_csv("~/Documentos/proyectos/microred/data/processed")