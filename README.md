# Todo List

## アプリの説明
このアプリはタスクを簡単に管理したいという思いから作成しました．
アプリを起動するとmacのメニューバーに予定が表示され，一目で自分がすべきタスクを確認することができます．
タスクの追加，完了，削除はメニューバーからwebサイトにとび，行うことができます．
## こだわり
見やすてくシンプルなデザイン，かつ直感的に使いやすいUI，UXを意識して作りました．

---

## 使い方
### メニューバー
アプリを起動すると，macのメニューバーにアプリのアイコンとともに予定と通知をonかoffにしているか表示されます．
表示される予定は登録してある予定の期限が一番古いものが表示されるようになっています．
通知は表示されている予定の期限になると，macに通知がくるようになっています．通知をonにすると○が，offにすると×が表示されます．
メニューバーをクリックすると「通知」「Webを開く」「Quit」が表示されます．「通知」は予定の通知のon/offを設定できます．「Webを開く」をクリックすると，Todoを管理するWebページが開きます．「Quit」をクリックするとアプリを終了することができます．
### Webページ
Webでは予定の「追加」「完了のチェック」「削除」を行うことができます．
予定の「追加」では，予定を入力フォームに入力し，その予定の期限を選択することで「未実行」のところに予定を追加することができます．
予定の「完了のチェック」では，チェックボックスにチェックすることで予定の完了を行うことができます．これにより，予定は「未実行」から「実行済」に移動します．チェックを外すと予定を「未実行」に移すことができます．
予定の「削除」では，いらなくなった予定を削除することができます．

## Initial Setting
`$ git clone https://github.com/2022AIT-OOP2-G07/Todo.git`

`$ cd Todo`

`$ python -m venv .env`

`$ source .env/bin/activate`

`(.env) $ pip install flask`

`(.env) $ pip install rumps`
### Require
Python version : 3.10
`Flask==2.2.2`

`rumps==0.4.0`
## Usage
### アプリケーションの起動
`$ (.env) $ python app.py`

`$ (.env) $ python menubar.py`

---

## 仕様
### 言語
-  Python：サーバ，DBの管理，メニューバーの作成，通知の管理
-  HTML：Webページの表示
-  CSS：Webページの表示
-  Java Script：Webページの表示
-  SQL：DBの操作
### ライブラリ
- Flask：サーバーの構築
- rumps：メニューバーへTodoの表示，macに通知を送る
### データ
- SQLite：予定の保存
- JSON：アプリの設定情報を追加

---

## 課題
- menubar.pyを実行時にapp.pyも同時に実行させる
- 予定の「編集」機能の追加
- メニューバーをクリックしたときに，予定の一覧を表示
- 予定の完了である「完了のチェック」をメニューバーからでも行えるようにする
- アプリのapp化
Pythonのライブラリ「py2app」を用いてapp化
