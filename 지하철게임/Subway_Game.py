# 지하철 게임
# 술자리 게임에서 벌칙주를 마신 사람이 다음 게임 지목 할 때 지하철이라고 한다음 호선을 고른다.
# 호선을 고른 후 바로 지하철 노선 중 아무 역이나 순서대로 말해가면서 중복, 마지막역이 나올때까지 
# 계속 역 이름을 말해간다.
# 끝까지 가는 경우는 드물고 보통 중복이나 기억 못해서 벌칙주를 마시는게 대부분이다.
# 중복만 아니면 되기 때문에 잘 기억하고 있다가 순서 상관없이 먼저 말하면 된다.


# 게임 초기값 설정
# ======================================================================================================
# 반복문에 사용
i = 0
# 3호선 역이름
Line1 = {'소요산역', '동두천역', '보산역', '동두천중앙역', '지행역', '덕정역', '덕계역', '양주역', '녹양역', '가능역', '의정부역', '회룡역', '망월사역',
        '도봉산역', '도봉역', '방학역', '창동역', '녹천역', '월계역', '광운대역', '석계역', '신이문역', '외대앞역', '회기역', '청량리역', '제기동역', '신설동역', '동묘앞역',
        '동대문역', '종로5가역', '종로3가역', '종각역', '시청역', '서울역', '남영역', '용산역', '노량진역', '대방역', '신길역', '영등포역', '신도림역', '구로역', '구일역',
        '개봉역', '오류동역', '온수역', '역곡역', '소사역', '부천역', '중동역', '송내역', '부개역', '부평역', '백운역', '동암역', '간석역', '주안역', '도화역', '제물표역',
        '도원역', '동인천역', '인천역', '가산디지털단지역', '독산역', '금천구청역', '석수역', '관악역', '안양역', '명학역', '금정역', '군포역', '당정역', '의왕역', '성균관대역',
        '화서역', '수원역', '세류역', '병점역', '세마역', '오산대역', '오산역', '진위역', '송탄역', '서정리역', '지제역', '평택역', '성환역', '직산역', '두정역', '천안역', '봉명역',
        '쌍용역', '아산역', '배방역', '온양온천역', '신창역', '광명역', '서동탄역'}

Line2 = {'시청역', '을지로입구역', '을지로3가역', '을지로4가역', '동대문역사문화공원역', '신당역', '상황십리역', '한양대역', '뚝섬역', '성수역', '건대입구역', '구의역', '강변역', '잠실나루역',
        '잠실역', '잠실새내역', '종합운동장역', '삼성역', '선릉역', '역삼역', '강남역', '교대역', '서초역', '방배역', '사당역', '낙성대역', '서울대입구역', '봉천역', '신림역', '신대방역',
        '구로디지털단지역', '대림역', '신도림역', '문래역', '영등포구청역', '당산역', '합정역', '홍대입구역', '신촌역', '이대역', '아현역', '충정로역', '용답역', '신답역', '용두역', '신설동역',
        '도림천역', '양천구청역', '신정네거리역', '까치산역'}

Line3 = {'대화역', '주엽역', '정발산역', '마두역', '백석역', '대곡역', '화정역', '원당역', '원흥역', '삼송역', '지축역', '구파발역', '연신내역', '불광역', '녹번역', '홍제역', '무악재역', '독립문',
        '경복궁역', '안국역', '종로3가역', '을지가로3가역', '충무로역', '동대입구역', '약수역', '금호역', '옥수역', '압구정역', '신사역', '잠원역', '고속터미널역', '교대역', '남부터미널역', '양재역',
        '매봉역', '도곡역', '대치역', '학여울', '대청역', '일원역', '수서역', '가락시장역', '경찰병원역', '오금역'}

Line4 = {'오이도역', '정왕역', '신길온천역', '안산역', '초지역', '고잔역', '중앙역', '한대앞역', '상록수역', '반월역', '대야미역', '수리산역', '산본', '금정역', '범계역', '평촌역', '인덕원', '정부과천청사역',
        '과천역', '대공원역', '경마공원역', '선바위역', '남태령역', '남태령역', '사당역', '총신대입구역', '동작역', '이촌역', '신용산역', '삼각지역', '숙대입구역', '서울역', '회현역', '명동역', '충무로역',
        '동대문역사문화공원역', '동대문역', '혜화역', '한성대입구역', '성신여대입구역', '길음역', '미아사거리역', '미아역', '수유역', '쌍문역', '창동역', '노원역', '상계역', '당고개역'}

# 선택한 라인을 가지고 올 리스트
ingameLine = []

# 중복을 걸러내기 위한 리스트
sameStation = []


# 진행 게임 설명
# ======================================================================================================
gameRule = (''' 
\n안녕하세요. 이 게임은 술 자리에서 즐겨하던 지하철 게임을 만들어 보았습니다.
룰은 순서 상관없이 중복하지 않고 역 이름을 다 입력하는 것입니다. 
중복하거나 해당 호선에서 제일 마지막으로 나온 역 이름을 입력한 사람이 벌칙을 받게 됩니다.

게임 방법
1. 게임 메뉴에서 원하시는 숫자를 입력해 다음 단계로 나아갑니다.
메뉴 선택은 숫자만 입력해주세요. 1.게임시작을 선택시 숫자 '1'만 입력해주시면 됩니다.

1. 먼저 참여 인원을 입력해주세요! 그냥 숫자로만 입력해주시면 됩니다. 
4명이 참여 한다면 숫자 '4'만 입력해주세요

2. 호선을 골라 주셔야합니다. 참여 인원과 마찬가지로 숫자만 입력해주세요. 
3호선이면 숫자 '3'만 입력해주세요

3. 지하철 역이름은 00역 이렇게 끝까지 입력을 해주시고 오타가 있으면 안됩니다.
대화역 입력하고 싶으면 '대화역' 이렇게 입력해주세요. '대화', '데화역' 과 같은 오타는 벌칙으로 간주됩니다.

4. 역이름이 부지명과 같이 있는 경우는 본 이름만 입력해주세요.
청량리(서울시립대입구)역 -> 쳥량리역
''')

print(gameRule)

while True:
    # 게임 초기 메뉴
    print('1. 게임시작 2. 게임설명 3. 게임종료')
    gameMenu = int(input('번호를 입력해주세요 : '))
    if gameMenu == 1:
        # 진행 게임 설정
        # ======================================================================================================
        # 참여자 인원 수
        member = int(input('\n참여 인원을 설정해 주세요 : '))
        print(member, '명이 참여하였습니다.')
        # 몇 호선인지 선택
        print('''\n호선을 선택해 주세요
1. 서울지하철 1호선 2. 서울지하철 2호선 3. 서울지하철 3호선 4. 서울지하철 4호선
''')
        gameLine = int(input('호선 숫자만 입력 : '))
        if gameLine == 1:
            ingameLine = Line1
            print('1호선 선택\n')
            print(ingameLine)
        elif gameLine == 2:
            ingameLine = Line2
            print('2호선 선택\n')
            print(ingameLine)
        elif gameLine == 3:
            ingameLine = Line3
            print('3호선 선택\n')
            print(ingameLine)
        else:
            ingameLine = Line4
            print('4호선 선택\n')
            print(ingameLine)

        
        
        # 게임 시작
        # ======================================================================================================
        for i in range(member):
            stationName = input('\n지하철 역 이름을 입력해주세요 : ')
            if stationName in ingameLine:
                if stationName in sameStation:
                    print('\n',i+1,'번 역 이름 중복. 탈락입니다!!\n')      
                    break      
                else:
                    print('\n',i+1,'번 통과!')
                    sameStation.append(stationName)   
            else:
                print('\n',i+1,'번 벌칙 당첨입니다!')
                break
    elif gameMenu == 2:
        print(gameRule)
    else:
        break