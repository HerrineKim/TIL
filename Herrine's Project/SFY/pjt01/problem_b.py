import json
from pprint import pprint


def movie_info(movie, genres):
    
    id = movie.get('id')
    title = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')

    genres_dict = {}
    # id와 name을 매핑시키고 싶은 것

    for genre in genres:
        genres_dict[genre.get('id')] = genre.get('name')
    
    # 가지고 있는 id를 위에 있는 딕셔너리에서 검색한 다음에 리스트에 이름을 넣어준다

    genre_ids = [18, 80]

    genre_name_list = []
    for genre_id in genre_ids:
        genre_name_list.append(genres_dict.get(genre_id))


    result = {
        'id' : id,
        'title' : title,
        'poster_path' : poster_path,
        'vote_average': vote_average,
        'overview' : overview,
        'genre_names': genre_name_list
    }

    return result



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))