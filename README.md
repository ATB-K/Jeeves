# <img src="https://raw.githubusercontent.com/ATB-K/Jeeves/master/app/static/images/Jeeves.ico" width="30"> Jeeves

## 説明 (Description)
<img src="https://raw.githubusercontent.com/ATB-K/Jeeves/doc/image/Jeeves.gif">

登録したRSSから記事を収集してJeevesのニュースサイト上で一覧表示する。<br>
RSSにアイキャッチ画像がない場合は記事内から取得する。<br>
機械学習による記事の評価→タグ判定機能付き。

## 使い方 (Usage)

<img src="https://raw.githubusercontent.com/ATB-K/Jeeves/doc/image/cmd.png">

Jeeves.pyに渡す引数で機能が切り替わる。<br>
DBなどの接続情報は instance\config 内のファイルに書いてください。

1. runserver

    Jeevesのサーバを起動する。

2. runbatch

    Jeevesで表示する記事をRSSから回収する。

3. learning

    学習用CSVから学習モデルを作成する。

4. show

    Jeevesに関する設定値の一覧を表示する。

5. init

    Jeevesが利用するテーブルの自動生成を行う。

## 依存関係 (Requirement)

- requirements.txt に記載済み

## インストール方法 (Install)

- Python
- Binary

## Author

[ATB](https://github.com/ATB-K)
