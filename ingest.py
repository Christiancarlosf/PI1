import pandas as pd
from sqlalchemy import create_engine
import json 

races = pd.read_csv("Datasets/races.csv", index_col=[0])
circuits = pd.read_csv("Datasets/circuits.csv", index_col=[0])
constructors = pd.read_json("Datasets/constructors.json")
results = pd.read_json("Datasets/results.json")
#lap_times_1 = pd.read_csv("Datasets/lap_times/lap_times_split_1.csv", index_col=[0])
#lap_times_2 = pd.read_csv("Datasets/lap_times/lap_times_split_2.csv", index_col=[0])
#lap_times_3 = pd.read_csv("Datasets/lap_times/lap_times_split_3.csv", index_col=[0])
#lap_times_4 = pd.read_csv("Datasets/lap_times/lap_times_split_4.csv", index_col=[0])
#lap_times_5 = pd.read_csv("Datasets/lap_times/lap_times_split_5.csv", index_col=[0])

#pit_stops = pd.read_json("Datasets/pit_stops.json")

with open("Datasets/drivers.json", encoding="UTF-8") as f:
    drivers = json.load(f)
    
drivers = pd.json_normalize(drivers)
drivers = drivers.rename(columns={'name.forename': 'forename','name.surname': 'surname' })

engine = create_engine('postgresql://root:root@localhost:5432/ChrisPI')

engine.connect()

races.to_sql(name='races', con=engine, if_exists='replace')
circuits.to_sql(name='constructors', con=engine, if_exists='replace')
constructors.to_sql(name='constructors', con=engine, if_exists='replace')
results.to_sql(name='results', con=engine, if_exists='replace')
drivers.to_sql(name='drivers', con=engine, if_exists='replace')
#pit_stops.to_sql(name='pit_stops', con=engine, if_exists='replace')
#qualifying.to_sql(name='qualifying', con=engine, if_exists='replace')
#pit_stops.to_sql(name='pit_stops', con=engine, if_exists='replace')
#qualifying.to_sql(name='qualifying', con=engine, if_exists='replace')

