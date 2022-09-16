from pydantic import BaseModel  
from typing import Optional

class RacesSchema(BaseModel):
    raceId: Optional[int]
    year: int
    round: int
    circuitId: Optional [int]
    name: str
    date: str
    time: str
    url: str

class DriversSchema(BaseModel):
    driverId : Optional[int]
    driverRef : str
    number : str 
    code : str 
    dob : str 
    nationality : str 
    url : str 
    forename : str 
    surname : str 


class CircuitsSchema(BaseModel):
    circuitId : Optional [int]
    circuitRef : str 
    name : str 
    location : str 
    country : str 
    lat : str 
    lng : str 
    alt : str 
    url : str 


class ResultsSchema(BaseModel):
    resultId : Optional[int]
    raceId : Optional[int] 
    driverId : Optional[int] 
    constructorId : Optional [int] 
    number : str 
    grid : int 
    position : str 
    positionText : int 
    positionOrder : int 
    points : int 
    laps : int 
    time : int 
    milliseconds : int 
    fastestLap : int 
    rank : int 
    fastestLapTime : int 
    fastestLapSpeed : int 
    statusId : int 

class ConstructorsSchema(BaseModel):
    constructorId : Optional[int] 
    constructorRef : str 
    name : str 
    nationality : str 
    url : str 

