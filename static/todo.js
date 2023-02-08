window.addEventListener("load", function () {
  //document.getElementByIdで指定したidのhtml要素を取得する
  let todo_table = document.getElementById("todo_table");
  for (let i = 0; i < todo_table.rows.length; i++) {
    //i行目の4列目にクリックイベントを付与
    todo_table.rows[i].cells[3].onclick = delete_todo;
    //i行目の０列目にクリックイベントを付与
    todo_table.rows[i].cells[0].onclick = check_todo;
  }

  let todo_check_table = document.getElementById("todo_check_table");
  for (let i = 0; i < todo_check_table.rows.length; i++) {
    todo_check_table.rows[i].cells[3].onclick = delete_todo;
    todo_check_table.rows[i].cells[0].onclick = uncheck_todo;
  }

  let todo_area = document.getElementById("todo");
  //todo_area.addEventListener('change',check_todo_area)
  todo_area.addEventListener("keyup", check_todo_area);

  //完了していない予定での処理
  let incomp_schedule = document.getElementById("incomp_img");
  incomp_schedule.addEventListener("click", () => {
    let no_check = document.getElementById("no_check");
    no_check.classList.toggle("toggle");
    let incomp_img = this.document.getElementById("incomp_img");
    incomp_img.classList.toggle("degree_90");
  });
  //完了した予定での処理
  let comp_schedule = document.getElementById("comp_img");
  comp_schedule.addEventListener("click", () => {
    let checked = document.getElementById("checked");
    checked.classList.toggle("toggle");
    let comp_img = this.document.getElementById("comp_img");
    comp_img.classList.toggle("degree_90");
  });
});

async function check_todo(e) {
  console.log(e.target.id);
  const postdata = new FormData();
  postdata.append("check_id", e.target.id);
  //pythonの処理が全て完了してから window.location.reload()
  //が行われるようにした
  await fetch("/check", {
    method: "POST",
    body: postdata, // IDデータが入ったFormDataを送信
  });

  window.location.reload();
}

async function uncheck_todo(e) {
  console.log(e.target.id);
  const postdata = new FormData();
  postdata.append("check_id", e.target.id);
  //pythonの処理が全て完了してから window.location.reload()
  //が行われるようにした
  await fetch("/uncheck", {
    method: "POST",
    body: postdata, // IDデータが入ったFormDataを送信
  });

  window.location.reload();
}

async function delete_todo(e) {
  let res = confirm("本当に削除しますか？");
  if (res == false) return;
  const postdata = new FormData();
  postdata.append("delete_id", e.target.id);
  //pythonの処理が全て完了してから window.location.reload()
  //が行われるようにした
  await fetch("/delete", {
    method: "POST",
    body: postdata, // IDデータが入ったFormDataを送信
  });

  window.location.reload();
}

/**function check_todo_area() {
  console.log(document.getElementById("todo").value.length);
  //半角だと30文字文字より多く文字を入力する事はできないが全角だと30文字を超えるが、enter押下時30文字に表示される
  if (document.getElementById("todo").value.length >= 30) {
    document.getElementById("alert_area").style.display = "block";
  } else {
    document.getElementById("alert_area").style.display = "none";
  }
}**/

const done_action = (ev) => {
  console.log(ev);
  elm = ev.srcElement; // チェックボックスをeventから再取得

  // チェックボックスの値が変更されたときに実行される

  console.log(elm);
  console.log(elm.checked);
  console.log(elm.value);
  if (elm.checked) {
    // flaskへ送信するデータを用意する
    const postdata = new FormData();
    postdata.append("checked_id", elm.value); // チェックした行のIDを設定

    // fetch
    // "/register_done" としてタスクをこなしたことを登録する。
    // この変更は、flask側(app.py)の処理も変更しています。
    fetch("/register_done", {
      method: "POST",
      body: postdata, // IDデータが入ったFormDataを送信
    }).then((response) => {
      // 正常にHTTPリクエストが通った
      console.log(response);

      // レスポンスデータからJSONを取り出し
      response.json().then((data) => {
        console.log(data); // 取得されたレスポンスデータをデバッグ表示

        // 正常にタスクを完了できているかを確認
        if (data.result !== "ok") {
          window.alert(data.message); // エラー表示
        } else {
          // タスクを完了できたら、チェックされた行を消す
          document.querySelector(`#todo_row_id-${elm.value}`).remove();
        }
      });
    });
  }
};

document.querySelectorAll("input[id^=fav-]").forEach((elm) => {
  elm.addEventListener("change", done_action);
});

document.getElementById("add-submit").addEventListener("click", async (ev) => {
  // ボタンイベントのキャンセル
  ev.preventDefault();

  // 入力チェック
  let todo = document.getElementById("todo").value;
  let limit = document.getElementById("limit").value;

  // 未入力がある項目ごとにエラーメッセージを積み上げる
  let error_message = "";
  if (!todo) error_message += "予定が未入力です。予定を入力してください。<br>";
  if (!limit) error_message += "期限が未入力です。期限を入力してください。<br>";

  // エラーメッセージがあるかどうかでエラーの表示有無を決定
  if (error_message !== "") {
    let err = document.getElementById("error-container");
    err.innerHTML = error_message;
    document.getElementById("error-container").style.display = "table";
    return;
  } else {
    document.getElementById("error-container").innerHTML = "";
    document.getElementById("error-container").style.display = "none";
  }

  //main.pyにデータを渡す
  const param = new FormData();
  param.append("todo", todo);
  param.append("limit", limit);
  console.log(param);
  //console.log(param.limit)

  fetch("/add_todo", {
    method: "POST",
    body: param,
  }).then((response) => {
    console.log(response);

    //入力項目の初期化
    document.getElementById("schedule").reset();

    // エラーの表示領域を初期化
    document.getElementById("error-container").innerHTML = "";
    document.getElementById("error-container").style.display = "none";
    // 登録メッセージ等の表示領域を初期化
    document.getElementById("message-container").innerHTML = "";
    document.getElementById("message-container").style.display = "none";

    response.json().then((data) => {
      console.log(data); // 取得されたレスポンスデータをデバッグ表示

      // 正常にタスクを完了できているかを確認
      if (data.result !== "ok") {
        window.alert(data.message); // エラー表示
      } else {
        // タスクを完了できたら、チェックされた行を消す
        window.alert(data.message);
        window.location.reload();
      }
    });
  });
});

document.querySelectorAll("button[id^=edit-]").forEach((elm) => {
  elm.addEventListener("click", (ev) => {
    console.log("編集ボタン押されたよ！");
    const text = prompt("予定を入力してください");
    //const e_limit = prompt('期限を入力してください');
    console.log(text);
    console.log(typeof text);
    //console.log(e_limit)
    console.log(elm.value);

    //main.pyにデータを渡す
    const param = new FormData();
    param.append("e_id", elm.value);
    param.append("e_todo", text);
    //param.append("limit", limit)
    console.log(param);
    //console.log(param.limit)

    fetch("/edit_todo", {
      method: "POST",
      body: param,
    }).then((response) => {
      console.log(response);

      //入力項目の初期化
      //document.getElementById("schedule").reset()

      response.json().then((data) => {
        console.log(data); // 取得されたレスポンスデータをデバッグ表示

        // 正常にタスクを完了できているかを確認
        if (data.result !== "ok") {
          window.alert(data.message); // エラー表示
        } else {
          console.log(data);
          // タスクを完了できたら、チェックされた行を消す
          window.alert(data.message);
        }
      });
    });

    window.location.reload();
  });
});
