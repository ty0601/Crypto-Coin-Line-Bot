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
movie_detail = ''
i = 0
for x in movies:
    if i > 4: break
    movie_detail += 'Movie : ' + x['title'] + '\n' + \
                    'Release Date : ' + x['release_date'] + '\n' + \
                    'Overview : \n' + x['overview'] + '\n\n'
    i += 1
