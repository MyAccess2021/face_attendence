from supabase import create_client, Client

# Replace these with your Supabase project credentials
SUPABASE_URL =  "https://dsvqjsnxdxlgufzwcaub.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRzdnFqc254ZHhsZ3VmendjYXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA4MjgyMjMsImV4cCI6MjA2NjQwNDIyM30.YHdiWzPvU6XBXFzcDZL7LKtgjU_dv5pVVpFRF8OkEz8"

# Create and expose the Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
