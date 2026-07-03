import json
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils.exceptions import BotBlocked, ChatNotFound
from loader import bot, dp

def load_user_ids(filename="id.txt"):
    user_ids = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            user_ids.append(int(line))

    return user_ids



async def main():
    user_ids = load_user_ids("id.txt")


    user_ids = list(set(user_ids))


    text = """На старт, внимание... ! 🔥 
Триатлон-квест по Тюмени стартует прямо сейчас! 🚀  
Впереди крутой маршрут, исторические загадки и море драйва!⚡️

Не забудь:  
✅ Удобная обувь  
✅ Заряженный телефон  
✅ Спортивное настроение  

Жду тебя на площади у мультицентра «Контора пароходства» на ярмарке (ЭКСПО) IRONSTAR.
⚡️ 57.161551, 65.546579 ⚡️

Чтобы начать квест, жми 👉 /start в меню слева ↙️

☝️ Напомню, что пройти квест ты можешь в любой день <b>с 3 по 5 июля 2026.</b>
Главное - финишируй <b>не позднее 17:00</b> в воскресенье 5 июля. 
Увидимся на старте! 😎"""




    for user_id in user_ids:
        try:
            await bot.send_message(user_id, text)
            print(f"✅ Сообщение отправлено {user_id}")
            await asyncio.sleep(0.5)  # минимальная задержка, чтобы избежать спама
        except BotBlocked:
            print(f"⛔ Бот заблокирован пользователем {user_id}")
        except ChatNotFound:
            print(f"❌ Чат не найден для {user_id}")
        except Exception as e:
            print(f"⚠️ Ошибка при отправке {user_id}: {e}")

    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())