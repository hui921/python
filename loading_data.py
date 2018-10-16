#텍스트 데이터 가져오기
import requests
requests.get("http://api.aoiku)


#바이너리 형식으로 이미지 저장
res = request.get("이미지 주소")
with open("logo.png", "wb") as t:
    t.write(res.content)

print("이미지파일이 저장 되었습니다.")