import requests

BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '8854669b886a6c07c12ea947bcc2311d',
    'region': 'KR',
    'language': 'ko.'
}

response = requests.get(BASE_URL+path, params=params)
data = response.json()

def popular_count():
    cnt_popular = len(data.get('results'))
    return cnt_popular

if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20