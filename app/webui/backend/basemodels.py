from pydantic import BaseModel

class TextSource(BaseModel):
    source_text: str    # 入力文字列