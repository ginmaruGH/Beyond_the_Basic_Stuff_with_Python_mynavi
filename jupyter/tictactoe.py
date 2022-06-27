# tictactoe.py, オブジェクト指向でない三目並べゲーム

ALL_SPACES = list('123456789')  # 辞書型の盤面データに対するキー
X, O, BLANK = 'X', 'O', ' '    # プレイヤーや空き場所を表す文字定数

def main():
    """三目並べのゲームをはじめる。"""
    print("三目並べゲームだよ！")
    # 辞書型の盤面データを生成する
    gameBoard = getBlankBoard()
    # "X"が先行、"O"が後攻
    currentPlayer, nextPlayer = X, O

    while True:
        print(getBoardStr(gameBoard))  # 盤面を画面に表示

        # プレイヤーが1~9の数値を入力するまで入力を促す
        move = None
        while not isValidSpace(gameBoard, move):
            print(f"{currentPlayer}の置き場所は？（1~9）")
            move = input()
        updateBoard(gameBoard, move, currentPlayer)  # 盤面を更新する

        # ゲーム終了の判定
        if isWinner(gameBoard, currentPlayer):  # 勝ち負けの判定
            print(getBoardStr(gameBoard))
            print(currentPlayer + "の勝ち！")
            break
        elif isBoardFull(gameBoard):  # 引き分けの判定
            print(getBoardStr(gameBoard))
            print("引き分け！")
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer  # プレイヤー交代
    print("お疲れさまでした！")

def getBlankBoard():
    """新規の盤面を作成する。"""
    board = {}  # 辞書型のデータとして盤面を表す
    for space in ALL_SPACES:
        board[space] = BLANK  # すべて空欄で初期化
    return board

def getBoardStr(board):
    """盤面の状態を文字列として返す。"""
    return f"""
        {board['1']}|{board['2']}|{board['3']}  1 2 3
        -+-+-
        {board['4']}|{board['5']}|{board['6']}  4 5 6
        -+-+-
        {board['7']}|{board['8']}|{board['9']}  7 8 9"""

def isValidSpace(board, space):
    """「有効な入力」かつ「指定箇所が空欄」であれば「True」を返す。"""
    return space in ALL_SPACES and board[space] == BLANK

def isWinner(board, player):
    """playerが勝者ならTrueを返す。"""
    b, p = board, player  # 変数名を短くする（構文糖 syntax sugar）
    # 縦3ヶ所・横3ヶ所・斜め2ヶ所にマークが揃っているかをチェックする
    return (
        (b['1'] == b['2'] == b['3'] == p) or  # 横上段
        (b['4'] == b['5'] == b['6'] == p) or  # 横中段
        (b['7'] == b['8'] == b['9'] == p) or  # 横下段
        (b['1'] == b['4'] == b['7'] == p) or  # 縦左列
        (b['2'] == b['5'] == b['8'] == p) or  # 縦中列
        (b['3'] == b['6'] == b['9'] == p) or  # 縦右列
        (b['1'] == b['5'] == b['9'] == p) or  # 斜め
        (b['3'] == b['5'] == b['7'] == p)     # 斜め
    )

def isBoardFull(board):
    """盤面に空き場所がなくなったら「True」を返す。"""
    for space in ALL_SPACES:
        if board[space] == BLANK:
            return False  # 1ヶ所でも空きが見つかったらFalseを返す
    return True  # 空きが見つからなかったらTrueを返す

def updateBoard(board, space, mark):
    """盤面の指定場所をマークする。"""
    board[space] = mark

# 実行時にmain()を呼び出す（importされた場合は実行しない）
if __name__ == '__main__':
    main()
