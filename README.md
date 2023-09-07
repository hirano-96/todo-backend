# todo-backend

Flask による TODO アプリケーションの バックエンド

# 環境構築

## バックエンド

### 参考

https://msiz07-flask-docs-ja.readthedocs.io/ja/latest/installation.html#install-flask

1. Flask をインストールしたいディレクトリまで移動し、仮想環境作成

   ```sh
   $ python3 -m venv venv(任意の仮想環境名)
   ```

2. 作成した仮想環境を有効化する

   ```sh
   $ . venv(作成した仮想環境名)/bin/activate
   ```

3. Flask をインストールする
   ```sh
   $ pip install Flask
   ```

## DB

つぎのミドルウェアを docker-compose を利用して起動できます。

- MySQL 8.0

  ```sh
  $ docker-compose up -d
  ```
