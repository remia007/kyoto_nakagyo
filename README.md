Flask and Leaflet(練習用)
=================

Clone:
```
git clone https://github.com/remia007/kyoto_nakagyo.git
```


Python Version:

```
3.9.1
```

Polygon data:
```
https://uedayou.net/loa/京都府京都市
```

Install dependencies:

```
pip install flask
pip install flask_sqlalchemy

// 以下はデータ作成用のため、アプリ起動には必要ない
pip install requests
pip install pandas
pip install bs4
```

Create DB:
```
python data_creation
```

Start server:

```
python app.py
```

View the demo by navigating to `http://localhost:5000`
