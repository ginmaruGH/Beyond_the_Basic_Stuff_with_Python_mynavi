"""
四目並べ, by Al Sweigart al@inventwithpython.com
コネクトフォーに似た、タイルが4つ奈良病に落とすゲーム。
"""

import sys

# 盤面表示に使う定数
EMPTY_SPACE = "."  # 数えやすいようにスペースはピリオドで表す
PLAYER_X = "X"
PLAYER_O = "O"

# 注意：BOARD_WIDTHを変更したときは、
# BOARD_TEMPLATEとCOLUMN_LABELSも変更する
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# 盤面表示のテンプレート文字列
BOARD_TEMPLATE = """
     1234567
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+"""

def main():
    """四目並べのゲームを1回実行する"""

    print(
        """四目並べ, by Al Sweigart al@inventwithpython.com
        2人のプレイヤーが交互に、タイルを7つの列のいずれかに落として、
        水平、垂直、斜めに4枚揃えたほうが勝ち。"""
    )

    # ゲームの初期化
    gameBoard = getNewBoard()
    playerTurn = PLAYER_X

    # プレイヤーのターンを開始する
    while True:
        # 盤面を表示し、入力を受け付ける
        displayBoard(gameBoard)
        playerMove = getPlayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        # 勝ちか引き分けかをチェックする
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)  # 最終的な盤面を表示
            print("Player {} の勝ち！".format(playerTurn))
            sys.exit()
        elif isFull(gameBoard):
            displayBoard(gameBoard)  # 最終的な盤面を表示
            print("引き分け！ ")
            sys.exit()

        # プレイヤー交代
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X

def getNewBoard():
    """四目並べの盤面を表す辞書を返す。

    キーは、（列のインデックス、行のインデックス）のような2つの整数のタプルで、
    値は、"X", "O", "."のいずれかになる。（ピリオドは空白を表す）"""

    board = {}

    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            board[(columnIndex, rowIndex)] = EMPTY_SPACE
    return board

def displayBoard(board):
    """盤面とタイルを出力する。"""

    # 盤面テンプレートのformat()にわたすデータのリストを用意する。
    # リストに格納するデータは、左から右へ、上から下へ向かう順番で、
    # 盤面上のタイルと空白部分の情報になっている。
    tileChars = []
    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            tileChars.append(board[(columnIndex, rowIndex)])

    # 盤面を表示
    print(BOARD_TEMPLATE.format(*tileChars))

def getPlayerMove(playerTile, board):
    """プレイヤーに、どの列にタイルを落とすかを決めてもらう。

    タイルの落ちる場所（列、行）のタプルで返す。"""

    # プレイヤーから有効な入力があるまで入力を促す
    while True:
        print(
            f"player{playerTile}, 1から{BOARD_WIDTH}または、QUITと入力してください。："
        )
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("お疲れさまでした！")
            sys.exit()

        if response not in COLUMN_LABELS:
            print(f"1から{BOARD_WIDTH}までの数字を入力してください。：")
            continue  # 再度入力を促す

        # 0ベースのインデックスにするため-1しておく
        columnIndex = int(response) - 1

        # 列が一杯の場合は、再度入力を促す
        if board[(columnIndex, 0)] != EMPTY_SPACE:
            print("その列は一杯です。ほかの列を選んでください。")
            continue  # 再度入力を促す

        # 一番下から空白部分を探す
        for rowIndex in range(BOARD_HEIGHT - 1, -1, -1):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return (columnIndex, rowIndex)

def isFull(board):
    """盤面に空白部分がない場合はTrueを返す。空白部分がある場合はFalseを返す。"""

    for rowIndex in range(BOARD_HEIGHT):
        for columnIndex in range(BOARD_WIDTH):
            if board[(columnIndex, rowIndex)] == EMPTY_SPACE:
                return False  # 空白が見つかったのでFalse返す
    return True  # 空白部分なし

def isWinner(playerTile, board):
    """playerTileが1列に4枚揃っていたらTrue、揃っていなければFalseを返す。"""

    # 盤面全体を調べて1列に4枚揃っているかを確認する
    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT):
            # 右方向へ4枚分調べる
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex)]
            tile3 = board[(columnIndex + 2, rowIndex)]
            tile4 = board[(columnIndex + 3, rowIndex)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # 下方向へ4枚調べる
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex, rowIndex + 1)]
            tile3 = board[(columnIndex, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    for columnIndex in range(BOARD_WIDTH - 3):
        for rowIndex in range(BOARD_HEIGHT - 3):
            # 右下方向へ4枚調べる
            tile1 = board[(columnIndex, rowIndex)]
            tile2 = board[(columnIndex + 1, rowIndex + 1)]
            tile3 = board[(columnIndex + 2, rowIndex + 2)]
            tile4 = board[(columnIndex + 3, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

            # 左下方向へ4枚調べる
            tile1 = board[(columnIndex + 3, rowIndex)]
            tile2 = board[(columnIndex + 2, rowIndex + 1)]
            tile3 = board[(columnIndex + 1, rowIndex + 2)]
            tile4 = board[(columnIndex, rowIndex + 3)]
            if tile1 == tile2 == tile3 == tile4 == playerTile:
                return True

    return False

# プログラムを実行するとゲームがスタートする（インポートされた場合除く）
if __name__ == "__main__":
    main()
