from flask import Flask , request

app = Flask(__name__) #建立flask物件

@app.route('/hello_get') #接收查詢字的參數
def hello_get():
    name = request.args.get('name')
    age = request.args.get('age')
    return 'hello {}, you are {} years old'.format(name,age)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000) #啟動網頁伺服器 一般port為5000