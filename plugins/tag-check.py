#All Rights Reserved! @xmysteriousx

from pyrogram import (
    Client,
    filters
)
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired
)
from pyrogram.types import (
    ChatPermissions,
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from configs import Config

async def anon_filter(_, __, m: Message):
    return bool(m.from_user is None and m.sender_chat)

anonymous = filters.create(anon_filter)

async def flt_admin(_, client, message):
    try:
        user = await client.get_chat_member(message.chat.id, message.from_user.id)
        return True if user.status in ["administrator", "creator"] else False
    except Exception:
        pass    

admin = filters.create(flt_admin)

@Client.on_message(~anonymous & ~admin & filters.group)
async def addorno(client, message):
    firs = message.from_user.first_name
    las = message.from_user.last_name
    chat_id = message.chat.id
    user_id = message.from_user.id
    REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("Unmute Me ⚠️",
                          url=Config.Bot_url)]])
    if Config.Tag_Name in firs:
        a=1
    elif las is not None:
        if Config.Tag_Name in las:
            a=1
        else:
            a=0
    elif user_id == 1023936257:
        a=1
    else:
        a=0
    if a == 0:
        await message.reply_text(text=f"""{message.from_user.mention} you have been muted because you have <b>not added</b> our group tag in your name!
        
If you want to <b>get unmuted</b> please follow the instructions below!👇:-

1. Put `{Config.Tag_Name}`(Tap to copy) in your name.
2. After setting the tag press the below <b>Unmute Me ⚠️</b> button and press /start to the bot and send the unmute command of the group you have been muted!

- send /{Config.unmute_command_1} if you have been muted in {Config.Group1_name}
- send /{Config.unmute_command_2} if you have been muted in {Config.Group2_name}
- send /{Config.unmute_command_3} if you have been muted in {Config.Group3_name}

If you do all the things correctly you will get unmuted instantly!""",
                                quote=True,
                                reply_markup=REPLY_MARKUP)
                                
        await client.restrict_chat_member(
            chat_id, user_id, ChatPermissions(can_send_messages=False)
        )        
      
#start
START_MSG = Config.START_MSG
@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(START_MSG)

#UNMUTE GROUP 1    
@Client.on_message(filters.command(Config.unmute_command_1) & filters.private)
async def unmute1(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    channel1 = Config.Group1_id
    firs = message.from_user.first_name
    las = message.from_user.last_name
    if Config.Tag_Name in firs:
        b=1
    elif las is not None:
        if Config.Tag_Name in las:
            b=1
        else:
            b=0
    else:
        b=0
    if b == 1:
        try:
            await client.restrict_chat_member(
                channel1, user_id, ChatPermissions(can_send_messages=True)
            )
            await message.reply_text(text=f"""{message.from_user.mention}, You have <b>unmuted yourself in {Config.Group1_name}</b> successfully!\nNow you can chat in our group as much as you want🥳""", reply_to_message_id=chat_id)
            await message._client.send_message(
            chat_id=Config.Log_Group,
            text=f"""👆 Below user is unmuted successfully-
<b>User</b> - {message.from_user.mention}
<b>User First Name</b> - {message.from_user.first_name}
<b>User Last Name</b> - {message.from_user.last_name}
<b>User id</b> - `{message.chat.id}`
<b>Unmuted Group</b> - {Config.Group1_name}"""
)
        except Exception:
            pass
    else:
        await message.reply_text(text=f"""Oh come on {message.from_user.mention}! You have still not added our group tag in your name!😡 So you are still muted😝

If you want to <b>get unmuted</b> please follow the instructions below!👇:-

1. Put `{Config.Tag_Name}`(Tap to copy) in your name.
2. After setting the tag send the unmute command of the group you have been muted!

- send /{Config.unmute_command_1} if you have been muted in {Config.Group1_name}
- send /{Config.unmute_command_2} if you have been muted in {Config.Group2_name}
- send /{Config.unmute_command_3} if you have been muted in {Config.Group3_name}

If you do all the things correctly you will get unmuted instantly!""",  reply_to_message_id=chat_id)

#UNMUTE GROUP 2 
@Client.on_message(filters.command(Config.unmute_command_2) & filters.private)
async def unmute2(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    channel2 = Config.Group2_id
    firs = message.from_user.first_name
    las = message.from_user.last_name
    if Config.Tag_Name in firs:
        b=1
    elif las is not None:
        if Config.Tag_Name in las:
            b=1
        else:
            b=0
    else:
        b=0
    if b == 1:
        try:
            await client.restrict_chat_member(
                channel2, user_id, ChatPermissions(can_send_messages=True)
            )
            await message.reply_text(text=f"""{message.from_user.mention}, You have <b>unmuted yourself in {Config.Group2_name}</b> successfully!\nNow you can chat in our group as much as you want🥳""", reply_to_message_id=chat_id)
            await message._client.send_message(
            chat_id=Config.Log_Group,
            text=f"""Below user is unmuted successfully-
<b>User</b> - {message.from_user.mention}
<b>User First Name</b> - {message.from_user.first_name}
<b>User Last Name</b> - {message.from_user.last_name}
<b>User id</b> - `{message.chat.id}`
<b>Unmuted Group</b> - {Config.Group2_name}"""
)
        except Exception:
            pass
    else:
        await message.reply_text(text=f"""Oh come on {message.from_user.mention}! You have still not added our group tag in your name!😡 So you are still muted😝

If you want to <b>get unmuted</b> please follow the instructions below!👇:-

1. Put `{Config.Tag_Name}`(Tap to copy) in your name.
2. After setting the tag send the unmute command of the group you have been muted!

- send /{Config.unmute_command_1} if you have been muted in {Config.Group1_name}
- send /{Config.unmute_command_2} if you have been muted in {Config.Group2_name}
- send /{Config.unmute_command_3} if you have been muted in {Config.Group3_name}

If you do all the things correctly you will get unmuted instantly!""",  reply_to_message_id=chat_id)

 #UNMUTE GROUP 3
@Client.on_message(filters.command(Config.unmute_command_3) & filters.private)
async def unmute3(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    channel3 = Config.Group3_id
    firs = message.from_user.first_name
    las = message.from_user.last_name
    if Config.Tag_Name in firs:
        b=1
    elif las is not None:
        if Config.Tag_Name in las:
            b=1
        else:
            b=0
    else:
        b=0
    if b == 1:
        try:
            await client.restrict_chat_member(
                channel3, user_id, ChatPermissions(can_send_messages=True)
            )
            await message.reply_text(text=f"""{message.from_user.mention}, You have <b>unmuted yourself in {Config.Group3_name}</b> successfully!\nNow you can chat in our group as much as you want🥳""", reply_to_message_id=chat_id)
            await message._client.send_message(
            chat_id=Config.Log_Group,
            text=f"""Below user is unmuted successfully-
<b>User</b> - {message.from_user.mention}
<b>User First Name</b> - {message.from_user.first_name}
<b>User Last Name</b> - {message.from_user.last_name}
<b>User id</b> - `{message.chat.id}`
<b>Unmuted Group</b> - {Config.Group3_name}"""
)
        except Exception:
            pass
    else:
        await message.reply_text(text=f"""Oh come on {message.from_user.mention}! You have still not added our group tag in your name!😡 So you are still muted😝

If you want to <b>get unmuted</b> please follow the instructions below!👇:-

1. Put `{Config.Tag_Name}`(Tap to copy) in your name.
2. After setting the tag send the unmute command of the group you have been muted!

- send /{Config.unmute_command_1} if you have been muted in {Config.Group1_name}
- send /{Config.unmute_command_2} if you have been muted in {Config.Group2_name}
- send /{Config.unmute_command_3} if you have been muted in {Config.Group3_name}

If you do all the things correctly you will get unmuted instantly!""",  reply_to_message_id=chat_id)
