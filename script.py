import pandas as pd
import json

def main():
    #Leer el archivo JSON
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    #si el Json es un diccionario único, conviertelo en una lista
    if isinstance(data, dict):
        data = [data]

    #Crea un DtaFrame y cuarda en ecxel
    df = pd.DataFrame(data)
    df.to_excel('output.xlsx', index=False)
    print("Archivo Ecxel 'output.xlsx' generado exitosamente.")

if __name__ == '__main__':
    main()
