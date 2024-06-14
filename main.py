from fastapi import FastAPI,Request
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

@app.get("/get-amp")
async def get_amp(request: Request, rotated: bool, __amp_source_origin: str):
    # Set the amp-access-control-allow-source-origin header to match the AMP source origin
    sleep(4)
    headers = {
        "AMP-Email-Allow-Sender": "*",
        "Content-Type": "application/json"  # Set the appropriate content type for your response
    }
    
    # Return a response with the headers set
    return JSONResponse(status_code=200, content={"message": "Request processed successfully"}, headers=headers)