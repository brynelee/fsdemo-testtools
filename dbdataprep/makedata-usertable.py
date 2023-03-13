# coding=utf-8
from mysql_dbconn import QdasSql
import faker
import time


def aa():
    
    for i in range(10, 10000):

        fake = faker.Faker("zh_CN")

        user_name = fake.user_name()

        password = "666666"
        
        mobile = fake.phone_number()

        status = 1

        email = fake.email()
        
        personal_id = fake.ssn()

        sql = "insert into testdb.usertable values ('{}','{}','{}', NULL , NULL, '{}','{}','{}','{}')".format(
            user_name, password, i, mobile, status, email, personal_id)
        print(sql)

        sq = QdasSql()
        sq.execute_commit(sql)


if __name__ == "__main__":
    aa()
