### 概要
- GiNZAを利用した日本語係り受け解析テストアプリ
- 解析結果はpyvisでHTMLドキュメントとして可視化

### 前提条件
- Windows 11 Proマシン上で実行
- インターネットに接続
- Webブラウザが使用可能
    - Google Chrome
    - Microsoft Edge
- ```docker compose```コマンドが使用可能

### 使用方法
1. アプリを起動
    1. 下記のいずれかを実行
        - コマンド実行
            ```bash
            docker compose -f docker/docker-compose.yml up
            ```
        - バッチファイルを実行
            ```
            execute.bat
            ```

1. Webブラウザでアクセス
    - [```http://localhost:8080/```](http://localhost:8080/)

1. ```元文章：```の欄に日本語の文章を入力
1. ```実行```ボタンを押すと係り受け解析が実行される。
    - 解析結果はプロジェクトフォルダ直下の```data/cache/*.html```に保存される。
    - しばらくするとページ下部にダウンロードリンクが追加される。

### アプリ構成
下記Dockerのサービスから構成される。
1. ### webui_service
    - FastAPIによるWebアプリ
    - APIドキュメントは(```http://localhost:8080/docs```)を確認
    - フロントエンド
        - 言語: HTML, JavaScript
        - CSSフレームワーク: BootStrap 5.3.0
    - バックエンド
        - 言語: Python 3.9.21
        - 可視化ツール: pyvis 0.3.2
        - コンテナ間通信: gRPC 1.69.0
    - クライアントとしてginza_serviceとgRPC通信
    - その他ライブラリは```docker/webui/```を参照
1. ### ginza_service
    - GiNZAで係り受け分析を実行
    - サービス
        - 言語: Python 3.9.21
        - コンテナ間通信: gRPC 1.69.0
    - サーバーとしてwebui_serviceとgRPC通信
    - その他ライブラリは```docker/GiNZA/```を参照