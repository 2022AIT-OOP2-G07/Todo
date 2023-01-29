# ０．sqlite3をインポート。これがないと始まらない
import sqlite3
from flask import Flask, render_template, request, g, jsonify
import datetime

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def todo_db():

    # １．DB接続。ファイルがなければ作成する
    con = sqlite3.connect('todo_list.db')
    # ２．テーブル作成
    con.execute(
        "CREATE TABLE IF NOT EXISTS todo(id integer PRIMARY KEY AUTOINCREMENT, todo_data text, todo_deadline datetime,check_data boolean)")
    con.commit()
    # 3．データ参照
    cur = con.execute("SELECT * FROM todo")
    # 4. データを締切の近い順に並び替え
    cur = con.execute("select * from todo order by todo_deadline")

    data = cur.fetchall()
    cur.close()

    return render_template('index.html', data=data)


@app.route('/add_todo', methods=['POST'])
def add_todo():

    # javascriptでフェッチして得たデータの取得
    add_todo = request.form.get('todo', None)
    # 上記と同じくadd_limitに格納
    add_limit = request.form.get('limit', None)
    con = sqlite3.connect('todo_list.db')
    # データベースにデータを追加
    con.execute("INSERT INTO todo(todo_data, todo_deadline)values(?,?)", [
                add_todo, add_limit])
    con.commit()
    cur = con.execute("SELECT * FROM todo")
    cur = con.execute("select * from todo order by todo_deadline")
    data = cur.fetchall()
    cur.close()
    # return render_template('index.html', data = data)
    return jsonify({'result': 'ok', 'message': '追加のタスクを完了しました。', 'data': data})


@app.route('/register_done', methods=['POST'])
def register_done():

    # htmlで入力したデータの取得
    checked_id = request.form.get('checked_id', None)
    print(checked_id)

    if not checked_id:
        # checked_idがない場合はエラーを返す
        # JSON形式でエラーである旨をJSに返す
        return jsonify({'result': 'error', 'message': 'データが正しく受け取れませんでした'})
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
            ''', (checked_id, ))  # id = ?の部分にchecked_idをセットしています

        except sqlite3.Error as e:
            print("error", e.args[0])
            return jsonify({'result': 'db_error', 'message': e.args[0]})

        # 変更をコミット(これをやらないと反映されません)
        con.commit()
        # 接続を閉じる
        con.close()

    # エラーなく登録できたら正常終了のメッセージを返します
    return jsonify({'result': 'ok', 'message': f'{ checked_id }のタスクを完了しました。'})


@app.route("/delete", methods=["POST"])
def delete():
    delete_id = request.form.get('delete_id', None)
    con = sqlite3.connect('todo_list.db')
    con.execute("DELETE FROM todo WHERE id = ?", [delete_id])
    con.commit()


@app.route('/edit_todo', methods=['POST'])
def edit_todo():

    # javascriptでフェッチして得たデータの取得
    e_id = request.form.get('e_id', None)
    e_todo = request.form.get('e_todo', None)
    print(e_id)
    print(e_todo)
    if not e_todo:
        # e_todoがない場合はエラーを返す
        return jsonify({'result': 'error', 'message': 'pythonにデータが正しく受け取れませんでした'})
    else:
        # TODOのタスク完了をデータベースに反映
        con = sqlite3.connect('todo_list.db')
        cur = con.cursor()

        try:
            # 削除(delete)処理ではなく、check_data列に1を設定して更新(update)する方法
            # UPDATE文を実行(変数となる部分を?で指定して、後から値をセットしています)
            cur.execute('''
                update todo
                set todo_data = ?
                where id = ?
            ''', (e_todo, e_id))  # id = ?の部分にchecked_idをセットしています

        except sqlite3.Error as e:
            print("error", e.args[0])
            return jsonify({'result': 'db_error', 'message': e.args[0]})

        # 変更をコミット(これをやらないと反映されません)
# con.commit()
#     # JSON形式でエラーである旨をJSに返す

# cur = con.execute("select * from todo where check_data <> 1 order by todo_deadline")
# data = cur.fetchall()
# print(data)
#             #con.close()
# cur.close()
#     #return jsonify({'result': 'error', 'message': 'pythonにデータが正しく受け取れました。'})
#         # エラーなく登録できたら正常終了のメッセージを返します
# return jsonify({'result': 'ok', 'message': f'{ e_id }のタスクを完了しました。' }, data = data)


#         cur = con.execute("select * from todo where check_data <> 1 order by todo_deadline")
#         data = cur.fetchall()
#         cur.close()
#     #return jsonify({'result': 'error', 'message': 'pythonにデータが正しく受け取れました。'})
#         # エラーなく登録できたら正常終了のメッセージを返します
#         return jsonify({'result': 'ok', 'message': f'{ e_id }のタスクを完了しました。' }, data = data)

        con.commit()
    # JSON形式でエラーである旨をJSに返す

        cur = con.execute(
            "select * from todo where check_data <> 1 order by todo_deadline")
        data = cur.fetchall()
        print(data)
        # con.close()
        cur.close()
    # return jsonify({'result': 'error', 'message': 'pythonにデータが正しく受け取れました。'})
        # エラーなく登録できたら正常終了のメッセージを返します
        return jsonify({'result': 'ok', 'message': f'{ e_id }のタスクを完了しました。'}, data=data)


if __name__ == '__main__':
    app.debug = True
    app.run()
