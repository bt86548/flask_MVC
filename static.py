from flask import Flask , request

app = Flask(__name__,static_url_path='/static1',static_folder='./static') #建立flask物件

if __name__ == '__name__':
    app.run(debug=True, host='0.0.0.0',port=5000) #啟動網頁伺服器 一般port為5000in__':
