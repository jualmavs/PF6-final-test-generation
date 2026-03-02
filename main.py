import requests
import json


def dish_fetch(num):

    url = "https://api-colombia.com/api/v1/TypicalDish"

    response = requests.get(url)
    data = json.loads(response.text)

   
    for dish in data:
        if dish.get("id") == num:
            return {
                "id": dish.get("id"),
                "name": dish.get("name")
            }

    
    return {
        "id": num,
        "name": "No encontrado"
    }


def main():
    numero = int(input("Ingrese el id del plato: "))
    resultado = dish_fetch(numero)

    print("Resultado:")
    print(resultado)


if __name__ == "__main__":
    main()