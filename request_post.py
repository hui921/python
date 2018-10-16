# requests 모듈의 메서드
import requests
#http에서 사용하는 데이터 전송 방식 GET, POST 방식

#get방식
r = requests("http://google.com")

#post방식
formData = {"key1":"value1", "key2":"value2"}
r=requests.post("http://sample.com", data=formData)