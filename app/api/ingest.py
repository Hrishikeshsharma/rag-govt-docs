from fastapi import FastAPI, File, UploadFile, APIRouter

router = APIRouter()

@router.post("/upload")
async def upload_file(file:UploadFile = File(...)):
    filepath = f"/data/uploads/{file.filename}"

    with open(filepath, 'wb') as f:
        f.write(await file.read())



    return {
        "filename":{file.filename},
        "message":"Document loaded succssfully"
    }