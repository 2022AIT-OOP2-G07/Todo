import datetime

print(datetime.datetime.now())

# ３．テーブルにデータを追加
#con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(1,'ご飯を食べる','2023-01-12 19:00',false)")
#con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(2,'勉強をする','2023-01-23 17:00',false)")
#con.execute("INSERT INTO todo(id, todo_data, todo_deadline, check_data)values(3,'おせちを食べる','2023-01-01 12:00',true)")
#con.commit()

# 5．データ削除
#con.execute("DELETE FROM todo")
#con.commit()

# 6．テーブル削除
#con.execute("DROP TABLE todo")

# 7．DB接続解除
#con.close()

##データの追加とその時に期限順にソート)
##ソートした後のデータをhtml上に反映させたいからソート後のidを上から順番に取得して
