'''
    집합데이터형 (자바 => Collection)
    1. list=> List / ArrayList, Array
        = 중복데이터를 허용
        = 인덱스번호 => 순서가 존재
        = name={"","","",""...
            일차원 배열
            
            데이터 수집 (크롤링,데이터베이스)
                    |
                데이터를 모아서 관리(CSV,TXT)
                        |
                    분석 (Numpy,phndas)
                        |
                    시각화 (Mathplotib,Seaborn
                        |
                    완료 => 데이터베이스 누적

'''
names=["홍길동","심청이","이순신","강감찬","박문수",]
print(names)
for name in names:
    print(name);
print(f"인원:{len(names)}")
# 추가 appen => 마지막에 추가
names.append("을지문덕")
names.insert(1,"김두한") #add(index,문자)
print(names)

# 여러개를 동시에 추가
# names.extend(["김유신","춘향이"])
# print(names)
names.sort(reverse=True) # DESC
print(names)
# 삭제
names.remove("홍길동")
print(names)
# 정렬
# 역순 출력