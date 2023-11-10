from fastapi import FastAPI
import uvicorn
from api import weather_api
from views import home


app = FastAPI()

def configure():
    app.include_router(home.router)
    app.include_router(weather_api.router)

configure()

if __name__ == '__main__':
    uvicorn.run(app)