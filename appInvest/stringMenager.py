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