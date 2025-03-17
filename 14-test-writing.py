# テストのためのモジュールをインポート
import unittest

# 文字列が渡された場合は、エラーを起こす
# それ以外の場合は、掛け算を行う
def multiply(a, b):
    # 数値のみを受け付ける
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise ValueError("引数には数値を指定してください")
    return a * b

# テストを書く
class 