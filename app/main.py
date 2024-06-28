from fastapi import FastAPI

from app.envelopes.router import router as router_envelopes
from app.users.router import router as router_users
from app.transactions.router import router as router_transactions
from app.transactions.categories.router import router as rouer_category

app = FastAPI()

app.include_router(router_users)
app.include_router(router_envelopes)
app.include_router(router_transactions)
app.include_router(rouer_category)


