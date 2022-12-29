# 캐시
def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for city in cities:  # 시티 순회하면서
            city = city.lower()  # 전부 소문자로 바꿔서 계산
            if city not in cache:  # 캐시에 없으면서 (cache miss)
                if len(cache) < cacheSize:  # 캐시사이즈보다 작으면 더 들어갈 수 있으므로 넣음
                    cache.append(city)
                else:  # 캐시사이즈랑 같으면 가장 오래전 참조한 값 빼고 현재값 넣어줌
                    cache.pop(0)
                    cache.append(city)
                answer += 5
            else:  # 캐시에 있는 경우 (cache hit)
                cache.pop(cache.index(city))  # 해당 값을 가장 최신 위치에 넣어줌
                cache.append(city)
                answer += 1
            
    return answer