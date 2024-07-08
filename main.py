from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from time import sleep
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-amp")
async def get_amp(request: Request, rotated: bool, __amp_source_origin: str):
    # Check campaign date
    start_date = datetime(2024, 6, 1)
    end_date = datetime(2024, 6, 7)
    current_date = datetime.now()
        # Check HTTP requests
    origin = request.headers.get("Origin")
    amp_email_sender = request.headers.get("AMP-Email-Sender")

    if amp_email_sender:
        sender_email = amp_email_sender
        headers = {
            "AMP-Email-Allow-Sender": sender_email,
            "Content-Type": "application/json"
        }
    elif origin:
        if not __amp_source_origin:
            raise HTTPException(status_code=400, detail={"message":"Çark çevilirken bir hata oluştu. Lütfen tekrar deneyin."},headers=headers)
        
        headers = {
            "Access-Control-Allow-Origin": "*",
            "AMP-Access-Control-Allow-Source-Origin": __amp_source_origin,
            "Access-Control-Expose-Headers": "AMP-Access-Control-Allow-Source-Origin",
            "Content-Type": "application/json"
        }
    else:
        raise HTTPException(status_code=400, detail={"message":"Çark çevilirken bir hata oluştu. Lütfen tekrar deneyin."},headers=headers)

    if not (start_date <= current_date <= end_date):
        sleep(5)
        raise HTTPException(status_code=400, detail={"message":"Kampanya 1-7 Haziran 2024 arasında geçerlidir."},headers=headers)
    
    
    
    # Simulate request processing delay
    sleep(5)
    
    # Return response with headers
    return JSONResponse(status_code=200, content={"message": "Request processed successfully"}, headers=headers)
