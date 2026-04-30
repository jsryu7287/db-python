#
# py crud_menu.py 
#
import mysql.connector

# DB 연결
conn = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="db123456"
)

cursor = conn.cursor(dictionary=True)

# ----------------------
# READ (SELECT)
# ----------------------
def select_all():
    cursor.execute("SELECT * FROM menu")
    rows = cursor.fetchall()

    print("\n[전체 조회")
    for row in rows:
        print(row)

def select_coffee_all():
    cursor.execute("SELECT * FROM menu where category_id=1")
    rows = cursor.fetchall()

    print("\n[커피 메뉴 조회]")
    for row in rows:
        print( "{0:20s}\t\t{1}".format(row['menu_name'], row['description']) )

def select_dessert_all():
    cursor.execute("SELECT * FROM menu where category_id=4")
    rows = cursor.fetchall()

    print("\n[디저트 메뉴]")
    for row in rows:
        print( "{0:20s}\t\t{1}".format(row['menu_name'], row['description']) )



# ----------------------
# 메뉴
# ----------------------
def menu():
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

if __name__ == "__main__":
    menu()