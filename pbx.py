import os
import base64
import ipaddress
import random
import struct
from random import randint

try:
    from pyrogram import Client as PClient
except:
    os.system("pip install pyrogram")
    from pyrogram import Client as PClient

try:
    from telethon.sessions import StringSession
    from telethon.sessions.string import (_STRUCT_PREFORMAT, CURRENT_VERSION,
                                          StringSession)
    from telethon.sync import TelegramClient
except:
    os.system("pip install telethon")
    from telethon.sessions import StringSession
    from telethon.sessions.string import (_STRUCT_PREFORMAT, CURRENT_VERSION,
                                          StringSession)
    from telethon.sync import TelegramClient


def main():
    print("T E A M    P B X    ! !")
    print("Hello!! Welcome to  Session Generator\n")
    print("Human Verification Required !!")
    while True:
        verify = int(randint(1, 50))
        okvai = int(input(f"Enter {verify} to continue: "))
        if okvai == verify:
            print("\nChoose the string session type: \n1. Pbxbot \n2. Telethon \n3. Pyrogram ")
            while True:
                library = input("\nYour Choice: ")
                if library == "1":
                    generate_hellbot_session()
                    break
                elif library == "2":
                    generate_telethon_session()
                    break
                elif library == "3":
                    generate_pyro_session()
                    break
                else:
                    print("Please enter integer values (1/2/3/ only).")
            break
        else:
            print("Verification Failed! Try Again:")


def generate_hellbot_session():
    print("!!! PbxBOT SESSION !!!")
    print("One session for all PbxBot's Project.")
    api_id = int(input("\nEnter APP ID here: "))
    api_hash = input("\nEnter API_HASH here: ")
    with PClient(name="helluser", api_id=api_id, api_hash=api_hash, in_memory=True) as hell:
        print("\nYour PBXBOT SESSION is saved in your telegram saved messages.")
        _session = hell.export_session_string()
        hell_session = hellbot_session(_session)
        hell.send_message(
            "me",
            f"#PBXBOT_SESSION \n\n`{hell_session}`",
        )


def generate_pyro_session():
    print("Pyrogram Session for Music Bot!")
    APP_ID = int(input("\nEnter APP ID here: "))
    API_HASH = input("\nEnter API HASH here: ")
    with PClient(name="helluser", api_id=APP_ID, api_hash=API_HASH, in_memory=True) as hellbot:
        print("\nYour PBXBot Session Is sent in your Telegram Saved Messages.")
        hellbot.send_message(
            "me",
            f"#PYBOT #PYROGRAM\n\n`{hellbot.export_session_string()}`",
        )


def generate_telethon_session():
    print("\nTelethon Session For telethoneBot!")
    APP_ID = int(input("\nEnter APP ID here: "))
    API_HASH = input("\nEnter API HASH here: ")
    with TelegramClient(StringSession(), APP_ID, API_HASH) as hellbot:
        print("\nYour telethoneBot Session Is sent in your Telegram Saved Messages.")
        hellbot.send_message(
            "me",
            f"#TELETHONBOT #TELETHON \n\n`{hellbot.session.save()}`",
        )



def hellbot(text):
    res = ''.join(
        map(
            random.choice,
            zip(text.lower(), text.upper()),
        )
    )
    return res.strip()


def hellbot_session(session):
    pyro_format = {
        351: ">B?256sI?",
        356: ">B?256sQ?",
        362: ">BI?256sQ?",
    }

    ipv4_dc = {
        1: "149.154.175.53",
        2: "149.154.167.51",
        3: "149.154.175.100",
        4: "149.154.167.91",
        5: "91.108.56.130",
    }

    error_msg = "Error in generating session! Report it in @ll_BAD_MUNDA_ll Chats"

    # converting pyrogram session
    if len(session) in pyro_format.keys():
        if len(session) in [351, 356]:
            dc_id, _, auth_key, _, _ = struct.unpack(
                pyro_format[len(session)],
                base64.urlsafe_b64decode(session + "=" * (-len(session) % 4)),
            )
        else:
            dc_id, _, _, auth_key, _, _ = struct.unpack(
                pyro_format[len(session)],
                base64.urlsafe_b64decode(session + "=" * (-len(session) % 4)),
            )

        # https://github.com/badmunda98/Telethon/blob/v1/telethon/sessions/string.py
        new_session = CURRENT_VERSION + StringSession.encode(
            struct.pack(
                _STRUCT_PREFORMAT.format(4),
                dc_id,
                ipaddress.ip_address(ipv4_dc[dc_id]).packed,
                443,
                auth_key
            )
        )
        return f"=={hellbot('hell')}{new_session}{hellbot('bot')}=="
    else:
        return error_msg


main()

    
