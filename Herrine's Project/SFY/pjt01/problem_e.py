import json


def dec_movies(movies):
    movie_ids = []
    for movie in movies:
        movie_ids.append(movie.get('id'))
    # print(movie_ids)
    dec_li = []
    for movie_id in movie_ids:
        info_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        # json을 dictionary로 바꿔서
        info_dict = json.load(info_json)
        M = info_dict.get('release_date')
        Month = M[5:7]
        if Month == '12':
            t = info_dict.get('title')
            dec_li.append(t)
    result = dec_li

    return result

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))