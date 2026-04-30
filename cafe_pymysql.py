import pymysql

# 1. 데이터베이스 접속 설정 (본인의 환경에 맞게 수정하세요)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'rootroot',
    'db': 'db123456',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor  # dict 형태로 결과 반환 (row['컬럼명'] 사용 가능)
}

# 전역 변수로 선언
conn = None
cursor = None

def connect_db():
    global conn, cursor
    try:
        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
    except pymysql.MySQLError as e:
        print(f"DB 접속 에러: {e}")
        exit()

# ----------------------
# READ (SELECT)
# ----------------------
def select_all():
    cursor.execute("SELECT * FROM menu")
    rows = cursor.fetchall()

    print("\n[전체 조회]")
    for row in rows:
        # 전체 조회 시에도 가독성을 위해 딕셔너리 전체 출력
        print(row)

def select_coffee_all():
    cursor.execute("SELECT * FROM menu WHERE category_id=1")
    rows = cursor.fetchall()

    print("\n[커피 메뉴 조회]")
    for row in rows:
        # row['컬럼명'] 방식으로 접근
        print("{0:20s}\t\t{1}".format(row['menu_name'], row['description']))

def select_dessert_all():
    cursor.execute("SELECT * FROM menu WHERE category_id=4")
    rows = cursor.fetchall()

    print("\n[디저트 메뉴]")
    for row in rows:
        print("{0:20s}\t\t{1}".format(row['menu_name'], row['description']))

# ----------------------
# 메뉴
# ----------------------
def menu():
    connect_db()  # 프로그램 시작 시 DB 연결
    
    try:
        while True:
            print("\n===== 메뉴 =====")
            print("1.조회   11.커피종류 12.디저트 0.종료")

            choice = input("번호 선택: ")

            if choice == "1":
                select_all()
            elif choice == "11":
                select_coffee_all()
            elif choice == "12":
                select_dessert_all()
            elif choice == "0":
                print("프로그램 종료")
                break
            else:
                print("잘못된 입력입니다.")
    finally:
        # 프로그램 종료 전 자원 해제
        if conn:
            cursor.close()
            conn.close()
            print("DB 연결이 해제되었습니다.")

if __name__ == "__main__":
    menu()