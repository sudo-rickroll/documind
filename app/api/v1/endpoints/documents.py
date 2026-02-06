from fastapi import APIRouter, HTTPException
from app.schemas.document import DocumentCreate
from app.services.cache_service import CacheService
import uuid

router = APIRouter()

cache_service = CacheService()

@router.post("/", status_code=201)
async def create_document(doc: DocumentCreate):
    doc_id = str(uuid.uuid4())

    doc_data = {
        "id": doc_id,
        "content": doc.content,
        "status": "cached"
    }

    await cache_service.set_document(doc_id, doc_data)

    return doc_data

@router.get("/{doc_id}")
async def get_document(doc_id: str):
    doc = await cache_service.get_document(doc_id)

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    
    return doc
