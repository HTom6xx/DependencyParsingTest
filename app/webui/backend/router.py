import os, datetime
from fastapi import APIRouter, HTTPException

from .basemodels import TextSource
from fastapi.responses import JSONResponse, FileResponse
from .tasks import DependencyParsingTask, visualize_network

router = APIRouter()

@router.post("/DependencyParsing")
async def dependency_parsing(req: TextSource):
    """_summary_ 係り受け解析を実行

    Args:
        req (TextSource): 処理するテキストのリクエスト
        
    Returns:
        _type_: 結果ファイル名
    """
    try:
        da = DependencyParsingTask()
        result = da(req.source_text)
        file_name = visualize_network(result)
    except Exception as ex:
        print(ex)
        raise HTTPException(status_code=500, detail=f"Error:{ex}")

    return JSONResponse(content={'file_name': file_name})


@router.get("/download/{file_name}")
async def cache(file_name: str):
    """_summary_ ファイルをコンテナ内ボリュームからダウンロード

    Args:
        file_name (str): ファイル名

    Raises:
        HTTPException: ファイルが見つからない場合

    Returns:
        _type_: FileResponse
    """
    file_path = os.path.join('../cache', file_name)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"({file_name}) not found")
    response = FileResponse(
        path=file_path,
        filename=f'{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.html')
    return response