# linebot
予定を入力することで対話型で時刻などを入力していきリマインダとして機能してくれるものです。
ex)
　　　　　　　　予約（自分）
   （bot）いつにしますか\n
　　　　　　　　明日（自分）

   （bot）何時にしますか\n
   
　　　　　　　　12:00（自分）

   （bot）何の予定がありますか？
　　　　　　　　サッカー（自分）
    
   （bot）明日の12:00にサッカーで予約しました。
   
   次の日の12:00（herokuサーバーの調子でずれがある）に  サッカーの時間ですとBotがlineをしてくれるという機能。
  
  Webフレームワーク：Flask
  データベース:postgresql
  
  一時的にExcelファイルをつかってlineから入力された情報を得る。

友達登録時：
データベースにlineの個人idを登録するために自動的に自分のlineに登録者通知が来るためその時は手動で登録をしなければならない（完全に個人用目的で開発をした。）→make_new.py

lineと対話するコード→main.py
入力情報をexcelファイルにバッファリングするがidでファイルを作成しているため今回は原本.xlsxだけリポジトリに入れてある。
予定時刻に通知するコード→db.py

herokuスケジューラーを用いて10分に一回db.pyを実行することで通知させているため、10分単位のレスポンスになる。

機能
確認　と入力すると今まで登録したリマインド情報が一覧で見ることができる。
削除　と入力すると個別にidが指定されていてその番号を押すことでリマインド情報を削除することができる。
ヘルプ　使い方の表示

不正な入力は三回で最初から入力させる

クラスを使ったプログラムに変更を検討中
