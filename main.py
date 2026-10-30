from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import pandas as pd
import joblib
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. SETUP DATABASE NEON.TECH
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://neondb_owner:npg_03IHNAtYGSOJ@ep-young-bonus-azderjcl-pooler.c-3.ap-southeast-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Struktur Tabel Database (Tambah Kolom Patient_Name)
class RiwayatPasien(Base):
    __tablename__ = "riwayat_prediksi"
    id = Column(Integer, primary_key=True, index=True)
    Patient_Name = Column(String) # <--- TAMBAHAN BARU
    Age = Column(Integer)
    Gender = Column(String)
    Heart_Rate_bpm = Column(Integer)
    Oxygen_Saturation = Column(Integer)
    Systolic = Column(Integer)
    Diastolic = Column(Integer)
    Body_Temperature = Column(Float)
    Body_ache = Column(Integer)
    Shortness_of_breath = Column(Integer)
    Cough = Column(Integer)
    Fatigue = Column(Integer)
    Sore_throat = Column(Integer)
    Fever = Column(Integer)
    Headache = Column(Integer)
    Runny_nose = Column(Integer)
    Diagnosis = Column(String)
    Severity = Column(String)
    Treatment_Plan = Column(String)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistem Diagnosa Penyakit API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model_diagnosis = joblib.load('models/model_diagnosis.joblib')
model_severity = joblib.load('models/model_severity.joblib')
model_treatment = joblib.load('models/model_treatment_plan.joblib')

# Format Data Input (Tambah Patient_Name)
class PatientData(BaseModel):
    Patient_Name: str # <--- TAMBAHAN BARU
    Age: int
    Heart_Rate_bpm: int
    Oxygen_Saturation: int = Field(alias="Oxygen_Saturation_%")
    Systolic: int
    Diastolic: int
    Body_Temperature: float
    Male: int
    Female: int
    Body_ache: int = Field(alias="Body ache")
    Shortness_of_breath: int = Field(alias="Shortness of breath")
    Cough: int
    Fatigue: int
    Sore_throat: int = Field(alias="Sore throat")
    Fever: int
    Headache: int
    Runny_nose: int = Field(alias="Runny nose")

@app.post("/predict")
def predict_disease(patient: PatientData):
    data_dict = patient.dict(by_alias=True)
    
    # Hapus Nama sebelum masuk ke Model ML agar tidak error
    ml_input = data_dict.copy()
    del ml_input["Patient_Name"]
    df_input = pd.DataFrame([ml_input])
    
    pred_diagnosis = str(model_diagnosis.predict(df_input)[0])
    pred_severity = str(model_severity.predict(df_input)[0])
    pred_treatment = str(model_treatment.predict(df_input)[0])
    
    db = SessionLocal()
    try:
        db_record = RiwayatPasien(
            Patient_Name=data_dict["Patient_Name"], # Simpan Nama ke DB
            Age=data_dict["Age"],
            Gender="Laki-laki" if data_dict["Male"] == 1 else "Perempuan",
            Heart_Rate_bpm=data_dict["Heart_Rate_bpm"],
            Oxygen_Saturation=data_dict["Oxygen_Saturation_%"],
            Systolic=data_dict["Systolic"],
            Diastolic=data_dict["Diastolic"],
            Body_Temperature=data_dict["Body_Temperature"],
            Body_ache=data_dict["Body ache"],
            Shortness_of_breath=data_dict["Shortness of breath"],
            Cough=data_dict["Cough"],
            Fatigue=data_dict["Fatigue"],
            Sore_throat=data_dict["Sore throat"],
            Fever=data_dict["Fever"],
            Headache=data_dict["Headache"],
            Runny_nose=data_dict["Runny nose"],
            Diagnosis=pred_diagnosis,
            Severity=pred_severity,
            Treatment_Plan=pred_treatment
        )
        db.add(db_record)
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        db.close()
    
    return {
        "Diagnosis": pred_diagnosis,
        "Severity": pred_severity,
        "Treatment_Plan": pred_treatment
    }

@app.get("/riwayat")
def get_riwayat():
    db = SessionLocal()
    data = db.query(RiwayatPasien).order_by(RiwayatPasien.id.desc()).all()
    db.close()
    return data

@app.put("/riwayat/{id}")
def update_riwayat(id: int, patient: PatientData):
    db = SessionLocal()
    try:
        record = db.query(RiwayatPasien).filter(RiwayatPasien.id == id).first()
        if not record: return {"status": "error"}
        
        data_dict = patient.dict(by_alias=True)
        
        # Hapus Nama sebelum prediksi ulang
        ml_input = data_dict.copy()
        del ml_input["Patient_Name"]
        df_input = pd.DataFrame([ml_input])
        
        record.Patient_Name = data_dict["Patient_Name"]
        record.Age = data_dict["Age"]
        record.Gender = "Laki-laki" if data_dict["Male"] == 1 else "Perempuan"
        record.Heart_Rate_bpm = data_dict["Heart_Rate_bpm"]
        record.Oxygen_Saturation = data_dict["Oxygen_Saturation_%"]
        record.Systolic = data_dict["Systolic"]
        record.Diastolic = data_dict["Diastolic"]
        record.Body_Temperature = data_dict["Body_Temperature"]
        record.Body_ache = data_dict["Body ache"]
        record.Shortness_of_breath = data_dict["Shortness of breath"]
        record.Cough = data_dict["Cough"]
        record.Fatigue = data_dict["Fatigue"]
        record.Sore_throat = data_dict["Sore throat"]
        record.Fever = data_dict["Fever"]
        record.Headache = data_dict["Headache"]
        record.Runny_nose = data_dict["Runny nose"]
        
        record.Diagnosis = str(model_diagnosis.predict(df_input)[0])
        record.Severity = str(model_severity.predict(df_input)[0])
        record.Treatment_Plan = str(model_treatment.predict(df_input)[0])
        
        db.commit()
        return {"status": "success", "Diagnosis": record.Diagnosis, "Severity": record.Severity, "Treatment_Plan": record.Treatment_Plan}
    except Exception as e:
        db.rollback()
        return {"status": "error"}
    finally:
        db.close()

@app.delete("/riwayat/{id}")
def delete_riwayat(id: int):
    db = SessionLocal()
    try:
        record = db.query(RiwayatPasien).filter(RiwayatPasien.id == id).first()
        if record: db.delete(record); db.commit()
        return {"status": "success"}
    finally: db.close()