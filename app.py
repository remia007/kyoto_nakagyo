from flask import Flask, render_template, jsonify, request
import define_db
import sql


@define_db.app.route('/')
def index():
    return render_template('index.html')


@define_db.app.route('/init')
def init():
    result = sql.init()
    return jsonify({"data": result})


# @define_db.app.route('/center')
# def polygon_center():
#     result = sql.polygon_center()
#     return jsonify({"data": result})

if __name__ == '__main__':
    define_db.app.run(debug=True)
