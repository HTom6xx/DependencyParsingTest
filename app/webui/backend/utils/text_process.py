import re

def cleaning_text(text:str) -> str:
    """_summary_ 文字列から余計な文字を除外する。

    Args:
        text (str): 入力文字列

    Returns:
        str: 整形された文字列
    """
    # null文字の除外
    text = text.replace('\0', '')
    
    # 空白の除外
    for empty in ['\t', '　', ' ']:
        text = text.replace(empty, '')
    
    # 記号の除外
    # 参考:https://qiita.com/ganyariya/items/42fc0ed3dcebecb6b117, 2025-01-12確認.
    code_regex = re.compile(
        '["#$%&\'\\\\()*+,-./:;<=>@[\\]^_`{|}~「」※〔〕“”〈〉『』【】＆＊・（）＄＃＠｀＋￥％＼／［…］●]')
    text = code_regex.sub('', text.rstrip())

    return text


def text2lines(text:str) -> list:
    """_summary_ 文字列を改行ごとに区切る。

    Args:
        text (str): 入力文字列
        
    Returns:
        list: 改行を区切り文字としたリスト
    """
    text = text.replace('\r\n', '\n')

    result = text.split('\n')
    result = list(filter(lambda x: len(x)>0, result))

    return result