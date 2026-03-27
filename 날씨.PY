import requests
from bs4 import BeautifulSoup

def get_naver_weather(location):
    # 네이버에 '지역 + 날씨'로 검색한 결과 페이지를 가져옵니다.
    search_url = f"https://search.naver.com/search.naver?query={location}+날씨"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        # 현재 온도 추출 (네이버 날씨 영역의 클래스명 기준)
        current_temp = soup.select_one(".temperature_text > strong").text
        # "현재 온도20.5°" 형태에서 숫자만 추출
        temp_value = float(current_temp.replace("현재 온도", "").replace("°", "").strip())
        return temp_value
    except Exception as e:
        print("날씨 정보를 가져오는 데 실패했습니다.")
        return None

def suggest_outfit(temp):
    print(f"\n🌡️ 현재 기온: {temp}°C")
    
    if temp >= 28:
        outfit = "민소매, 반바지, 원피스"
    elif 23 <= temp < 28:
        outfit = "반팔, 얇은 셔츠, 반바지"
    elif 20 <= temp < 23:
        outfit = "긴팔 티, 가디건, 후드티, 슬랙스"
    elif 17 <= temp < 20:
        outfit = "니트, 가디건, 맨투맨, 청바지"
    elif 12 <= temp < 17:
        outfit = "자켓, 야상, 청바지"
    elif 9 <= temp < 12:
        outfit = "트렌치코트, 간절기 코트"
    elif 5 <= temp < 9:
        outfit = "코트, 가죽 자켓, 히트텍"
    else:
        outfit = "패딩, 두꺼운 코트, 목도리"
    
    return f"👗 추천 옷차림: {outfit}"

# 실행
location = input("날씨를 확인할 지역을 입력하세요 (예: 서울, 부산): ")
temp = get_naver_weather(location)

if temp is not None:
    print(suggest_outfit(temp))