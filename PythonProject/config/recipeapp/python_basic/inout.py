'''
    파일 입출력
    => 특화된 언어 (데이터 수집) = 파일 저장
    => 데이터 분석 (Numpy, Pandas , konlp => 형태소 분석
    => 웹사이트는 많이 사용하지 않는다
          | 스프링과 연동 , MSA
           ----------------- 웹 = 웹 연결 (JSON)
    형식) 파일 => 단방향 / 읽기 / 쓰기
          1. 파일열기
             f=open(경로명,모드) => c:\ c:/
                          ----
                          w(생성/쓰기) / r(읽기) / a(추가)
         2. 파일 닫기
            f.close()

        3. 예외처리 

'''
def writedata():
    try:
        f=open("c:/pydata/student.txt","w") #=> w:create파일 생성 내용 저장
        for i in range(1,11):
            data="홍길동 %d\n" %i
            f.write(data)
        f.close()
        print("파일 저장 완료!!")
    except Exception as e:
        print("파일 에러:",e)
#writedata()
def readdata():
    try:
        f=open("c:/pydata/student.txt",'r')
        # r모드는 읽기 = create는 안된다
        while 1: # True => 0이 아닌 모든 수는 True
            line=f.readline() #한줄씩 읽어온다
            if not line: # if(line==null)
                break
            print(line)
        f.close()
    except Exception as e:
        print(e)
readdata()
def readdates():
    try:
        f=open("c:/pydata/student.txt","r")
        lines=f.readlines() #전체를 한번에 읽어 온다
        # list => []
        '''
            데이터 여러개를 읽기
            데이터베이스 : () tuple
            일반 파일 : [] list
            파일 (JSON) : {} => dict
        '''
        print(lines)
        for line in lines:
            print(line)
        f.close()
    except Exception as e:
        print(e)
#readdates()
# with => 파일을 자동으로 닫기게 만든다 => f.close()
def readWithdata():
    try:
        with open("c:/pydata/student.txt","r") as f:
            line=f.readline()
            print(line)
        #f.close()
    except Exception as e:
        print(e)