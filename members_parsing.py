# Telegram members parser - Power async tool for parsing telegram members
# Copyright (c) 2025 Treizd
#
# This file is part of telegram_members_parser project.
#
# members_parsing is free software: you can redistribute it and/or modify
# it under the terms of the MIT License. See the LICENSE file for details.


from pyrogram import Client
import asyncio
import json

# Better putting this in .env file!
API_ID = 123456789
API_HASH = "YOURAPIHASH"
CHAT_TO_PARSE = -100123456789 # Chat ID to parse. Must be group ID, supergroup ID or channel ID. Requires admin rights for channels
PATH_TO_SAVE = "users.json" # Must be .json file

class User:
    def __init__(self, user_id: int, first_name: str = None, last_name: str = None, username: str = None, is_premium: str = False):
        # For devs: you can add more attributes. See the get_chat_mm
        self.user_id = user_id
        self.first_name = first_name or "None"
        self.last_name = last_name or "None"
        self.username = f"@{username}" if username else "None"
        self.is_premium = is_premium
    
    def __str__(self):
        return f'User(user_id={self.user_id}, first_name="{self.first_name}", last_name="{self.last_name}", username="{self.username}", is_premium="{self.is_premium}")'

    def __dict__(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "is_premium": self.is_premium
        }

async def main():
    app = Client("my_account", api_id=API_ID, api_hash=API_HASH)

    try:
        await app.start()
        
        users = []
        async for user in app.get_chat_members(chat_id=CHAT_TO_PARSE):
            if not user.user.is_bot:
                users.append(User(user_id=user.user.id, first_name=getattr(user.user, "first_name", None), last_name=getattr(user.user, "last_name", None), username=getattr(user.user, "username", None), is_premium=user.user.is_premium).__dict__())

        with open(PATH_TO_SAVE, "w", encoding="utf-8") as f: # For devs: consider using aiofiles for unblockin I/O operations
            json.dump(users, f, indent=4, ensure_ascii=False)
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        await app.stop()

if __name__ == "__main__":
    asyncio.run(main())


