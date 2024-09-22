from app import app
import routing

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, port=8082, host="0.0.0.0")