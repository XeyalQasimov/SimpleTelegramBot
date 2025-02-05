import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import re

# Tokeni daxil et
TOKEN = "7853209835:AAFeJ7BnQ58czODvqvLRfDc0OhvoJssm19I"

# Bot və Dispatcher obyektlərini yarat
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Silinəcək sözlər
forbidden_words = [r"(?i)\b(fərid|ferid|farid|Farid)\b"]

# Mesajları yoxlayan funksiya
@dp.message()
async def delete_forbidden_messages(message: Message):
    if message.text:  # Mesajın text olub-olmadığını yoxlayırıq
        for word in forbidden_words:
            if re.search(word, message.text):
                await message.delete()
                break  # Mesaj silindisə, əlavə yoxlamağa ehtiyac yoxdur

# Asinxron bot funksiyası
async def main():
    print("Bot işə düşdü...")  # Terminalda botun başladığını görmək üçün
    await dp.start_polling(bot)

# Botu başlat
asyncio.run(main())