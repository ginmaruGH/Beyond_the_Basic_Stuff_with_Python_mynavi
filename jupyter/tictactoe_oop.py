# tictactoe_oop.py, オブジェクト指向バーsジョンの三目並べゲーム

ALL_SPACES = list('123456789')  # 辞書型の盤面データに対するキー
X, O, BLANK = 'X', 'O', ' '    # プレイヤーや空き場所を表す文字定数

def main():
    """三目並べをはじめる。"""
    print("三目並べゲームだよ！")
    # 辞書型の盤面データを生成する
    gameBoard = TTTBoard()
    # "X"が先行、"O"が後攻
    currentPlayer, nextPlayer = X, O
    while True:
        print(gameBoard.getBoardStr())  # 盤面を画面に表示

        # プレイヤーが1~9の数値を入力するまで入力を促す
        move = None
        while not gameBoard.isValidSpace(move):
            print(f"{currentPlayer}の置き場所は？（1~9）")
            move = input()
        gameBoard.updateBoard(move, currentPlayer)  # 盤面を更新する

        # ゲーム終了の判定
        if gameBoard.isWinner(currentPlayer):  # 勝ち負けの判定
            print(gameBoard.getBoardStr())
            print(currentPlayer + "の勝ち！")
            break
        elif gameBoard.isBoardFull():  # 引き分けの判定
            print(gameBoard.getBoardStr())
            print("引き分け！")
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer  # プレイヤー交代
    print("お疲れさまでした！")

class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        """新規の盤面を作成する。"""
        self._space = {}  # 辞書型のデータとして盤面を表す
        for space in ALL_SPACES:
            self._space[space] = BLANK  # すべて空欄で初期化

    def getBoardStr(self):
        """盤面の状態を文字列として返す。"""
        return f"""
        {self._space['1']}|{self._space['2']}|{self._space['3']} 1 2 3
        -+-+-
        {self._space['4']}|{self._space['5']}|{self._space['6']} 4 5 6
        -+-+-
        {self._space['7']}|{self._space['8']}|{self._space['9']} 7 8 9"""

    def isValidSpace(self, space):
        """有効な入力」かつ「指定箇所が空欄」であれば「True」を返す。"""
        return space in ALL_SPACES and self._space[space] == BLANK

    def isWinner(self, player):
        """playerが勝者ならTrueを返す。"""
        s, p = self._space, player  # 変数名を短くする（構文糖 syntax sugar）
        # 縦3ヶ所・横3ヶ所・斜め2ヶ所にマークが揃っているかをチェックする
        return (
            (s['1'] == s['2'] == s['3'] == p) or  # 横上段
            (s['4'] == s['5'] == s['6'] == p) or  # 横中段
            (s['7'] == s['8'] == s['9'] == p) or  # 横下段
            (s['1'] == s['4'] == s['7'] == p) or  # 縦左列
            (s['2'] == s['5'] == s['8'] == p) or  # 縦中列
            (s['3'] == s['6'] == s['9'] == p) or  # 縦右列
            (s['1'] == s['5'] == s['9'] == p) or  # 斜め
            (s['3'] == s['5'] == s['7'] == p)     # 斜め
        )

    def isBoardFull(self):
        """盤面に空き場所がなくなったら「True」を返す。"""
        for space in ALL_SPACES:
            if self._space[space] == BLANK:
                return False  # 1ヶ所でも空きが見つかったらFalseを返す
        return True  # 空きが見つからなかったらTrueを返す

    def updateBoard(self, space, player):
        """盤面の指定場所をマークする。"""
        self._space[space] = player


# 実行時にmain()を呼び出す（importされた場合は実行しない）
if __name__ == '__main__':
    main()
