const done_action = (ev) => {
    console.log(ev)
    elm = ev.srcElement // チェックボックスをeventから再取得

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
}



document.querySelectorAll("input[id^=fav-]").forEach((elm) => {
    elm.addEventListener('change', done_action)
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

    fetch('/add_todo', {
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


                // data を再表示
                show_data(data.data)
            }
        })
        
    })
})

document.querySelectorAll("button[id^=edit-]").forEach((elm) => {
    elm.addEventListener("click", (ev) => {
        console.log("編集ボタン押されたよ！")
        const text = prompt('予定を入力してください');
        //const e_limit = prompt('期限を入力してください');
        console.log(text)
        //console.log(e_limit)
        console.log(elm.value)

        //main.pyにデータを渡す
        const param = new FormData()
        param.append("e_id", elm.value)
        param.append("e_todo", text)
        //param.append("limit", limit)
        console.log(param)
        //console.log(param.limit)

        fetch('/edit_todo', {
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

                    console.log(data)
                    // タスクを完了できたら、チェックされた行を消す
                    window.alert(data.message)


                    // data を再表示
                    show_data(data.data)
                }
            })
            
        })

        //window.location = "http://127.0.0.1:5000/edit.html";
    })
})


// データ表示を関数化
const show_data = (data) => {
    // データを表示させる
    const tableBody = document.querySelector("#todo_table > tbody")
    tableBody.innerHTML = ""

    // レスポンスのJSONデータの件数が0だった場合
    if (data && data.length == 0) {
        let tr = document.createElement('tr')
        tr.innerHTML = "表示するデータがありません。"
        tableBody.appendChild(tr)
        return
    }

    data.forEach(elm => {
        /* 
        <tr id="todo_row_id-{{item[0]}}">
            <th>{{item[0]}}</th>
            <th>{{item[1]}}</th>
            <th>{{item[2]}}</th>
            <th>{{item[3]}}</th>
            <th>{{item[4]}}</th>
            <th><input type="checkbox" id="fav-{{item[0]}}" name="fav-{{item[0]}}" value="{{item[0]}}"></th>
        </tr>
        */

        let tr = document.createElement('tr')
        tr.id = `todo_row_id-${elm[0]}`
        tr.className="todo_row_id"
        // id
        // let td = document.createElement('td')
        // td.textContent = elm[0]
        // tr.appendChild(td)
        // tr.id="yotei"
        // task_name

        td = document.createElement('td')
        td.textContent = elm[1]
        td.id="yotei"
        tr.appendChild(td)

        td = document.createElement('td')

        let btn = document.createElement('button')
        btn.innerHTML="編集"
        btn.type="button"

        btn.id = `edit-${elm[0]}`
        btn.name=`edit-${elm[0]}`
        btn.value=`${elm[0]}`
        td.appendChild(btn)

        tr.appendChild(td)
        
        td = document.createElement('td')
        const img = document.createElement('img')
        img.src='static/img/other/limit.svg'
        img.width=25
        img.height=25
        td.appendChild(img)
        tr.appendChild(td)

        td = document.createElement('td')
        td.textContent = elm[2]
        td.id="kigen"
        tr.appendChild(td)
        td = document.createElement('td')
        td.textContent = elm[3]
        td.id="kanryou"
        tr.appendChild(td)
        td = document.createElement('td')
        //td.textContent = elm[4]
        //tr.appendChild(td)

        // <th><input type="checkbox" id="fav-{{item[0]}}" name="fav-{{item[0]}}" value="{{item[0]}}"></th>
        td = document.createElement('td')
        let cb = document.createElement('input')
        cb.setAttribute('type','checkbox')
        cb.setAttribute('id', `fav-${elm[0]}`)
        cb.setAttribute('name',`fav-${elm[0]}`)
        cb.setAttribute('value',`${elm[0]}`)
        // チェックがされた時の処理を追加
        cb.addEventListener('change', done_action)

        td.appendChild(cb)
        tr.appendChild(td)

        // 1行分をtableタグ内のtbodyへ追加する
        tableBody.appendChild(tr)
    })
    
}
