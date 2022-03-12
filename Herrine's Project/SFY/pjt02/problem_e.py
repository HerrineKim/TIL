import requests
from pprint import pprint

def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '8854669b886a6c07c12ea947bcc2311d',
        'query': title,
        'region': 'KR',
        'language': 'ko'
    }

    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    search_movie = data['results']
    if len(search_movie) == 0:
        return None
    elif len(search_movie) > 1 :
        sorted(search_movie, key=lambda movie: (-movie['vote_count']))
    movie_id = search_movie[0]['id']

    path1 = f'/movie/{movie_id}/credits'
    params1 = {
        'api_key': '8854669b886a6c07c12ea947bcc2311d',
        'language': 'ko'
    }

    response1 = requests.get(BASE_URL+path1, params=params1)
    data1 = response1.json()
    actors = []
    directors = []
    for actor in data1['cast']:
        if actor['cast_id'] < 10:
            actors.append(actor['name'])
    for staff in data1['crew']:
        if staff['department'] == 'Directing':
            directors.append(staff['name'])
    credits = {'cast': actors, 'crew': directors}
    return credits


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
