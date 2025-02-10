from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field
from pydantic_extra_types.payment import PaymentCardNumber


class PaymentMethodBase(BaseModel):
    user_id: int
    card_number: PaymentCardNumber = Field(default='4111111111111111')
    expiry_date: date
    cardholder_name: str = Field(..., max_length=100)
    billing_address: str = Field(..., max_length=255)


class PaymentMethodCreate(PaymentMethodBase):
    pass


class PaymentMethodInDB(PaymentMethodBase):
    payment_method_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class PaymentMethodResponse(PaymentMethodBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
