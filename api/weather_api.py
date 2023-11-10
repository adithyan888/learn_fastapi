import fastapi

from models.location import Location
from models.umbrella_status import UmbrellaStatus
from services import live_weather_service

router = fastapi.APIRouter()

@router.get('/api/umbrella')
async def do_i_need_an_umbrella(location: Location = fastapi.Depends()):

    data = await live_weather_service.get_live_report(location)
    weather = data.get('weather', {})
    category = weather.get("category", 'UNKNOWN')

    forecast = data.get('forecast', {})
    temp = forecast.get('temp', 0)

    bring = category.lower().strip() == "rain"

    return UmbrellaStatus(bring_umbrella=bring, temp=temp, weather=category)