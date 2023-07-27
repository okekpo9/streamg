import streamlit as st
import pandas as pd #if you will
import gspread
from google.oauth2 import service_account


# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets[{
  "type": "service_account",
  "project_id": "powerful-host-394016",
  "private_key_id": "2a8e5cde323012af5814c207d0a1358cc6553cac",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCd9MIyxEZXlNh0\niwbMrfehfB8iuCnPTuH1ceMFLrIzWuDw7VSWjSew/Tg97/7MjSsJeWvAsd0fcCH5\nZqazychqYkefkMF+k/rBN+rSqVy8SuRIFUVy4b/91p1/xnck5eBiDLFZhVqjdKY+\nOgvcq265/Vi/Ru911+rR4X9MAsyuTEfT6h9Q6MeRPddvZMUlUtw5zT30cigMO/Gj\nT7IZu1lhYpNkXP3JbnV8U2u0z7Giw33pZ3Xg1DOYVPI7gDElGUxV0r/MYkS6kUWI\nYd3pdL5E6qswACriB8cyUBa0yffU/Kz90IOxbxvbp40vNZp4ZRCTkgb6syzVFWqw\nQXXbz0r9AgMBAAECggEAAndqMF5EkTgEqCTGpcs4FFNI1BFsmbWIff0z9HhMb94T\nQB6po1iOgmxQVUVVh1i29+96kgS9SFJVnEqQ0BSpoesKi3Szs3PdYxfsYOdAvxo+\nRleUK7BE/79lmIjBeRyZcR+xgQi96jGa55zrNASHIVaw1SD6C1UWLc1LaZbdYSe3\nhazN3X2+K3swZlSrbgOcgkgKAq+X9LipuQ/qQIiDyhD2X1M1YBRBzzfD+KKTh3j7\nuyrEHU9/mKYim5XldFDItkeaze69HP+55LhM4agj6OpFCZnSE8JAsZxd13s6Y/Pf\nv/IDnjQARzv9InYbhLFTtWEN+AQgeZdFXmaeJPPUIwKBgQDUDcFjSHDtnHQR++KM\nVFBQrB04rtnA+VYlYLxgNLmuNvB4cdDTOPcoEKHLTs0iuEGojUolrr2evuDLTivY\nz57iZN4P3yajmlyoIi8XPvELkLQrXozvSTMQOHkzDdC8OxnAwWTdsNEdhputb+gv\njYyvlOhul7RddqTyoTxJ+O912wKBgQC+sOuq0scNE3j1T1RdKMSnKZ3q6qChsui1\nCnpKUcEGHqmRWBPjJEM5JnXCTSA5zbxe2CzaxNL7tgWFwYg/YFGnfyWtvXSujA8u\n0J67JqcDkethWFp4CpRnSv79x+cjPoWQJ0fswIv9yqH7t53cztRB6OEUl1aAhOlV\nVhnZYZrWBwKBgHBLwIflSvhqDAWiEH0kAUxXeToVTnelEvvEWL3R7irWKU5/Z4kT\n978d37Cc0IF8djjeac++0+gHSWAgy5OLj6ZwqDBbikjFbCAVyj5TNK9dOCxna9ck\nOohyf6yLumiUG7U6NUI5auRp7nNQefME0OYCw3wdloSQWhWrURQTYixVAoGAOyXV\nc579bujjU/PPTzYeCVu3R+6O9Jjx5XXiiLrjDGrmXdbcFFBjKY7sZ+BUZpmSHDkh\ncJosdzb2b46gHEhcC4A8x69ESf/XlcXP9mz+0PSp9f/Zz/I4JfH1NfKTlzMFarlE\nbgMraQU5SUKjDKJ65Ba/+gsXIbYYSgfy7KKBzHECgYBwhBMsOVB35HNXwio7jicI\n3agnchpij3xRT/4k5nCZUO2+GQghmYdyZod8Lhs4Q0M+RTlVem2GK4AJS3aM9tWv\nQX0SNu6ZCvDtOhHh8RWSh44f+cJdzD/78TSpj/LgrPpqqXv0RHCiR1eEUmvnGBZY\nadAm+r0jyA+JqFT3f8eXxA==\n-----END PRIVATE KEY-----\n",
  "client_email": "google-sheet-for-my-first-proj@powerful-host-394016.iam.gserviceaccount.com",
  "client_id": "101891064699912321214",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/google-sheet-for-my-first-proj%40powerful-host-394016.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"
    ],
)
conn = connect(credentials=credentials)
client=gspread.authorize(credentials)
sheet_id = '1JBnGyvodeB3gMWaVxEA5lUDN2xnM3gbZdE0G58WpgkM/edit#gid=1364046319'
csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
database_df = pd.read_csv(csv_url, on_bad_lines='skip')
database_df = database_df.astype(str)
sheet_url = st.secrets["private_gsheets_url"] #this information should be included in streamlit secret
sheet = client.open_by_url(sheet_url).sheet1
sheet.update([database_df.columns.values.tolist()] + database_df.values.tolist())
st.success('Data has been written to Google Sheets')


