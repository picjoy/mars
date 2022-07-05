from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# DB를 쓸 꺼니까 이 3줄!!
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.epsmx.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta



@app.route('/')
def home():
   return render_template('index.html')

@app.route("/mars", methods=["POST"])
def web_mars_post():
    # name, address, size를 받아서 걔를 저장해라
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    # 그 창구에서 받아다가 DB에서다 저장
    doc = {
        'name' : name_receive,
        'address' : address_receive,
        'size' : size_receive
    }
    db.mars.insert_one(doc)
    # 주문 완료라고 다시 내려 주면
    return jsonify({'msg': '주문 완료!'})

@app.route("/mars", methods=["GET"])
def web_mars_get():
    # DB에서 모든 주문을 다 갖고 오기
    order_list = list(db.mars.find({}, {'_id': False}))

    return jsonify({'orders': order_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)