from pydantic import BaseModel, ConfigDict


class ExtraIgnoreModel(BaseModel):
    model_config = ConfigDict(extra='ignore')
