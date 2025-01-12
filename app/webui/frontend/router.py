from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """_summary_ トップページを返す。

    Args:
        request (Request): _description_

    Returns:
        _type_: _description_
    """
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)