from numpy import empty
import requests
from pprint import pprint


def recommendation(title):
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

    BASE_URL = 'https://api.themoviedb.org/3'
    path1 = f'/movie/{movie_id}/recommendations'
    params1 = {
        'api_key': '8854669b886a6c07c12ea947bcc2311d',
        'language': 'ko'
    }

    response = requests.get(BASE_URL+path1, params=params1)
    data1 = response.json()
    empty_list = []
    recom_list = []
    if len(data1['results']) == 0:
        return empty_list
    else:
        for i in range(len(data1['results'])):
            recom_list.append(data1['results'][i]['title'])
        return recom_list

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
