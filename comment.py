import asyncio
from telethon import TelegramClient, events
import random

cmt_list = r'D:\Python\Telegram\cmt_list.txt'

# Hàm để lấy một dòng ngẫu nhiên từ file
def get_random_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return random.choice(lines).strip()

# Hàm để lấy nhiều dòng ngẫu nhiên từ file
def get_multiple_random_lines(file_path, num_lines=5):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return random.sample(lines, min(num_lines, len(lines)))

# Khởi tạo và cấu hình bot1
bot1 = TelegramClient('bot1_session', 21944258, '8b3008b5efdbaec2c0b025b4b971d14e').start(bot_token='7089848482:AAGBUUbvkNSOTtOlgAZCzw9p3vsXabQiTc8')

@bot1.on(events.NewMessage(pattern='(?i).*comment.*'))
async def handle_rude_message_bot1(event):
    vid1 = r'C:\Users\LENOVO\Pictures\gif\creepy-doraemon-by-error.mp4'
    if event.is_group or event.is_channel:
        # Gửi 5 dòng ngẫu nhiên từ danh sách comment
        await bot1.send_file(event.chat_id, vid1)
        random_comments = get_multiple_random_lines(cmt_list, 10)
        for comment in random_comments:
            await event.reply(comment.strip())

# Khởi tạo và cấu hình bot2
bot2 = TelegramClient('bot2_session', 27307404, '253f570f03234e6cd764c50c4494fe71').start(bot_token='7111216640:AAGOlB8TynK65pdDDy_gfBT9g2fBXTkR860')

@bot2.on(events.NewMessage(pattern='(?i).*comment.*'))
async def handle_rude_message_bot2(event):
    if event.is_group or event.is_channel:
        vid2 = r'C:\Users\LENOVO\Pictures\gif\doraemon-cartoon-doraemon.mp4'
        await bot2.send_file(event.chat_id, vid2)
        # Gửi 5 dòng ngẫu nhiên từ danh sách comment
        random_comments = get_multiple_random_lines(cmt_list, 10)
        for comment in random_comments:
            await event.reply(comment.strip())

# Khởi tạo và cấu hình bot3
bot3 = TelegramClient('bot3_session', 29442830, 'ece5878abf0bf7ae17aec73d6bc96f57').start(bot_token='7391039518:AAEveDIko-7UmBPBFGzx3Ikiv8VIR0lNCUM')

@bot3.on(events.NewMessage(pattern='(?i).*comment.*'))
async def handle_rude_message_bot3(event):
    if event.is_group or event.is_channel:
        vid3 = r'C:\Users\LENOVO\Pictures\gif\pikachu-pokemon.mp4'
        await bot2.send_file(event.chat_id, vid3)
        # Gửi 5 dòng ngẫu nhiên từ danh sách comment
        random_comments = get_multiple_random_lines(cmt_list, 10)
        for comment in random_comments:
            await event.reply(comment.strip())

# Hàm để khởi động các bot với thời gian chờ giữa các lần kết nối
async def start_bots():
    await bot1.connect()
    await asyncio.sleep(2)  # Thêm thời gian chờ giữa các kết nối
    await bot2.connect()
    await asyncio.sleep(2)
    await bot3.connect()

async def main():
    await start_bots()
    await asyncio.gather(
        bot1.run_until_disconnected(),
        bot2.run_until_disconnected(),
        bot3.run_until_disconnected()
    )

# Khởi động các bot
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
