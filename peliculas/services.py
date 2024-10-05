import requests

def consumir_api(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        print(response.json)
        return response.json()
    
def genero_peliculas():
    response = consumir_api('https://api.themoviedb.org/3/genre/movie/list?api_key=ecbcdcf9044928d12b179d9153f5a269&language=es-VE')
    
    if response:
        return response.get('genres')
    
    return ''

def genero_peliculas_tv():
    response = consumir_api('https://api.themoviedb.org/3/genre/tv/list?api_key=ecbcdcf9044928d12b179d9153f5a269&language=es-VE')
    
    if response:
        return response.get('genres')
    
    return ''

def ver_peliculas(parametros={}):
    response = consumir_api('https://api.themoviedb.org/3/movie/popular?api_key=ecbcdcf9044928d12b179d9153f5a269&language=es-VE&with_genres={genres}&page={page}'.format(**parametros))
    
    if response:
        return response.get('results')
    
    return ''