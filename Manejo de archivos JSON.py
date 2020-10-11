import json

def crear_JSON(**myDict):
    myDict = {'Status': {'A11': 'A', 'A12': 'B', 'A13': 'C', 'A14': 'D'},
        'Credit History': {'A30': 'No tiene', 'A31': 'Todos reembolsados', 'A32': 'Algunos reembolsados', 'A33': 'Retrasado', 'A34': 'Critico'},
        'Purpose': {'A43': 'radio/tv', 'A46': 'education', 'A42': 'furniture/equipment', 'A40': 'Carro nuevo', 'A41': 'Carro usado',
                    'A49': 'Negocios', 'A44': 'uso domestico', 'A45': 'repairs', 'A410': 'otros', 'A48': 'retraining'},
        'Saving Account': {'A65': 'sin cuenta', 'A61': 'Menor de 100', 'A63': 'entre 500 y 1000', 'A64': 'mayor que 999', 'A62': 'entre 100 y 500'},
        'Present Employment Since': {'A75': 'Mayor que 6', 'A73': 'entre 1 y 4', 'A74': 'entre 4 y 7',
                                    'A71': 'desempleado', 'A72': 'menor que 1'},
        'Status and Sex': {'A93': 'mujer sol', 'A92': 'mujer DSC', 'A91': 'hombre DS', 'A94': 'hombre CV'},
        'Debtors/Guarantors': {'A101': 'ninguno', 'A103': 'fiador', 'A102': 'co-applicant'},
        'Property': {'A121': 'bienes raices', 'A122': 'seguro de vida', 'A124': 'Sin propiedad', 'A123': 'carro u otro'},
        'Plans': {'A143': 'ninguno', 'A141': 'Banco', 'A142': 'tiendas'},
        'Housing': {'A152': 'propio', 'A153': 'gratis', 'A151': 'alquilada'},
        'Job': {'A173': 'empleado', 'A172': 'no calificado', 'A174': 'independiente', 'A171': 'desempleado'},
        'Telephone': {'A192': 'si', 'A191': 'no'},
        'Foreing Worker': {'A192': 'si', 'A191': 'no'}}
    with open('data base.json', 'w') as archivo:
        json.dump(myDict, archivo, indent=4)
        print('Archivo creado con exito')

def leer_JSON():
    with open('data base.json', 'r') as myDict:
        return json.load(myDict)

def main():
    #crear_JSON(myDict)
    myDict = leer_JSON()
    print(myDict['Apt'].keys())


if __name__ == "__main__":
    main()

    
            



    


