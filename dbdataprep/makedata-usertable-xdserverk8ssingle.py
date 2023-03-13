# coding=utf-8
from mysql_dbconn_xdserverk8ssingle import QdasSql
import faker
import time


def aa():
    
    sq = QdasSql()

    for i in range(37000, 39000):

        fake = faker.Faker("zh_CN")

        user_name = fake.user_name()

        password = "666666"
        
        mobile = fake.phone_number()

        status = 1

        email = fake.email()
        
        personal_id = fake.ssn()

        sql = "insert into usercenter.usertable values ('{}','{}','{}', NULL , NULL, '{}','{}','{}','{}')".format(
            user_name, password, i, mobile, status, email, personal_id)
        print(sql)
        
        sq.execute_commit(sql)

        time.sleep(0.2)


if __name__ == "__main__":
    aa()
    print("successfully done.")
