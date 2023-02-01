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
        "CREATE TABLE IF NOT EXISTS todo(id integer PRIMARY KEY , todo_data text, todo_deadline datetime, check_data integer DEFAULT 0)")
    con.commit()

    # cur = con.execute("select * from todo order by todo_deadline")
    cur = con.execute(
        "select * from todo where check_data = '0' order by todo_deadline")
    data = cur.fetchall()
    cur.close()

    cur2 = con.execute(
        "select * from todo where check_data = '1' order by todo_deadline")
    check_data = cur2.fetchall()
    cur2.close()

    return render_template('index.html', data=data, check_data=check_data)


@app.route('/add_todo', methods=['POST'])
def add_todo():

    add_todo = request.form.get('todo', None)
    # 上記と同じくadd_limitに格納
    add_limit = request.form.get('limit', None)
    check_todo = 1
    limit_str = add_limit.replace("T", " ")
    con = sqlite3.connect('todo_list.db')
    # データベースにデータを追加
    con.execute("INSERT INTO todo(todo_data, todo_deadline, check_data)values(?,?,?)", [
                add_todo, limit_str, 0])
    con.commit()
    cur = con.execute("SELECT * FROM todo")
    cur = con.execute("select * from todo order by todo_deadline")
    data = cur.fetchall()
    cur.close()
    # return render_template('index.html', data = data)
    return jsonify({'result': 'ok', 'message': '追加のタスクを完了しました。', 'data': data})

#     #     add_id = 0

#     #    # javascriptでフェッチして得たデータの取得
#     #     add_todo = request.form.get('todo', None)
#     #     print(add_todo)
#     #     if len(add_todo) > 30:
#     #         return jsonify({'result': 'error', 'message': '⚠️予定の文字数は30字以内でお願いします'})

#      add_limit = request.form.get('limit', None)
#     # print(add_limit)

#     # limit_str = add_limit.replace("T", " ")
#     # # str = '2021-05-01 17:10:45'

#      con = sqlite3.connect('todo_list.db')

#     cur = con.execute("SELECT * FROM todo")

#     for row in cur:
#         print(row)
#         print(type(row))
#         print(row[0])
#         add_id = row[0]
#     cur.close()

#     add_id += 1

#     if not add_todo:
#         # checked_idがない場合はエラーを返す
#         # JSON形式でエラーである旨をJSに返す
#         return jsonify({'result': 'error', 'message': 'データが正しく受け取れませんでした'})
#     else:

#         # TODOの追加内容をデータベースに反映
#         con = sqlite3.connect('todo_list.db')
#         cur = con.cursor()

#         try:
#             # データベース内に内容の追加
#             # cur.execute('''
#             #    update todo
#             #    set id = ?
#             #    set todo_data = ?
#             #    set limit = ?
#             #    set check_data = false
#             # ''',(add_id+1, add_todo, add_limit))
#             # データ追加(レコード登録)
#             sql = 'insert into todo (id, todo_data, todo_deadline, check_data) values (?,?,?,?)'
#             add_data = (add_id, add_todo, limit_str, False)
#             con.execute(sql, add_data)

#         except sqlite3.Error as e:
#             print("error", e.args[0])
#             return jsonify({'result': 'db_error', 'message': e.args[0]})

#         # 変更をコミット(これをやらないと反映されません)
#         con.commit()
#         # 接続を閉じる
#         # con.close()

#         cur = con.execute("SELECT * FROM todo")
#         for row in cur:
#             print(row)
#             print(type(row))

#         cur = con.execute(
#             "select * from todo where check_data <> 1 order by todo_deadline")
#         data = cur.fetchall()
#         cur.close()

#         # 6．テーブル削除
#         # con.execute("DROP TABLE todo")
#         # 7．DB接続解除

#         # return render_template('index.html', data = data)
#         return jsonify({'result': 'ok', 'message': '追加のタスクを完了しました。', 'data': data})


# checkが押されている項目の削除
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


@app.route("/delete", methods=["POST"])
def delete():
    delete_id = request.form.get('delete_id', None)
    con = sqlite3.connect('todo_list.db')
    con.execute("DELETE FROM todo WHERE id = ?", [delete_id])
    con.commit()


@app.route("/check", methods=["POST"])
def check():
    check_id = request.form.get('check_id', None)
    con = sqlite3.connect('todo_list.db')
    con.execute("UPDATE todo SET check_data = 1 WHERE id = ?", [check_id])
    con.commit()


@app.route("/uncheck", methods=["POST"])
def uncheck():
    check_id = request.form.get('check_id', None)
    con = sqlite3.connect('todo_list.db')
    con.execute("UPDATE todo SET check_data = 0 WHERE id = ?", [check_id])
    con.commit()


if __name__ == '__main__':
    app.debug = True
    app.run()
