import requests

url = 'https://api.themoviedb.org/3/movie/now_playing?api_key=ae84f682cf50c20d864e92f56ee3c947&language=en-US&page=1'

headers = {
    'Accepts': 'application/json',
    'api_key': 'ae84f682cf50c20d864e92f56ee3c947'
}
parameters = {
    'api_key': 'ae84f682cf50c20d864e92f56ee3c947'
}

json = requests.get(url, params=parameters, headers=headers).json()

movies = json['results']

for x in movies:
    movie_detail = x['title'] + '\n' + x['release_date'] + '\n' + x['overview'] + '\n\n'
