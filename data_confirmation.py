import define_db

# 全件検索
results = define_db.Kyoto_nakagyo_m.query.all()
for r in results:
    print(r)