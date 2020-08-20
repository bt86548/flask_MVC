# #接收表單資料
# from flask import Flask , request
#
# app = Flask(__name__) #建立flask物件
#
# @app.route('/hello_post',methods = ['GET','POST']) #同時接受兩種get&post方式進行訪問,定義接口可以被訪問
# def hello_post():
#     request_method = request.method #偵測怎樣的方式進行訪問(GET跟POST都有可能)
#     outstr = '' #放置空字串,作為傳入值用
#     if request_method == 'GET':
#         outstr = """
#         <body>
#             <form action = 'hello_post' method = 'POST'>
#                 <input type = "textbox" name="name" >
#                 <button type = "submit">SUBMIT</button>
#             </form>
#         </body>
#         """
#         return outstr
#     elif request_method == 'POST': #因為是post表示有讀取進去資料,要抓到對方輸入資料
#         outstr = """
#              <body>
#                  <form action = 'hello_post' method = 'POST'>
#                      <input type = "textbox" name="name" >
#                      <button type = "submit">SUBMIT</button>
#                  </form>
#              """
#         name = request.form.get('name') #用name來抓取資料
#         outstr += """
#             <div>
#                 Hello {}
#             </div>
#             </body>
#         """.format(name)
#         return outstr
#
#
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0',port=5000) #啟動網頁伺服器 一般port為5000

#接收表單資料(Jinja模板:搭配hello_post html html,加入render_template模組)
from flask import Flask , request,render_template

app = Flask(__name__) #建立flask物件

@app.route('/hello_post',methods = ['GET','POST']) #同時接受兩種get&post方式進行訪問,定義接口可以被訪問
def hello_post():
    request_method = request.method #偵測怎樣的方式進行訪問(GET跟POST都有可能)
    name = ''
    if request_method == 'POST':
        name = request.form.get('name')
    return render_template('hello_post.html',request_method=request_method,name = name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5000) #啟動網頁伺服器 一般port為5000