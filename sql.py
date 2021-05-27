import define_db


def init():
    result = define_db.Kyoto_nakagyo_m.query.all()
    area = [[r.id, r.prefectures, r.city, r.ward, r.town, r.polygon] for r in result]
    return area