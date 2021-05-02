import sqlite3


class DatabaseUtil:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_db(self):
        conn = sqlite3.connect(self.db_name)
        print('Database ' + self.db_name + ' is created')

        conn.execute('''CREATE TABLE TEMP_REC
                 (ID TEXT PRIMARY KEY     NOT NULL,
                 DATE           INT    NOT NULL,
                 TEMP           REAL     NOT NULL,
                 HOUR           INT      NOT NULL);''')

        conn.execute('''CREATE TABLE PROCESSED_TEMP
                         (DATE INT PRIMARY KEY     NOT NULL,
                         MAX_TEMP           REAL    NOT NULL,
                         MIN_TEMP           REAL     NOT NULL,
                         AVG_TEMP           REAL      NOT NULL);''')
        print("Tables created successfully")

        conn.close()

    def insert_temp_data(self, temp_id, date, temp, hour):
        conn = sqlite3.connect(self.db_name)
        conn.execute("INSERT INTO TEMP_REC (ID,DATE,TEMP,HOUR) \
                      VALUES (" + temp_id + ", " + date + ", " + temp + ", " + hour + ")")

        conn.commit()
        conn.close()

    def insert_processed_data(self, date, max_temp, min_temp, avg_temp):
        conn = sqlite3.connect(self.db_name)
        conn.execute("INSERT INTO PROCESSED_TEMP (DATE,MAX_TEMP,MIN_TEMP,AVG_TEMP) \
                              VALUES (" + date + ", " + max_temp + ", " + min_temp + ", " + avg_temp + ")")

        conn.commit()
        conn.close()

    def get_max_temp(self, day):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.execute("SELECT max(temp) from TEMP_REC where date = " + day)

        for c in cursor:
            return c[0]

        conn.close()

    def get_avg_temp(self, day):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.execute("SELECT avg(temp) from TEMP_REC where date = " + day)

        for c in cursor:
            return c[0]

    def get_min_temp(self, day):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.execute("SELECT min(temp) from TEMP_REC where date = " + day)

        for c in cursor:
            return c[0]
