from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class SourceSchema(BaseModel):
    id: Optional[int] = None
    name: str
    type: str = Field(..., description="rss|telegram|manual|other")
    url: Optional[str] = None


class RawEventSchema(BaseModel):
    id: Optional[int] = None
    source_id: int
    external_id: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None
    created_at: Optional[datetime] = None


class InfoCardSchema(BaseModel):
    id: Optional[int] = None
    title: str
    summary: Optional[str] = None
    tags: List[str] = []
    source_ids: List[int] = []
    importance: Optional[float] = None


class FeedbackSchema(BaseModel):
    id: Optional[int] = None
    info_card_id: int
    is_useful: Optional[bool] = None
    rating: Optional[int] = Field(default=None, ge=1, le=5)
    created_at: Optional[datetime] = None


class UserNoteSchema(BaseModel):
    id: Optional[int] = None
    info_card_id: int
    content: str
    created_at: Optional[datetime] = None


class TradeSignalSchema(BaseModel):
    id: Optional[int] = None
    info_card_id: int
    symbol: Optional[str] = None
    direction: Optional[str] = None
    entry_range: Optional[str] = None
    stop_loss: Optional[str] = None
    take_profit: Optional[str] = None
