from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from time import sleep
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

trusted_emails = ["trusted@example.com"]  # Güvendiğiniz e-posta adreslerini burada tanımlayın

@app.get("/get-amp")
async def get_amp(request: Request, rotated: bool, __amp_source_origin: str):
    # HTTP isteklerini kontrol edin
    origin = request.headers.get("Origin")
    amp_email_sender = request.headers.get("AMP-Email-Sender")
    
    if amp_email_sender:
        sender_email = amp_email_sender
        if sender_email not in trusted_emails:
            raise HTTPException(status_code=403, detail="Untrusted email sender")
        headers = {
            "AMP-Email-Allow-Sender": sender_email,
            "Content-Type": "application/json"
        }
    elif origin:
        request_origin = origin
        if not __amp_source_origin:
            raise HTTPException(status_code=400, detail="Missing __amp_source_origin query parameter")
        
        sender_email = __amp_source_origin
        
        headers = {
            "Access-Control-Allow-Origin": "*",
            "AMP-Access-Control-Allow-Source-Origin": "*",
            "Access-Control-Expose-Headers": "*",
            "Content-Type": "application/json"
        }
    else:
        raise HTTPException(status_code=400, detail="Missing Origin or AMP-Email-Sender headers")
    
    # İsteği bekletin
    sleep(7)
    
    # Yanıtı başlıklarla birlikte döndürün
    return JSONResponse(status_code=200, content={"message": "Request processed successfully"}, headers=headers)
