import os
from dotenv import load_dotenv
from supabase import create_client
from project import stations, name_passenger, selected_station, station_price
load_dotenv()

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

inserting = (supabase.table("metro database").insert({"id": 2, "name": name_passenger, "station name": selected_station, "price": station_price}).execute())
response = supabase.table('metro database').select("*").execute()
print(response)