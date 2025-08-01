# FlaskというWebフレームワークをimport
from flask import Flask, render_template

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

# `if __name__ == '__main__':` は、Pythonの標準的な書き方
# これにより、他のモジュールからインポートされたときには
# この部分のコードは実行されない
if __name__ == '__main__':
    # Webアプリを起動する命令や
    # debug=Trueにしとくと、コードを書き換えたときに
    # 自動的にWebアプリが再起動する
    # これで開発が楽になる
    app.run(debug=True)