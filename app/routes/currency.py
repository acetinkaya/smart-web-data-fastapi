from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.services.tcmb_service import get_tcmb_currency_data
from app.utils.xml_parser import save_currency_history, create_currency_chart

router = APIRouter(
    prefix="/currency",
    tags=["Currency"]
)

@router.get("/tcmb")
def tcmb_currency():
    data = get_tcmb_currency_data()
    save_currency_history(data)
    return data

@router.get("/history")
def currency_history():
    from app.data.currency_history import load_history
    return load_history()

@router.get("/chart")
def currency_chart():
    chart_path = create_currency_chart()
    return FileResponse(chart_path)
