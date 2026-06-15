from datetime import date

def toFloat(text:str) -> float:

    if not text:
        return 0.0

    text = text.replace(',', '.')

    try:
        return float(text)
    except:
        return 0.0

def dias_restantes(data):
    return (data - date.today()).days

def projecaoGanhos(valor, taxaM, dias):
    taxaD = (1 + taxaM/100) ** (1/30) - 1
    return round(valor * ((1 + taxaD) ** dias - 1), 2)