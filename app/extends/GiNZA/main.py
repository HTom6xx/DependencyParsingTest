from concurrent import futures
import grpc
from proto import ginza_pb2, ginza_pb2_grpc

from modules.text_process import DependencyProcess
dp = DependencyProcess()

GINZA_SERVICE_PORT = 8080

class Responces(ginza_pb2_grpc.GiNZAServiceServicer):
    def DependencyParsing(self, request, context):
        """_summary_ 係り受け解析のレスポンス定義

        Args:
            request (_type_): _description_
            context (_type_): _description_

        Returns:
            _type_: _description_
        """
        message = request.msg
        words = dp(message)
        res = []
        for word in words:
            temp = ginza_pb2.Word()
            temp.ind = word['ind']
            temp.word = word['word']
            temp.parent_ind = word['parent_ind']
            res.append(temp)

        return ginza_pb2.DependencyParsingResponse(res=res)
    
def main():
    # WebUI側と通信するためにgRPCサーバーを起動
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    ginza_pb2_grpc.add_GiNZAServiceServicerServicer_to_server(Responces(), server)

    server.add_insecure_port(f'[::]:{GINZA_SERVICE_PORT}')
    server.start()
    server.wait_for_termination()
    

if __name__ == '__main__':
    main()