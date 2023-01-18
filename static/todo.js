

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

document.getElementById("add-submit").addEventListener("click", async (ev) => {
    // ボタンイベントのキャンセル
    ev.preventDefault()
    console.log("addボタン押されたよ！！")

    // 入力チェック
    let todo = document.getElementById("todo").value
    let limit = document.getElementById("limit").value
    console.log(todo)
    console.log(limit)

    // 未入力がある項目ごとにエラーメッセージを積み上げる
    let error_message = ""
    if (!todo) error_message += "予定が未入力です。<br>"
    if (!limit) error_message += "期限が未入力です。<br>"
    

    // エラーメッセージがあるかどうかでエラーの表示有無を決定
    if (error_message !== "") {
        let err = document.getElementById('error-container')
        err.innerHTML = error_message
        document.getElementById('error-container').style.display = "table"
        return
    } else {
        document.getElementById('error-container').innerHTML = ""
        document.getElementById('error-container').style.display = "none"
    }

    //main.pyにデータを渡す
    const param = new FormData()
    param.append("todo", todo)
    param.append("limit", limit)
    console.log(param)
    //console.log(param.limit)

    fetch('/register_done', {
        method: 'POST',
        body: param,
    }).then((response) => {
        console.log(response)
       
        //入力項目の初期化
        document.getElementById("schedule").reset()

        // エラーの表示領域を初期化
        document.getElementById('error-container').innerHTML = ""
        document.getElementById('error-container').style.display = "none"
        // 登録メッセージ等の表示領域を初期化
        document.getElementById('message-container').innerHTML = ""
        document.getElementById('message-container').style.display = "none"


        response.json().then((data) => {
            console.log(data) // 取得されたレスポンスデータをデバッグ表示
            
            // 正常にタスクを完了できているかを確認
            if (data.result !== "ok") {
                window.alert(data.message) // エラー表示
            } else {
                // タスクを完了できたら、チェックされた行を消す
                window.alert(data.message)
            }
        })
        
    })
})