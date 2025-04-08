from app.main import app

if __name__ == "__main__":
    import uvicorn
    import os
    from dotenv import load_dotenv

    load_dotenv()

    app_host = os.getenv("APP_HOST")  
    app_port = int(os.getenv("APP_PORT"))  

    print(f"🚀 Starting server at http://{app_host}:{app_port}")

    uvicorn.run(app, host=app_host, port=app_port)
