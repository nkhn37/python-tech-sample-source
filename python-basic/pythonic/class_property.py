# ===== getter/setterではなくpropertyを使う =====
# --- 良い例 ---
class ClassGood:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value


c_good = ClassGood(1)
print(c_good.x)
c_good.x = 2
print(c_good.x)


# --- 悪い例 ---
class ClassBad:
    def __init__(self, x):
        self._x = x

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value


c_bad = ClassBad(1)
print(c_bad.get_x())
c_bad.set_x(2)
print(c_bad.get_x())
