import os, datetime
import networkx as nx
from pyvis.network import Network

import grpc
from proto import ginza_pb2, ginza_pb2_grpc

from .utils.text_process import cleaning_text, text2lines

GINZA_SERVICE_PORT = 8080
GRAPH_CACHE_FILEPATH = '../cache'

class DependencyParsingTask:
    def __call__(self, text:str):
        """_summary_ 係り受け解析を実行

        Args:
            text (str): 入力文字列

        Returns:
            list: 係り受け解析結果のリスト
        """
        text = cleaning_text(text)
        text_list = text2lines(text)
        result = []
        for text in text_list:
            with grpc.insecure_channel(f"ginza_service:{GINZA_SERVICE_PORT}") as channel:
                stub = ginza_pb2_grpc.GiNZAServiceServicerStub(channel)
                res = stub.DependencyParsing(
                    ginza_pb2.DependencyParsingRequest(msg=text))
            res = list(res.res)
            res = [
                {'ind': int(x.ind), 'word': x.word, 'parent_ind': int(x.parent_ind)} \
                    for x in res]
            result.append(res)
        return result


def visualize_network(dep_data_list:list):
    """_summary_ pyvisを用いて解析結果をHTMLドキュメントとして可視化

    Args:
        dep_data_list (list): 係り受け解析結果のリスト

    Returns:
        _type_: 出力されたHTMLドキュメントのパス
    """
    # グラフを作成
    net = Network(height="750px", width="100%")
    G = nx.Graph()
    nodes = []
    edges = []
    for dep_data in dep_data_list:
        words = [x['word'] for x in dep_data]
        word_node_list = [(x['word'], words[x['parent_ind']]) for x in dep_data]

        for word_node in word_node_list:
            if word_node[0] != word_node[1]:
                edges.append(word_node)
            if not word_node[0] in nodes:
                nodes.append(word_node[0])

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    nx.draw(G, with_labels=True)
    net.from_nx(G)

    # 出力先フォルダが無ければ作成
    if not os.path.exists(GRAPH_CACHE_FILEPATH):
        os.makedirs(GRAPH_CACHE_FILEPATH)
        
    # 出力ファイル名を日時から決定
    file_name = f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.html'
    file_path = os.path.join(GRAPH_CACHE_FILEPATH, file_name)

    # 可視化データを保存
    net.save_graph(file_path)
    return file_name