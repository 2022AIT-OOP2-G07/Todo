

document.querySelectorAll("input[id^=fav-]").forEach((elm) => {
    elm.addEventListener('change', (ev) => {
        // チェックボックスの値が変更されたときに実行される
        
        console.log(elm)
        console.log(elm.checked)
        console.log(elm.value)
        if (elm.checked) {
            // flaskへ送信するデータを用意する
            const postdata = new FormData()
            postdata.append("checked_id", elm.value) // チェックした行のIDを設定

            // fetch
            // "/register_done" としてタスクをこなしたことを登録する。
            // この変更は、flask側(app.py)の処理も変更しています。
            fetch('/register_done', {
                method: 'POST',
                body: postdata  // IDデータが入ったFormDataを送信
            }).then((response) => {
                // 正常にHTTPリクエストが通った
                console.log(response)

                // レスポンスデータからJSONを取り出し
                response.json().then((data) => {
                    console.log(data) // 取得されたレスポンスデータをデバッグ表示
                    
                    // 正常にタスクを完了できているかを確認
                    if (data.result !== "ok") {
                        window.alert(data.message) // エラー表示
                    } else {
                        // タスクを完了できたら、チェックされた行を消す
                        document.querySelector(`#todo_row_id-${ elm.value }`).remove()
                    }
                })
            })
        }
    })
})

