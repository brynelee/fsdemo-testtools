# coding=utf-8
from mysql_dbconn import QdasSql
import faker
import time
def aa():
    for i in range(1000, 2000):
        # ??faker ????????
        fake = faker.Faker("zh_CN")
        user_name = fake.name()
        click_url = fake.url()
        timestring = int(round(time.time() * 1000))
        # ??insert into ???????format ???
        sql = "insert into testdb.testtable1 values ('{}','{}','{}')".format(user_name, click_url, i)
        print("?????===", timestring)
        sq = QdasSql()
        # ??????????????
        sq.execute_commit(sql)

if __name__ =="__main__":
    aa()
