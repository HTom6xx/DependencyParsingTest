
import spacy

class DependencyProcess:
    def __init__(self):
        self.nlp = spacy.load('ja_ginza')

    def __call__(self, text:str):
        """文字列に対し係り受け解析を実行
        Args:
            text (str): _description_

        Returns:
            list: 下記dictの配列{
                'ind': トークンのインデックス, 
                'word': トークン,
                'parent_ind': 親トークンのインデックス}
        """
        response = []
        result = self.nlp(text)
        for sent in result.sents:
            for token in sent:
                response.append({
                    'ind': f'{token.i}',
                    'word': token.orth_,
                    'parent_ind': f'{token.head.i}'
                })
        return response