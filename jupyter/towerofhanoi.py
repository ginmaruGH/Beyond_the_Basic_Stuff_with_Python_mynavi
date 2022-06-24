"""ハノイの塔, by Al Sweigart al@inventwithpython.com
積み上げ型パズルゲーム"""

import copy
import sys

# 円盤数を増やすと難易度アップ
TOTAL_DISKS = 5

# 最初はすべての円盤がAの塔にある
# リストをスタックとして利用
# リストの最後尾をスタックの一番上として扱う
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    """ハノイの塔のゲームを1回実行する"""
    print(
        """ハノイの塔, by Al Sweigart al@inventwithpython.com
        円盤を1枚ずつ別の塔に移動させる。
        大きな円盤を小さな円盤の上に載せることはできない。
        詳細は、https://ja.wikipedia.org/wiki/ハノイの塔"""
    )
    """
    towersは、キー"A", "B", "C"と塔を表す円盤のリストからなる辞書型データ。
    リストには、円盤のサイズを表す整数値が含まれる。
    円盤が5枚の場合、
    リスト[5, 4, 3, 2, 1]は、完成した塔を表す。
    空のリスト[]は、円盤のない塔を表す。
    リスト[1, 3]は、大きい円盤が小さい円盤の上に乗っていることになり無効である。
    リスト[3, 1]は、小さい円盤が大きい円盤の上に乗せられているので有効である。
    """
    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}

    while True:  # 1回のループで1ターン
        # 塔と円盤を表示する
        displayTowers(towers)

        # プレイヤーに入力を求める
        fromTower, toTower = getPlayerMove(towers)

        # 円盤をfromTowerからtoTowerに移動する
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # ゲームをクリアできているかをチェックする
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            displayTowers(towers)  # 最後の状態を出力
            print("クリアしました！おめでとうございます！")
            sys.exit()


def getPlayerMove(towers):
    """
    プレイヤーに入力を求める
    (fromTower: 移動元の塔, toTower: 移動先の塔)
    の形で返す
    """
    while True:  # プレイヤーから有効な入力があるまで入力を促す
        print(
            'どの塔からどの塔に動かすかを文字で入力してください。\n終了する場合は、"QUIT"と入力してください。'
        )
        print("（例：AからBに移動する場合は、\"AB\"と入力）")
        print()
        response = input("> ").upper().strip()

        if response == "QUIT":
            print("お疲れさまでした！")
            sys.exit()

        # 入力が有効な文字かどうかを確認する
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("AB, AC, BA, BC, CA, CB のいずれかを入力してください。")
            continue  # 再度入力を促す

        # わかりやすい変数名にする
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            # 移動元の塔に円盤が1つもない場合はダメ
            print("その塔には円盤がありません。")
            continue  # 再度入力を促す
        elif len(towers[toTower]) == 0:
            # 移動先の塔が空ならどんな円盤でもOK
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print("小さい円盤の上に大きい円盤を置くことはできません。")
            continue  # 再度入力を促す
        else:
            # 有効な入力なので、選ばれた塔のセットを返す
            return fromTower, toTower


def displayTowers(towers):
    """塔と円盤を出力する"""

    # 塔を3つ出力する
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                displayDisk(0)  # ポールだけを出力
            else:
                displayDisk(tower[level])  # 円盤を出力
        print()

    # 塔のラベルA、B、Cを表示する
    emptySpace = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(emptySpace))


def displayDisk(width):
    """
    大きさがwidthの円盤を出力する。
    widthが0の場合は円盤なし。
    """
    emptySpace = " " * (TOTAL_DISKS - width)

    if width == 0:
        # 円盤がないポール部分の出力
        print(f"{emptySpace}||{emptySpace}", end="")
    else:
        # 円盤の出力
        disk = "@" * width
        numLabel = str(width).rjust(2, "_")
        print(f"{emptySpace}{disk}{numLabel}{disk}{emptySpace}", end="")


# プログラムを実行するとゲームがスタートする（インポートされた場合を除く）
if __name__ == "__main__":
    main()
