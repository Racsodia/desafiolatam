import numpy as np
import matplotlib.pyplot as plt

def plot_ll(lims=(-10, 10), weights=[0.5, 1, 5], n=50, palette=plt.cm.GnBu, plot_legend=True):
    # Código obtenido de https://github.com/GAMES-UChile/Curso-Aprendizaje-de-Maquinas/blob/master/Figuras.ipynb

    #Curva logística:
    x = np.linspace(lims[0], lims[1], 1000)
    plots = [
        1 / (1 + np.exp(-w*x))
        for w in weights
    ]
    colors = palette(np.linspace(0.2, 0.9, len(weights)))

    for i in range(len(weights) - 1):
        plt.plot(x, np.flip(plots[i]) if lims[0] > lims[1] else plots[i], lw=2, color=colors[i], alpha=0.8, ls="dotted", label=f"Ajuste {i+1}")
    
    plt.plot(x, np.flip(plots[-1]) if lims[0] > lims[1] else plots[-1], label="Máxima verosimilitud", lw=3, color=colors[-1] if len(weights) > 1 else "steelblue")

    #Muestras (falsas):
    menos_1 = lims[0] + lims[1] - 1
    mas_1 = lims[0] + lims[1] + 1
    muestra_c1 = np.random.uniform(lims[0], menos_1 if lims[0] < lims[1] else mas_1, n)
    muestra_c2 = np.random.uniform(mas_1 if lims[0] < lims[1] else menos_1, lims[1], n)
    clases = np.zeros(n)
    plt.plot(muestra_c1, clases, 'o', label='Muestras Clase 1', ms=13, c="mediumpurple")
    plt.plot(muestra_c2, clases + 1, 'o', label='Muestras Clase 2', ms=13, c="palevioletred")

    #Plano de decisión:
    plt.axhline(0.5, ls='--', alpha=0.6, color='gray', label="Frontera de decisión")

    if plot_legend:
        plt.legend(ncol=5, bbox_to_anchor =(1, 1.25))
        
    plt.xlabel('x')
    plt.ylabel('Probabilidad');
    return muestra_c1, muestra_c2

def plot_ll_logit():
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 2, 1)
    c1, c2 = plot_ll(lims=(3, -3), weights=[5], n=5, plot_legend=False)
    plt.title("Regresión logística")

    plt.subplot(1, 2, 2)
    plt.plot((-3, 3), (4, -4), color="steelblue", lw=3)
    plt.axhline(0, ls='--', alpha=0.6, color='gray')
    plt.yticks(np.arange(-4, 5), ("-inf", -3, -2, -1, 0, 1, 2, 3, "+inf"))
    plt.plot(c1, [-4] * len(c1), 'o', label='Muestras Clase 1', ms=13, c="mediumpurple")
    plt.plot(c2, [4] * len(c2), 'o', label='Muestras Clase 2', ms=13, c="palevioletred")
    plt.title("Log odds (Logit)")
    plt.ylabel("Log odds")
    plt.xlabel("x")
    plt.legend()
    plt.tight_layout()
    
def crossvalidation_schema(cv_folds=5, textprop={}):
    """docstring for crossvalidation_schema"""
    fig=plt.figure()
    ax=fig.add_axes([0,0,1,1])
    ax.axis('off')
    for i in range(cv_folds):
        ax.add_patch(plt.Rectangle((0, i), 5, 0.7, fc='lightgrey'))
        ax.add_patch(plt.Rectangle((5. * i /cv_folds, i), 5. / cv_folds,
        0.7, fc='skyblue'))
        ax.text(5. * (i + .5) / cv_folds, i + .45, "Val.", ha='center', va='center', **textprop)
        ax.text(5, i + .15, r'Ensayo {0}$\in${1} '.format(cv_folds -
        i, cv_folds), ha = 'right', va='bottom', **textprop)
        ax.text(5.5, i + .35, r'Error testing $\hat\theta_{{0}}$'.format(i))
        ax.text(7, 2.3, 'Error')
        ax.set_xlim(-1, 6)
        ax.set_ylim(-0.2, cv_folds + 0.2)