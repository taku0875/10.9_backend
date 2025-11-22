from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all for MVP
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/results")
def create_result(result: models.MeasurementResultCreate, db: Session = Depends(get_db)):
    db_result = models.MeasurementResult(
        eye=result.eye,
        distance=result.distance,
        visual_acuity=result.visual_acuity
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

@app.get("/api/results")
def read_results(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    results = db.query(models.MeasurementResult).offset(skip).limit(limit).all()
    return results
