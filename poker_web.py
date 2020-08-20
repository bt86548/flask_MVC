from flask import Flask , request,jsonify
import poker as p
app = Flask(__name__) #建立flask物件


#網址:loaclhost:5000/poker
@app.route('/poker', methods=['GET', 'POST']) #使用者進入頁面時,會用get方式進入
def poker(): #先用get讀取,當method = post時,用post的方式傳,此時跳到elif做
    if request.method == 'GET':
        outStr = """
        <html>
            <head>
                <title>poker</title>
            </head>
            <body>
                <h1>How many players?</h1>
                <form action="/poker" method="post"> 
                    <input type="textbox" name="players"> 
                    <button type="submit">Submit</button>
                </form>
            </body>
        </html>
        """
        return outStr
    elif request.method == 'POST': #接收資料
        players = request.form.get('players')
        cards = p.poker(int(players)) #players取出來時是字串
        return jsonify(cards) #一般return只能回傳字串,用jsonify轉換成json格式

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000) #啟動網頁伺服器 一般port為5000