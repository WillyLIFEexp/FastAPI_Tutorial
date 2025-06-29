from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: str | None = None

# ✅ Add this class to fix your error
class RefreshTokenRequest(BaseModel):
    refresh_token: str
