class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method

    # 생성자를 통해 item 딕셔너리를 생성하고, 처음 클래스 객체를 생성할 때 받은 인자로 item 딕셔너리의 값을 결정한다.
    def __init__(self, name, city, district, ptype, longitude, latitude):
        self.__item = {'name':'', 'city':'', 'district':'', 'ptype':'', 'longitude':0.0, 'latitude':0.0}
        self.__item['name'] = str(name)
        self.__item['city'] = str(city)
        self.__item['district'] = str(district)
        self.__item['ptype'] = str(ptype)
        self.__item['longitude'] = float(longitude)
        self.__item['latitude'] = float(latitude)

    # item 딕셔너리의 keyword의 값을 반환하는 get 메소드 추가
    def get(self, keyword='name'):
        return self.__item[keyword]
    
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

def str_list_to_class_list(str_list):
    p = []      # parking_spot 클래스 원소 저장할 리스트 'p' 선언
    for i in range(len(str_list)):      # 읽은 텍스트 파일의 줄 수만큼 반복
        data = str_list[i].split(',')       # 읽은 텍스트 파일의 줄을 쉼표(',')로 구분하여 'data' 리스트에 저장
        name = data[1]      # name부터 latitude까지 리스트 'data'에서 올바른 값을 저장
        city = data[2]
        district = data[3]
        ptype = data[4]
        longitude = data[5]
        latitude = data[6]
        # 저장한 데이터를 인자로 'parking_spot' 클래스 객체 't' 선언
        t = parking_spot(name, city, district, ptype, longitude, latitude)
        p.append(t)     # 'parking_spot' 클래스 객체 't'를 리스트 'p'에 추가
    return p    # parking_spot 클래스를 원소로 하는 리스트 'p'를 반환
    
def print_spots(spots):
    print(f"---print elements({len(spots)})---")        # *len(list) : list의 길이 반환
    # 리스트 'spots' 요소 하나마다 한 줄씩 출력 
    for i in spots:
        print(i)

def filter_by_name(spots, name):
    # 주어진 문자열이 이름에 포함된 곳만 필터링
    new_spots = [spot for spot in spots if name in spot.get('name')]
    return new_spots

def filter_by_city(spots, city):
    # 주어진 도시에 위치한 것만 필터링
    new_spots = [spot for spot in spots if city in spot.get('city')]
    return new_spots

def filter_by_district(spots, district):
    # 주어진 시 군구에 위치한 것만 필터링
    new_spots = [spot for spot in spots if district in spot.get('district')]
    return new_spots

def filter_by_ptype(spots, ptype):
    # 주어진 유형에 맞는 것만 필터링
    new_spots = [spot for spot in spots if ptype in spot.get('ptype')]
    return new_spots

def filter_by_location(spots, locations):
    # 튜플 인자 'locations'을 사용해 최소 경도, 최대 경도, 최소 위도, 최대 위도 설정
    min_lat = locations[0]
    max_lat = locations[1]
    min_lon = locations[2]
    max_lon = locations[3]
    # 주어진 경도와 위도 사이에 위치한 것만 필터링
    new_spots = [spot for spot in spots if (min_lat < spot.get('latitude') and spot.get('latitude') < max_lat and min_lon < spot.get('longitude') and spot.get('longitude') < max_lon)]
    return new_spots

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)