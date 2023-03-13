# coding=utf-8
from mysql_dbconn import QdasSql
import faker
import time


def aa():

    fake = faker.Faker("zh_CN")

    user_name = fake.user_name()
    print(user_name)

    phone = fake.phone_number()
    print(phone)

    id = fake.ssn()
    print(id)

    email = fake.email()
    print(email)
    

    sql = "insert into testdb.bath_table07 values ('{}','{}')".format(
        user_name, phone)
    print(sql)

    simple_info = fake.simple_profile()
    print(simple_info)

    info = fake.profile()
    print(info)

    #sq = QdasSql()
    # ??????????????
    #sq.execute_commit(sql)


if __name__ == "__main__":
    aa()
