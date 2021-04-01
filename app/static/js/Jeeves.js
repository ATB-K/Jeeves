window.onload = function() {
    // コントロール部のマージン変更
    m_top = document.getElementById("site-header").clientHeight;
    document.getElementById("main_space").style.paddingTop = (m_top + 30 +"px");
}

function formatDate (date, format) {
    format = format.replace(/yyyy/g, date.getFullYear());
    format = format.replace(/MM/g, ('0' + (date.getMonth() + 1)).slice(-2));
    format = format.replace(/dd/g, ('0' + date.getDate()).slice(-2));
    format = format.replace(/HH/g, ('0' + date.getHours()).slice(-2));
    format = format.replace(/mm/g, ('0' + date.getMinutes()).slice(-2));
    format = format.replace(/ss/g, ('0' + date.getSeconds()).slice(-2));
    format = format.replace(/SSS/g, ('00' + date.getMilliseconds()).slice(-3));
    return format;
}

function getAnotherSiteView(name) {
    param = "SITE=" + name;
    return getView(param);
}

function getAnotherDateView(date) {
    param = "DATE=" + date;
    return getView(param);
}

function getView(param) {
    xhr = new XMLHttpRequest();
    xhr.open('POST', location.href, true);
    xhr.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    xhr.send(param);

    // 応答データ処理
    xhr.onreadystatechange = function() {
        if(xhr.readyState === 4 && xhr.status === 200) {
            // 取得htmlを反映
            document.getElementById('main_space').innerHTML = xhr.responseText;
        }

        // 画面描画後にTOPへスクロール
        setTimeout("goTop()", 150);
    }
}

// 先頭へ戻る
function goTop() {
    document.body.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    })
}