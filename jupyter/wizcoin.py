import collections.abc
import operator

class WizCoinException(Exception):
    """wizcoinモジュールが誤用された場合にこの例外を発生させる"""
    pass


class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        """galleons, sickles, knutsをセットしてWizCoinオブジェクトを作る。"""
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

    @property
    def galleons(self):
        """このオブジェクトのガリオン（galleon）硬貨の数を返す。"""
        return self._galleons

    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                'galleons attr must be set to an int, not a ' +
                value.__class__.__qualname__
            )
        if value < 0:
            raise WizCoinException(
                'galleons attr must be a positive int, not ' +
                value.__class__.__qualname__
            )
        self._galleons = value

    @property
    def sickles(self):
        """このオブジェクトのシックル（sickle）硬貨の数を返す。"""
        return self._sickles

    @sickles.setter
    def sickles(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                'sickles attr must be set to an int, not a ' +
                value.__class__.__qualname__
            )
        if value < 0:
            raise WizCoinException(
                'sickles attr must be a positive int, not ' +
                value.__class__.__qualname__
            )
        self._sickles = value

    @property
    def knuts(self):
        """このオブジェクトのクヌート（knut）硬貨の数を返す。"""
        return self._knuts

    @knuts.setter
    def knuts(self, value):
        if not isinstance(value, int):
            raise WizCoinException(
                'knuts attr must be set to an int, not a ' +
                value.__class__.__qualname__
            )
        if value < 0:
            raise WizCoinException(
                'knuts attr must be a positive int, not ' +
                value.__class__.__qualname__
            )
        self._knuts = value

    @property
    def total(self):
        """このWizCoinオブジェクトに含まれる全コインの価値（単位はknuts）"""
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def __repr__(self):
        """このオブジェクトを再生成する式を文字列で返す。"""
        return f"{self.__class__.__qualname__}({self.galleons}, {self.sickles}, {self.knuts})"

    def __str__(self):
        """このオブジェクトの内容を人間が読みやすい文字列として返す。"""
        return f"{self.galleons}g, {self.sickles}s, {self.knuts}k"

    def __add__(self, other):
        """2つのWizCoinオブジェクトの硬貨を合計する。"""
        if not isinstance(other, WizCoin):  # 型チェックを行う
            return NotImplemented

        return WizCoin(other.galleons + self.galleons, other.sickles + self.sickles, other.knuts + self.knuts)

    def __mul__(self, other):
        """各硬貨の数に非負整数を掛ける。"""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            # 負の整数を掛けると硬貨の数が負になってしまうので無効とする
            raise WizCoinException('負の数を掛けてはいけない。')

        return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

    def __rmul__(self, other):
        """硬貨の数に非負数を掛ける。"""
        return self.__mul__(other)

    def __iadd__(self, other):
        """Add the amounts in another WizCoin object to this object."""
        """別のWizCoinオブジェクトの金額をこのオブジェクトに加える。"""
        if not isinstance(other, WizCoin):
            return NotImplemented

        # selfオブジェクトを変更するように修正する：
        self.galleons += other.galleons
        self.sickles += other.sickles
        self.knuts += other.knuts
        return self  # 代入型ダンダーメソッドは、ほとんど場合selfを返す

    def __imul__(self, other):
        """このオブジェクトのgalleons, sickles, knutsに非負整数を掛ける。"""
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise WizCoinException("負の数を掛けてはいけない。")

        # WizCoinクラスは可変型のオブジェクトを生成する
        # したがって、以下ののように新たなオブジェクトを生成してはいけない
        # return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)

        # selfオブジェクトを変更するように修正する：
        self.galleons *= other
        self.sickles *= other
        self.knuts *= other
        return self  # 代入型ダンダーメソッドは、ほとんど場合selfを返す

    def _comparisonOperatorHelper(self, operatorFunc, other):
        """比較ダンダーメソッド用のヘルパーメソッド。"""

        if isinstance(other, WizCoin):
            return operatorFunc(self.total, other.total)
        elif isinstance(other, (int, float)):
            return operatorFunc(self.total, other)
        elif isinstance(other, collections.abc.Sequence):
            otherValue = (other[0] * 17 * 29) + (other[1] * 29) + other[2]
            return operatorFunc(self.total, otherValue)
        elif operatorFunc == operator.eq:
            return False
        elif operatorFunc == operator.ne:
            return True
        else:
            return NotImplemented

    def __eq__(self, other):  # eqは"EQual(==)"
        return self._comparisonOperatorHelper(operator.eq, other)

    def __ne__(self, other):  # neは"Not Eual(!=)"
        return self._comparisonOperatorHelper(operator.ne, other)

    def __lt__(self, other):  # ltは"Less Than(<)"
        return self._comparisonOperatorHelper(operator.lt, other)

    def __le__(self, other):  # leは"Less than or Equal(<=)"
        return self._comparisonOperatorHelper(operator.le, other)

    def __gt__(self, other):  # gtは"Greater Than(>)"
        return self._comparisonOperatorHelper(operator.gt, other)

    def __ge__(self, other):  # geは"Greater than or Equal(>=)"
        return self._comparisonOperatorHelper(operator.ge, other)
