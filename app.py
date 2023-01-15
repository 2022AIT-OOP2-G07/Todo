# ０．sqlite3をインポート。これがないと始まらない
import sqlite3
from flask import Flask,render_template,request,g, jsonify
import datetime

app = Flask(__name__)


@app.route('/')
def todo_db():
# １．DB接続。ファイルがなければ作成する
    con = sqlite3.connect('todo_list.db')
    # ２．テーブル作成
    con.execute("CREATE TABLE IF NOT EXISTS todo(id integer PRIMARY KEY, todo_data text,todo_time datetime default (DATETIME('now','locatetime')), todo_deadline datetime, check_data boolean)")
    # ３．テーブルにデータを追加
   

    #print(p_email)
    #con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'ご飯を食べる','2023-01-12 19:00',false)")
    #con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'勉強をする','2023-01-23 17:00',false)")
    #con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'おせちを食べる','2023-01-01 12:00',false)")
    #con.execute("INSERT INTO todo(id, todo_data, todo_time, todo_deadline, check_data)values(4,'掃除をする',datetime.now(),'2023-01-01 12:00',true)")
    #con.commit()

    # 5．データ削除
    #con.execute("DELETE FROM todo WHERE id = 1")
    #con.execute("DELETE FROM todo WHERE id = 2")
    ##con.execute("DELETE FROM todo WHERE id = 3")
    con.commit()
    # ４．データ参照
    cur = con.execute("SELECT * FROM todo")
    for row in cur:
        print(row)
        print(type(row))

    cur = con.execute("select * from todo where check_data <> 1 order by id")
    data = cur.fetchall()
    cur.close()

    # 6．テーブル削除
    ##con.execute("DROP TABLE todo")
    # 7．DB接続解除

    return render_template('index.html', data = data)


# checkが押されている項目の削除
@app.route('/register_done', methods=['POST'])
def register_done():

    # htmlで入力したデータの取得
    checked_id = request.form.get('checked_id', None)
    print(checked_id)

    if not checked_id:
        # checked_idがない場合はエラーを返す
        return jsonify({'result': 'error', 'message': 'データが正しく受け取れませんでした'})     # JSON形式でエラーである旨をJSに返す
    else:
        # TODOのタスク完了をデータベースに反映
        con = sqlite3.connect('todo_list.db')
        cur = con.cursor()

        try:
            # 削除(delete)処理ではなく、check_data列に1を設定して更新(update)する方法
            # UPDATE文を実行(変数となる部分を?で指定して、後から値をセットしています)
            cur.execute('''
                update todo
                set check_data = 1
                where id = ?
            ''',(checked_id, )) # id = ?の部分にchecked_idをセットしています

        except sqlite3.Error as e:
            print("error",e.args[0])
            return jsonify({'result': 'db_error', 'message': e.args[0] })
            
        # 変更をコミット(これをやらないと反映されません)
        con.commit()
        # 接続を閉じる
        con.close()

    # エラーなく登録できたら正常終了のメッセージを返します
    return jsonify({'result': 'ok', 'message': f'{ checked_id }のタスクを完了しました。' })



if __name__ == '__main__':
    app.debug = True
    app.run()




