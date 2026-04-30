#
# py crud_menu.py 
#
import mysql.connector

# DB 연결
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootroot",
    database="db123456"
)

cursor = conn.cursor(dictionary=True)

# ----------------------
# CREATE (INSERT)
# ----------------------
def insert_data():
    name = input("이름 입력: ")
    city = input("도시 입력: ")

    sql = "INSERT INTO test_tbl (name, city) VALUES (%s, %s)"
    cursor.execute(sql, (name, city))
    conn.commit()

    print("INSERT 완료! ID:", cursor.lastrowid)


# ----------------------
# READ (SELECT)
# ----------------------
def select_all():
    cursor.execute("SELECT * FROM test_tbl")
    rows = cursor.fetchall()

    print("\n[전체 조회 결과]")
    for row in rows:
        print(row)


# ----------------------
# UPDATE
# ----------------------
def update_data():
    user_id = input("수정할 ID: ")
    name = input("새 이름: ")
    city = input("새 도시: ")

    sql = "UPDATE test_tbl SET name=%s, city=%s WHERE id=%s"
    cursor.execute(sql, (name, city, user_id))
    conn.commit()

    print("UPDATE 완료! 수정된 행:", cursor.rowcount)


# ----------------------
# DELETE
# ----------------------
def delete_data():
    user_id = input("삭제할 ID: ")

    sql = "DELETE FROM test_tbl WHERE id=%s"
    cursor.execute(sql, (user_id,))
    conn.commit()

    print("DELETE 완료! 삭제된 행:", cursor.rowcount)


# ----------------------
# 메뉴
# ----------------------
def menu():
    while True:
        print("\n===== 메뉴 =====")
        print("1.조회   2.입력   3.갱신   4.삭제   0.종료")

        choice = input("번호 선택: ")

        if choice == "1":
            select_all()
        elif choice == "2":
            insert_data()
        elif choice == "3":
            update_data()
        elif choice == "4":
            delete_data()
        elif choice == "0":
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    menu()