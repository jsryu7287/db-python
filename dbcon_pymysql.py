#
# python -m pip install PyMySQL
# 

import pymysql

# 데이터베이스 접속 정보 설정
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'rootroot',
    'db': 'db123456',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor  # 결과를 딕셔너리로 반환
}

def fetch_data():
    # 1. 연결 시도 (with 문 사용 시 자동 close)
    try:
        with pymysql.connect(**db_config) as connection:
            # 2. 커서 생성
            with connection.cursor() as cursor:
                # 3. SQL 실행
                sql = "SELECT * FROM menu"
                cursor.execute(sql)

                # 4. 전체 데이터 가져오기
                results = cursor.fetchall()

                print(f"조회된 레코드 수: {len(results)}")
                print("-" * 30)
                
                for row in results:
                    # DictCursor 덕분에 컬럼명으로 접근 가능
                    print(row)

    except pymysql.MySQLError as e:
        print(f"접속 중 에러가 발생했습니다: {e}")

if __name__ == "__main__":
    fetch_data()