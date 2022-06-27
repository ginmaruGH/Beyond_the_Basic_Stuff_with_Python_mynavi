class WixCoin:
    def __init__(self, galleons, sickles, knuts):
        """galleons, sickles, knutsをセットしてWixCoinオブジェクトを作る。"""

        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
        # 注意：__init__()メソッドは値を返さない

    def value(self):
        """このWizCoinオブジェクトに含まれる全コインの価値（単位はknuts）"""

        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        """コインの重さをグラムの単位で返す"""

        return (self.galleons * 31.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
