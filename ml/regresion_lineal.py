"""
Regresión Lineal Simple
Implementación desde cero usando el método de mínimos cuadrados
para encontrar la recta que mejor se ajusta a los datos.
"""


def calcular_media(valores):
    return sum(valores) / len(valores)


def regresion_lineal(x, y):
    """
    Calcula los coeficientes de la regresión lineal y = m*x + b.

    Args:
        x: lista de valores independientes
        y: lista de valores dependientes

    Returns:
        (m, b) pendiente e intercepto
    """
    n = len(x)
    media_x = calcular_media(x)
    media_y = calcular_media(y)

    numerador = sum((x[i] - media_x) * (y[i] - media_y) for i in range(n))
    denominador = sum((x[i] - media_x) ** 2 for i in range(n))

    m = numerador / denominador
    b = media_y - m * media_x
    return m, b


def predecir(x, m, b):
    """Predice el valor de y para un x dado."""
    return m * x + b


def coeficiente_r2(x, y, m, b):
    """
    Calcula el coeficiente de determinación R².
    Un valor de 1.0 indica ajuste perfecto.
    """
    media_y = calcular_media(y)
    ss_total = sum((yi - media_y) ** 2 for yi in y)
    ss_residual = sum((yi - predecir(xi, m, b)) ** 2 for xi, yi in zip(x, y))
    return 1 - (ss_residual / ss_total)


if __name__ == "__main__":
    # Ejemplo: relación entre horas de estudio y calificación
    horas = [1, 2, 3, 4, 5, 6, 7, 8]
    calificacion = [50, 55, 60, 65, 70, 75, 80, 85]

    m, b = regresion_lineal(horas, calificacion)
    print(f"Ecuación: y = {m:.2f}x + {b:.2f}")

    horas_estudio = 9
    prediccion = predecir(horas_estudio, m, b)
    print(f"Predicción para {horas_estudio} horas: {prediccion:.1f}")

    r2 = coeficiente_r2(horas, calificacion, m, b)
    print(f"Coeficiente R²: {r2:.4f}")
