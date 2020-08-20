from flask import Flask #引入套件

app = Flask(__name__) #建立flask物件

@app.route('/hello/<username>') #接口名稱(習慣接口名稱與函式名稱相同)
def helloflask(username): #建立接口
    return 'Hello {}'.format(username) #回傳值需要字串

@app.route('/add/<x>/<y>') #接口名稱(習慣接口名稱與函式名稱相同)
def add(x,y): #建立接口
    return '{}'.format(2*int(x)+int(y)) #回傳值需要字串


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000) #啟動網頁伺服器 一般port為5000

