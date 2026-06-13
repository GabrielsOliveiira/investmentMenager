def toFloat(text:str) -> float:

    if not text:
        return 0.0

    text = text.replace(',', '.')

    try:
        return float(text)
    except:
        return 0.0

def dataMenager(data:str) -> str:
    newData = data.split("-")
    return(f"{newData[1]}/{newData[2]}/{newData[0]}")