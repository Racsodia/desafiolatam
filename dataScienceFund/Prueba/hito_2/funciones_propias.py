import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score

def nulos(dataframe, var):
    """"
    Retorna la cantidad de nulos valor y en porcentaje de una variable
    
    dataframe: dataframe que se quiere explorar
    
    var: variable a la cual que se quiere obtener los nulos
    """
    nulos = dataframe[var].isna()
    cantidad = nulos.sum()
    porcentaje = (cantidad/dataframe.shape[0]) * 100 
    
    return cantidad, porcentaje

def plot_freq(dataframe, col):
    """
    Grafica en formato de barras las frecuencias de la variable
    
    dataframe: dataframe que se quiere explorar
    
    col: variable a la cual se quiere graficar
    
    """
    
    dataframe[col].value_counts().plot(kind="bar");
    plt.title(f"Grafico de barra para {col}")
    
    plt.legend()
    
def frecuencia(dataframe, col):
    """
    Returna la frecuencia de la observaciones
    
    dataframe: dataframe que se quiere explorar
    
    col: variable que se quiere revisar
    """
    return dataframe[col].value_counts()

def plot_hist(data, variable):
    """
    Grafica en formato de histograma la variable, tambien representa la media y mediana
    
    data: dataframe que se quiere explorar
    
    variable: variable que se quiere revisar
    
    """
    promedio = np.mean(data[variable])
    mediana = np.median(data[variable])
    
    sns.distplot(data[variable], bins=8)
 
    plt.axvline(promedio, color="lightseagreen", label = f"Media: {round(promedio, 2)}", lw=3, ls="dotted")
    plt.axvline(mediana, color="plum", label = f"Mediana: {round(mediana, 2)}", lw=3, ls="dotted")
    plt.title(f"Histograma para {variable}")
    plt.legend()
        
        
def cambio_nombre_col(data, var, n_var):
    """
    Cambia de nombre a la variable
    
    data: dataframe donde se encuentra la variable
    
    var: nombre de la variable que se desea cambiar
    
    n_var: nombre nuevo de la variable
    """
    
    data.rename(columns={var:n_var}, inplace=True)
    
def report_scores(y_test, y_hat):
    """
    Imprime los valores de MSE y r2
    
    y_test= Recibe el y_test correspondiente a la separacion de la muestra
    
    y_hat= Recibe el y_hat de las predicciones
    """
    MSE = mean_squared_error(y_test, y_hat)
    r2 =  r2_score(y_test, y_hat)

    print(f"MSE: {MSE}, R2: {r2}")
    