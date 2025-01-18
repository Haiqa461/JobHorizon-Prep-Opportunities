from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

#response = supabase.table("tut1").select("*").execute()
# response = (
#     supabase.table("tut1")
#     .insert({"id": 2, "name": "Denmark"})
#     .execute()
# )

response = (
    supabase.table("tut1")
    .update({"name": "Haiqa"})
    .eq("id", 2)
    .execute()
)


print(response)