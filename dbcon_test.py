#
# pip install mysql-connector-python
#
# pip 가 설치되어 있지 않다면, 위 명령어로 설치 후 실행하세요.
#       python -m pip install mysql-connector-python
#       또는 
#       py -m pip install mysql-connector-python
# 
# Python 설치 경로
# C:\Users\사용자계정\AppData\Local\Programs\Python\Python314\python.exe -m pip install --upgrade pip
# C:\Users\사용자계정\AppData\Local\Programs\Python\Python314\Scripts\pip.exe install mysql-connector-python
# 환경 변수 편집:
#   Win + S 누르고 "시스템 환경 변수 편집" 검색 및 실행.
#    C:\Users\사용자계정\AppData\Local\Programs\Python\Python314
#    C:\Users\사용자계정\AppData\Local\Programs\Python\Python314\Scripts
# 
import mysql.connector
from mysql.connector import Error

def fetch_example_records():
    connection = None
    try:
        # 1. 데이터베이스 연결 설정
        connection = mysql.connector.connect(
            host='localhost',          # 호스트 주소
            user='root',      # MySQL 아이디
            password='rootroot',  # MySQL 비밀번호
            database='db123456'    # 연결할 데이터베이스 이름
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"MySQL 서버 버전 {db_info}에 연결되었습니다.")

            # 2. 커서(Cursor) 생성
            cursor = connection.cursor(dictionary=True) # dictionary=True 설정 시 결과를 dict 형태로 반환

            # 3. SQL 쿼리 실행
            query = "SELECT * FROM test_tbl"
            cursor.execute(query)

            # 4. 결과 페치(Fetch) 및 출력
            records = cursor.fetchall()
            print(f"총 레코드 수: {cursor.rowcount}")

            print("\n--- [example 테이블 데이터] ---")
            for row in records:
                print(row)

    except Error as e:
        print(f"Error: {e}")

    finally:
        # 5. 연결 종료 (자원 해제)
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("\nMySQL 연결이 안전하게 종료되었습니다.")

if __name__ == "__main__":
    fetch_example_records()