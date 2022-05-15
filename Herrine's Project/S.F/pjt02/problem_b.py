import requests
from pprint import pprint

def vote_average_movies():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '8854669b886a6c07c12ea947bcc2311d',
        'region': 'KR',
        'language': 'ko.'
    }

    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    movies = []
    for movie in data['results']:
        if movie['vote_average'] >= 8:
            movies.append(movie['title'])
    return movies


if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
