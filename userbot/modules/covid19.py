# Copyright (C) 2019 The Raphielscape Company LLC.
# Copyright (C) 2020 TeamDerUntergang.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# @NaytSeyd tarafından portlanmıştır.

from userbot import CMD_HELP, bot
from userbot.events import register
from urllib3 import PoolManager
from json import loads as jsloads


@register(outgoing=True, pattern="^.covid$")
async def covid(event):
    try:
        url = 'http://67.158.54.51/corona.php'
        http = PoolManager()
        request = http.request('GET', url)
        result = jsloads(request.data.decode('utf-8'))
        http.clear()
    except:
        await event.edit("`Bir hata oluştu.`")
        return

    sonuclar = ("** Koronavirüs Verileri **\n" +
                "\n**Dünya geneli**\n" +
                f"**🌎 Vaka Sayısı:** `{result['tum']}`\n" +
                f"**🌎 Vefat Sayısı:** `{result['tumolum']}`\n" +
                f"**🌎 İyileşen Sayısı:** `{result['tumk']}`\n" +
                "\n**Türkiye**\n" +
                f"**🇹🇷 Vaka (toplam):** `{result['trtum']}`\n" +
                f"**🇹🇷 Vaka (bugün):** `{result['trbtum']}`\n" +
                f"**🇹🇷 Vaka (aktif):** `{result['tra']}`\n" +
                f"**🇹🇷 Vefat (toplam):** `{result['trolum']}`\n" +
                f"**🇹🇷 Vefat (bugün):** `{result['trbolum']}`\n" +
                f"**🇹🇷 İyileşen:** `{result['trk']}`")

    await event.edit(sonuclar)


CMD_HELP.update({
    "covid19":
    ".covid \
    \n**Kullanım**: Hem Dünya geneli hem de Türkiye için güncel Covid 19 istatistikleri."
})
