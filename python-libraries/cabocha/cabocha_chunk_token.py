"""CaboChaによる構文解析の基本的な使い方
CaboCha解析結果の各要素を扱う

[説明ページ]
https://tech.nkhn37.net/python-cabocha-syntactic-analysis/#CaboCha-5

[環境構築方法]
同フォルダのREADME.mdを参照
"""
import CaboCha

# CaboChaの構文解析器を生成する
cabocha = CaboCha.Parser()

# 解析対象の文字列を用意する
sample_text = '私はCaboChaを使ってPythonで構文解析を実装した。'

# 構文解析を実行する
result_tree = cabocha.parse(sample_text)

# 個別の要素を扱う
chunk_id = 0
for i in range(result_tree.size()):
    token = result_tree.token(i)

    # 文節の先頭の場合はchunkがNoneではない
    if token.chunk is not None:
        print('===== Chunk')
        print(f'文節番号:{chunk_id}')
        print(f'係り先:{token.chunk.link}')
        print(f'主辞:{token.chunk.head_pos}')
        print(f'機能辞:{token.chunk.func_pos}')
        print(f'係り関係のスコア:{token.chunk.score}')
        chunk_id += 1

    print('----- Token')
    print(f'表層形:{token.surface}')
    print(f'形態素情報:{token.feature}')
