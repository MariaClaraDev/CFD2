import requests

def main():

    nomePlaneta = "Alderaan"

    urlBase = "https://swapi.dev/api/planets/"

    resultPlanetas = requests.get(urlBase)
    jsonResultPlanetas = resultPlanetas.json()

    for planetas in jsonResultPlanetas["results"]:
        if nomePlaneta == planetas["name"]:
            nomeFilmes = []
            for urlPlaneta in planetas["films"]:
                filme = requests.get(urlPlaneta)
                jsonFilme = filme.json()
                
                nomeFilmes.append(jsonFilme["title"])
    
    print("O Planeta {}, Aparece em {} Filmes, Abaixo o Nome Dos Mesmos:". format(nomePlaneta, len(nomeFilmes)))

    for i in nomeFilmes:
        print(i)
   
if __name__ == '__main__':
        main()