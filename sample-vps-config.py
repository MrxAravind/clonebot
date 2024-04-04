import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "6950272759:AAHrEHcqUszah81a1_rTP0DDM5xPbv_9v0M"
    APP_ID = 12725757
    API_HASH = "29e30e8d134c122f3733cc52891edd48"
    TG_USER_SESSION = "AQDCLf0APtlmB9YNqb-AYklrgSnzziKR9YeIM0mRm0E_ozr0Zckiv185YjjWvlYOeH9fJvXBp32v7DUbWqEcShxT1AYzn0GFFcN39qkg6TR2NnKROrFY8VM6Ju_n7P05isyeHa2CRb-2MIozXeh1yFBXUF_V-XF8ZZWGMaqBPbXq02z54DHbqzftROoTz0QXneNN4cE_gOttDDsxlItVbjlVEbUDObOy0jRsjAZ77Nvt-Td1ui5UNmzaaJqng6ENuW-BC3-p6u8hrDZ_nwT8SD8eQQt5hAyjq1wYE7GqGhQ2-NkUS59UVoassyhw4qXtmFrO-6J86XriblwcN-SdfCTbrXBexAAAAABlegy-AA"
    DB_URI = "mongodb+srv://boxopo9982:Lsq1hH7iRliG7jZy@switchbot.wtmkb7q.mongodb.net/?retryWrites=true&w=majority"

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
