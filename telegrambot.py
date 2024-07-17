from telethon import TelegramClient, events


client = TelegramClient('bot', App api_id, App api_hash).start(bot_token='bot_token')

@client.on(events.NewMessage(pattern='/mentionwindy'))
async def mention_all(event):
    if event.is_group or event.is_channel:
        chat = await event.get_input_chat()
        members = await client.get_participants(chat)
        mentions = []
        for member in members:
            if not member.bot:
                mention = f"<a href='tg://user?id={member.id}'>🐳</a>"
                mentions.append(mention)
        mention_text = ' '.join(mentions)
        await event.reply(mention_text, parse_mode='html')
    else:
        await event.reply('This command can only be used in groups or channels.')

client.start()
client.run_until_disconnected()
