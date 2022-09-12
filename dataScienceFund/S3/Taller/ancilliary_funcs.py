
import matplotlib.pyplot as plt

def fetch_descriptives(data, columns):
    '''
        Función que calcula las estadísticas descriptivas de las variables categoricas y numericas.
    '''
    categoricas = None
    numericas = None

    try:
        categoricas = data[columns].describe(include=object)
    except Exception as e:
        print(e)
    
    try:
        numericas = data[columns].describe(include=[np.number])
    except Exception as e:
        print(e)

    return categoricas, numericas


def show_null_cases(dataframe,var_to_inspect,column = 'ccodealp',print_list=False):
    null_cases = dataframe[var_to_inspect].isna()
    count_null = null_cases.sum()
    percent = (count_null/dataframe.shape[0]) * 100
    casos = []

    if print_list:
        casos = dataframe[null_cases][column]

    return count_null, percent, casos
    
def dot_plot(dataframe, plot_var,plot_by, statistic = 'mean', global_stat = False):
    agrupacion = dataframe.groupby(plot_by)[plot_var]
    valores_grafico = []

    if statistic == 'mean':
        valores_grafico = agrupacion.mean()
    elif statistic == 'median':
        valores_grafico = agrupacion.median()

    plt.plot(valores_grafico,valores_grafico.index,"o")

    if global_stat and statistic == 'mean':
        plt.axvline(dataframe[plot_var].mean(), label='Promedio general')
    elif global_stat and statistic == 'median':
        plt.axvline(dataframe[plot_var].median(), label='Mediana general')