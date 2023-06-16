#필요한 모듈 'parking_spot_manager', 'file_manager' 추가
import parking_spot_manager
import file_manager

def start_process(path):
    str_list = file_manager.read_file(path)     # 주어진 주소의 텍스트 파일을 한 줄씩 'str_list' 리스트에 하나의 문자열로 저장
    p = []      # parking_spot 클래스 원소를 저장할 리스트 'p' 선언
    for i in range(len(str_list)):      # 읽은 텍스트 파일의 줄 수만큼 반복
        data = str_list[i].split(',')       # 읽은 텍스트 파일의 줄을 쉼표(',')로 구분하여 'data' 리스트에 저장
        name = data[1]      # name부터 latitude까지 리스트 'data'에서 올바른 값을 저장
        city = data[2]
        district = data[3]
        ptype = data[4]
        longitude = data[5]
        latitude = data[6]
        # 저장한 데이터를 인자로 'parking_spot' 클래스 객체 't' 선언
        t = parking_spot_manager.parking_spot(name, city, district, ptype, longitude, latitude)
        p.append(t)     # 'parking_spot' 클래스 객체 't'를 리스트 'p'에 추가
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            # 'parking_spot_manager' 모듈의 'print_spots' 함수를 호출해 저장해 둔 리스트 'p'를 출력
            parking_spot_manager.print_spots(p)
        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                # parking_spot 클래스의 객체 리스트 'p'를 이름(입력받은 키워드)으로 필터링
                p = parking_spot_manager.filter_by_name(p, keyword)
            elif select == 2:
                keyword = input('type city:')
                # parking_spot 클래스의 객체 리스트 'p'를 도시(입력받은 키워드)로 필터링
                p = parking_spot_manager.filter_by_city(p, keyword)
            elif select == 3:
                keyword = input('type district:')
                # parking_spot 클래스의 객체 리스트 'p'를 시 군구(입력받은 키워드)로 필터링
                p = parking_spot_manager.filter_by_district(p, keyword)
            elif select == 4:
                keyword = input('type ptype:')
                # parking_spot 클래스의 객체 리스트 'p'를 유형(입력받은 키워드)으로 필터링
                p = parking_spot_manager.filter_by_ptype(p, keyword)
            elif select == 5:
                # 최소 경도, 최대 경도, 최소 위도, 최대 위도 입력 받기
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                # parking_spot 클래스의 객체 리스트 'p'를 위치(입력받은 키워드)로 필터링
                p = parking_spot_manager.filter_by_location(p, (min_lat, max_lat, min_lon, max_lon))
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")       #"Exit" 출력 후
            break       #반복문 탈출, 종료
        else:
            print("invalid input")