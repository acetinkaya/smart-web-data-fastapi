from fastapi import FastAPI
from app.routes.currency import router as currency_router

app = FastAPI(
    title="Smart Web Data FastAPI",
    description="TCMB XML verisini çekip FastAPI ile sunan uygulama",
    version="1.0.0"
)

app.include_router(currency_router)

@app.get("/")
def home():
    return {
        "message": "Smart Web Data FastAPI çalışıyor.",
        "docs": "/docs"
    }
