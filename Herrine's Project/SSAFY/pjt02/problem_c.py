import requests
from pprint import pprint

def ranking():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '8854669b886a6c07c12ea947bcc2311d',
        'region': 'KR',
        'language': 'ko.'
    }

    # response = requests.get(BASE_URL+path, params=params)
    # data = response.json()
    # pop_movies = sorted(data['results'], key=lambda movie:(-movie['vote_average']))
    # movies_top5 = []
    # for movie in pop_movies:
    #     movies_top5.append(movie)
    #     if len(movies_top5) >= 5:
    #         return movies_top5
    
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    arr = data['results']
    # pprint(arr)
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j]['vote_average'] > arr[j+1]['vote_average']:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    result = arr[:-6:-1]

    return result

if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
