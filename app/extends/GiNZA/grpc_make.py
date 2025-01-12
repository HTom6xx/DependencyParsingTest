from grpc.tools import protoc
from glob import glob
protos = glob('./proto/*.proto', recursive=True)

protoc.main(
    (
        '',
        '-I.',
        f'--pyi_out=.',
        f'--python_out=.',
        f'--grpc_python_out=.',
        *protos
    )
)