[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# きれいなPythonプログラミング

クリーンなコードを書くための最適な方法

[出版サイト](https://book.mynavi.jp/ec/products/detail/id=127578)

[サポートサイト](https://book.mynavi.jp/supportsite/detail/9784839977405.html)

[原著サイト](https://nostarch.com/beyond-basic-stuff-python)

[原著サポートサイト](https://inventwithpython.com/beyond/)

---

## PART 01 基本準備から始めよう

- Ch.01 エラーの取り扱いと質問の仕方
  - 1.1 エラーメッセージの読み方
  - 1.2 リンターでエラー予防
  - 1.3 プログラミングの質問方法
  - 1.4 具体的な質問例
  - 1.5 まとめ
- Ch.02 環境設定とコマンドライン
  - 2.1 ファイルシステム
  - 2.2 プログラムとプロセス
  - 2.3 コマンドライン
  - 2.4 環境変数とPATH
  - 2.5 コマンドラインを使わずにPython プログラムを実行する
  - 2.6 まとめ

## PART 02 Python に適した開発方法・ツール・テクニック

- Ch.03 Black を使ってコードフォーマットを整える
  - 3.1 こんなコードは嫌われる
  - 3.2 スタイルガイドとPEP 8
  - 3.3 スペース（空白文字）の使い方
  - 3.4 空行の挿入
  - 3.5 妥協しないコードフォーマットツール：Black
  - 3.6 まとめ
- Ch.04 わかりやすいネーミング
  - 4.1 ケーススタイル
  - 4.2 PEP 8の命名規則
  - 4.3 適度な名前の長さ
  - 4.4 検索しやすい名前
  - 4.5 ジョーク、ダジャレ、文化的な言及を避ける
  - 4.6 ビルトイン（組み込み）の名前を上書きしない
  - 4.7 最悪な変数名
  - 4.8 まとめ
- Ch.05 怪しいコード臭
  - 5.1 重複したコード
  - 5.2 マジックナンバー
  - 5.3 コメントアウトされたコードとデッドコード
  - 5.4 プリントデバッグ
  - 5.5 数字付きの変数名
  - 5.6 関数やモジュールにすべきクラス
  - 5.7 内包表記の中に内包表記がある
  - 5.8 空の例外ブロックと不十分なエラーメッセージ
  - 5.9 コード臭の迷信
  - 5.10 まとめ
- Ch.06 パイソニックなコードを書こう
  - 6.1 Python の禅
  - 6.2 インデント愛を伝えたい
  - 6.3 誤用の多い構文
  - 6.4 文字列のフォーマット
  - 6.5 リストのコピー
  - 6.6 パイソニックな辞書の使い方
  - 6.7 条件式：Python の「醜い」三項演算子
  - 6.8 変数の扱い
  - 6.9 まとめ
- Ch.07プログラミングの専門用語
  - 7.1 定義
  - 7.2 混同されやすい用語
  - 7.3 まとめ
  - 7.4 参考資料
- Ch.08 Python のよくある落とし穴
  - 8.1 ループ時にリストの追加・削除をしない
  - 8.2 copy.copy() やcopy.deepcopy() を使わずに可変型の値をコピーしない
  - 8.3 デフォルト引数に可変値を使用しない
  - 8.4 文字列連結で文字列を作らない
  - 8.5 sort() にアルファベット順のソートを期待してはいけない
  - 8.6 浮動小数点数が厳密であるとは限らない
  - 8.7 != 演算子を連鎖させない
  - 8.8 単要素のタプルではコンマを忘れずに
  - 8.9 まとめ
- Ch.09 Python の要注意コード
  - 9.1 256は256だけれども257は257ではない理由
  - 9.2 文字列のインターニング
  - 9.3 なんちゃってインクリメント・デクリメント演算子
  - 9.4 組み込み関数all()
  - 9.5 ブール値は整数値
  - 9.6 複数種類の演算子の連結
  - 9.7 空も飛べちゃうPython!?
  - 9.8 まとめ
- Ch.10 よい関数の書き方
  - 10.1 関数名
  - 10.2 関数サイズのトレードオフ
  - 10.3 関数のパラメーターと引数
  - 10.4 関数型プログラミング
  - 10.5 戻り値は常に同じデータ型であること
  - 10.6 例外を発生させる？それともエラーコードを返す？
  - 10.7 まとめ
- Ch.11 コメント、docstring、型ヒント
  - 11.1 コメント
  - 11.2 docstring
  - 11.3 型ヒント
  - 11.4 まとめ
- Ch.12 Git でプロジェクト管理
  - 12.1 Git のコミットとリポジトリー
  - 12.2 cookiecutter を使って新しいPython プロジェクトを作成する
  - 12.3 Git のインストール
  - 12.4 Git を使う手順
  - 12.5 コンピューター上にGit リポジトリーを作成する
  - 12.6 コミットログの表示
  - 12.7 古い変更点の復元
  - 12.8 GitHub とgit push コマンド
  - 12.9 まとめ
- Ch.13 パフォーマンスの測定とオーダー記法
  - 13.1 timeit モジュール
  - 13.2 cProfile プロファイラー
  - 13.3 オーダー記法について
  - 13.4 オーダー記法で表す計算量
  - 13.5 コードの計算量を決定する
  - 13.6 まとめ
- Ch.14 プロジェクトの実践
  - 14.1 ハノイの塔
  - 14.2 四目並べ
  - 14.3 まとめ

## PART 03 ブジェクト指向のPython

- Ch.15 オブジェクト指向プログラミングとクラス
  - 15.1 事例から学ぶ：書式への入力
  - 15.2 クラスからオブジェクトを作成する
  - 15.3 シンプルなクラスWizCoin の作成
  - 15.4 type() 関数と__qualname__ 属性
  - 15.5 非オブジェクト指向とオブジェクト指向：三目並べの例
  - 15.6 実社会でのクラス設計は難しい
  - 15.7 まとめ
- Ch.16 オブジェクト指向プログラミングと継承
  - 16.1 継承の仕組み
  - 16.2 isinstance() 関数とissubclass() 関数
  - 16.3 クラスメソッド
  - 16.4 クラス属性
  - 16.5 静的メソッド
  - 16.6 クラスメソッド・クラス属性・静的メソッドを使うタイミング
  - 16.7 オブジェクト指向の用語集
  - 16.8 継承を使わない場合
  - 16.9 多重継承
  - 16.10 メソッド解決順序
  - 16.11 まとめ
- Ch.17 パイソニックなオブジェクト指向：プロパティとダンダーメソッド
  - 17.1 プロパティ
  - 17.2 ダンダーメソッド
  - 17.3 まとめ

---

[Pythonハッカーガイドブック](https://book.mynavi.jp/ec/products/detail/id=115482)
