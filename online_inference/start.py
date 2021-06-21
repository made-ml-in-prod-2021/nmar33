import uvicorn
import time

if __name__ == '__main__':
    time.sleep(30)
    uvicorn.run('online_inference:app', host='0.0.0.0', port=8000)