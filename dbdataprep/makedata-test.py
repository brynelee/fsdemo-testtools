# coding=utf-8
from mysql_dbconn import QdasSql
import faker
import time


def aa():

    fake = faker.Faker("zh_CN")
    user_name = fake.name()
    click_url = fake.url()
    timestring = int(round(time.time() * 1000))
    # ??insert into ???????format ???
    sql = "insert into testdb.bath_table07 values ('{}','{}')".format(
        user_name, click_url)
    print(sql)
    print("?????===", timestring)
    #sq = QdasSql()
    # ??????????????
    #sq.execute_commit(sql)


if __name__ == "__main__":
    aa()
