# linebot
予定を入力することで対話型で時刻などを入力していきリマインダとして機能してくれるものです。
ex)
　　　　　　　　予約（自分）\n
   （bot）いつにしますか\n
　　　　　　　　明日（自分）\n

   （bot）何時にしますか\n
   
　　　　　　　　12:00（自分）\n

   （bot）何の予定がありますか？\n
　　　　　　　　サッカー（自分）\n
    
   （bot）明日の12:00にサッカーで予約しました。\n
   
   次の日の12:00（herokuサーバーの調子でずれがある）に  サッカーの時間ですとBotがlineをしてくれるという機能。
  
  Webフレームワーク：Flask
  データベース:postgresql
  
  一時的にExcelファイルをつかってlineから入力された情報を得る。

友達登録時：
データベースにlineの個人idを登録するために自動的に自分のlineに登録者通知が来るためその時は手動で登録をしなければならない（完全に個人用目的で開発をした。）→make_new.py

lineと対話するコード→main.py

予定時刻に通知するコード→db.py

