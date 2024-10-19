# TEAM DAXX ALL COPYRIGHT ©️
from pyrogram import filters
import os

class Config:
    API_ID = "28243586"
    API_HASH = "4022d5686b9b7a7cf8891205921a0ab3"
    TOKEN = "7489087428:AAHRuMjgt5LiE9QLUsfUm-2JG16x1r0CKec"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://anmol0700:anmol0700@cluster0.x6zba.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    START_PIC = "https://telegra.ph/file/a8ba8edd60489a54f2f84.jpg"
    SUDOERS = filters.user(["6929340267"])
