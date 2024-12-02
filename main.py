import uvicorn
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log", mode="a", encoding="utf-8")
    ]
)

if __name__ == "__main__":
    logging.info("Starting the application...")
    uvicorn.run("app.app:app", host="0.0.0.0", log_level="info", reload=True)
    logging.info("Application has been stopped.")
