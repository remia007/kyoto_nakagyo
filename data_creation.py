import pandas as pd
import define_db


def init_table():
    # table init
    define_db.db.drop_all()
    define_db.db.create_all()

def data_init():
    # delete
    define_db.db.session.query(define_db.Kyoto_nakagyo_m).delete()

    # insert
    df = pd.read_csv("data/kyoto_nakagyo_polygon.csv", dtype=str)

    for i in range(len(df)):
        id=df.iloc[i][0]
        prefectures=df.iloc[i][1]
        city=df.iloc[i][2]
        ward=df.iloc[i][3]
        town=df.iloc[i][4]
        polygon=df.iloc[i][5]

        row = define_db.Kyoto_nakagyo_m(id, prefectures, city, ward, town, polygon)
        # registration
        define_db.db.session.add(row)
    # commit
    define_db.db.session.commit()

init_table()
data_init()