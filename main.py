from aiogram.utils import executor
from config import dp
from handlers import client, callback, extra, admin, fsmAdminMenu, inline
from database.bot_db import sql_create


async def on_startup(_):
    sql_create()


client.register_handlers_client(dp)
fsmAdminMenu.register_handlers_fsmAdminMenu(dp)
callback.register_handlers_callback(dp)
admin.register_handler_admin(dp)
inline.register_handler_inline(dp)
extra.register_handlers_extra(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

