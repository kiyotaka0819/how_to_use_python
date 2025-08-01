# FlaskというWebフレームワークをimport
from flask import Flask, render_template, request

# Flask()アプリケーションのインスタンスを作成
# __name__は現在のモジュール名を示す特別な変数
app = Flask(__name__) 

# `@`　はデコレーターという
# 「'/'」はルートURLを示すWebページのパス
@app.route('/')

# `def` でhello関数を定義
# トップページにアクセスがあったときに、この関数が動く
def hello():
    # `render_template`は、HTMLテンプレートをレンダリングする関数
    return render_template('test.html')

# フォームからデータを受け取るルート
# `methods=['POST']`にすることで、フォームの送信（POSTリクエスト）だけを受け付ける
@app.route('/register', methods=['POST'])
def register():

    name = request.form.get('name')
    email = request.form.get('email')
    return render_template('ororon.html', name=name, email=email)

# `if __name__ == '__main__':` は、Pythonの標準的な書き方
# これにより、他のモジュールからインポートされたときには
# この部分のコードは実行されない
if __name__ == '__main__':
    # Webアプリを起動する命令
    # debug=Trueにしとくと、コードを書き換えたときに
    # 自動的にWebアプリが再起動する
    # これで開発が楽になる
    app.run(debug=True)