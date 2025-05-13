import re

txt="Field. Friend fr!end"
#단어
n=re.findall(r'ie',txt)
print(n)

txt="""
    6·3대선 공식선거운동이 시작된 12일 주요 정당이 발표한 이번 대선 10대 공약에는 
    분권·균형발전을 위한 정책 방향도 담겼다. 더불어민주당 이재명 후보는 ‘5극 3특’을, 
    국민의힘 김문수 후보는 ‘전국에 GTX 건설’을, 개혁신당 이준석 후보는 ‘조세 등의 지방권한 확대’를 분권·균형발전 공약의 간판으로 삼았
    """
# [가-힣] => Konlp
n=re.findall(r'[가-힣]+',txt)
print(n)
print(len(n))

n=re.findall(r'[0-9]+',txt)
print(n)
text = "123456 23456"
print(re.findall(r'234',text))
txt1="white space"
txt2="white space"
print(re.findall(r"e\ss",txt1))
print(re.findall(r"e\ss",txt2))
# a2f aaa 15f
# ^ , $
txt="this this this this"
print(re.sub(r"^this","Begin",txt))
print(re.findall(r"this$",txt))
print(re.sub(r"this$","End",txt))
# 중괄호
txt="Teth Teeth Teeeth TeeeTh"
print(re.findall(r"Te{1,4}Th",txt))
print(re.findall(r"Te{0,1}th",txt))
# *(0이상) , +(1이상)
txt="Tth Teth Teeth Teeeth Taskfsfsfsfs"
print(re.findall(r"Te*th",txt))
# Te*th => Te시작 문자는 0이상 th로 종료
# Youtube 동영상 키
print(re.findall(r"Te+th",txt))
print(re.findall(r"T[^e]*th",txt))
# e를 제외한 문자가 여러개 0개 존재
txt=("""
    211.238.142.101 127.0.0.1 123,123,123
    """)
n=re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",txt)
print(n)
n=re.findall(r"\d+",txt)
print(n)

txt='"abcd" <abcd>'
n=re.findall(r"<[^>]*>",txt)
# < => >제외 => 문자여러개 >
print(n)

# () => 그룹
"""
    (([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3}))\.([0-9]{1,3})
    ----------------------------------------  ------------
            회사번호                              고유번호
"""
txt="My Phone number is 010-1111-1111"
match=re.search(r"(\d{3})-(\d{4})-(\d{4})",txt)
print(match)

if match:
    print("번호 전체:",match.group(0))
    print("Area :", match.group(1))
    print("Prifix :", match.group(2))
    print("Line :", match.group(3))
    print(match.groups())
# search => 없는 경우 : none 
# 문자 대체 => sub
# 찾기 => findall
# 단어 => 긍정 / 부정 => 데이터사전 => 가중치
# 트위터 / 페이스북 => 대선
# 정규식은 문자열의 형태를 만들어서 찾는다
# ---- 오라클 / MySQL regexp_like()
# split(정규식) replaceAll(정규식)