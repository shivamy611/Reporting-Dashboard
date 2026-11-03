from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ReportIn(BaseModel):
    title: str
    description: str = ""
    category: str = ""


class ReportOut(ReportIn):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
