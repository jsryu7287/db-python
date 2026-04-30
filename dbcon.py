import mysql.connector

# DB 연결
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="db123456"
)

# 커서 생성
cursor = conn.cursor()

print("MySQL 연결 성공!")

# 쿼리 실행
sql = "SELECT * FROM test_tbl"
cursor.execute(sql)

# 결과 가져오기
rows = cursor.fetchall()

# 출력
for row in rows:
    print(row)


# 연결 종료
cursor.close()
conn.close()