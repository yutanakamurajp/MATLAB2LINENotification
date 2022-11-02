# MATLAB2LINENotification
MATLABからLINE通知を送る機能を実装した関数
具体的な説明は Qiita記事に記載しています。

## 使い方

0. （UNIX系の場合）requestsパッケージのインストール
requestsパッケージを使用するため，pip等を用いてインストールしておいてください。
`requirements.txt` ファイルを入れていますので，

```
$ pip install -r requirements.txt
```
で大丈夫です。

1. [LINE notify](https://notify-bot.line.me/ja/)からアクセストークンを発行

具体的な発行方法は[こちら](https://firestorage.jp/business/line-notify/)等に記載していますので，そちらを参照してください。
アクセスコード（例：dBHta…）を取得します。
取得したアクセスコードをテキストファイル`Key.txt`に保存します。

2. 文字列を作成し，関数に引数として指定します。

```MATLAB
LINENotification("送りたい文章")
```

## 補足等

`try ~ catch` を使用すると，計算エラーが出た場合にエラー文を送信させることもできます。

```MATLAB
try
    % メインプログラム

    LINENotification("計算終了")    
catch ME
    % エラー処理

    LINENotification(string(ME.massage))
end

```