import define_db
# from shapely.geometry import Polygon


def init():
    result = define_db.Kyoto_nakagyo_m.query.all()
    area = [[r.id, r.prefectures, r.city, r.ward, r.town, r.polygon]
            for r in result]
    return area

# def polygon_center():
#     result = define_db.Kyoto_nakagyo_m.query.all()
#     polygon_list = [r.polygon for r in result]

#     return polygon_center

