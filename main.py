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
async def root(request: Request):
    # Get the AMP source origin from the request headers
    amp_source_origin = request.headers.get("AMP-Same-Origin", None)
    
    # Validate the AMP source origin
    sleep(5)
    if not amp_source_origin:
        return JSONResponse(status_code=400, content={"error": "AMP-Same-Origin header missing"})
    
    # Set the amp-access-control-allow-source-origin header to match the AMP source origin
    headers = {
        "amp-access-control-allow-source-origin": amp_source_origin,
        "Content-Type": "application/json"  # Set the appropriate content type for your response
    }
    
    # Return a response with the headers set
    return JSONResponse(status_code=200, content={"message": "Form submitted successfully"}, headers=headers)
