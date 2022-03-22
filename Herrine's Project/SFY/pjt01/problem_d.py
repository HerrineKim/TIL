from encodings import utf_8
import json


def max_revenue(movies):
    movie_ids = []
    for movie in movies:
        movie_ids.append(movie.get('id'))
    # print(movie_ids)
    maxV = 0
    for movie_id in movie_ids:
        info_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        # json을 dictionary로 바꿔서
        info_dict = json.load(info_json)
        rev = info_dict.get('revenue')
        if rev > maxV:
            maxV = rev
            target_id = movie_id

    
    res_json = open(f'data/movies/{target_id}.json', encoding='UTF8')
    res_dict = json.load(res_json)
    result = res_dict.get('title')

    return result
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))