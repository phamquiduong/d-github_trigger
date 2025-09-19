from pydantic import BaseModel, ConfigDict


class WebhookRequestBase(BaseModel):
    model_config = ConfigDict(extra='ignore')
