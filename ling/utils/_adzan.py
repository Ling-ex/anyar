# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/kastaid/getter/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from .aiorequests import Optional, __aiohttpRequests


def fahrenheit(celci: Optional[int]) -> Optional[str]:
    """Convert celcius to farenheit"""
    temperature = (int(celci) * float(1.8)) + 32
    temperat: str = f'{temperature}'
    temp = temperat.split('.')
    return temp[0]


async def __fetch_adzan(
    str_city: Optional[str],
) -> Optional[str]:
    url = f'https://muslimsalat.com/{str_city}.json?key=bd099c5825cbedb9aa934e255a81a5fc'
    response = await __aiohttpRequests(url, re_json=True)
    if not response:
        text = 'Mohon coba lagi.'
        return text
    if response['status_code'] == 0:
        text = f'Tidak bisa mendapatkan Informasi Adzan untuk Wilayah <b>{str_city}</b>, tolong periksa kembali.'
    else:
        timefor = f"""
<b>{response['query']}, {response['country']}, {response['items'][0]['date_for']}.</b>
"""
        cordinates = f"{response['latitude'] or ''},{response['longitude'] or ''}"
        map = f'https://www.google.com/maps?q={cordinates}'
        celci = (
            f"{response['today_weather']['temperature']}"
            if response['today_weather']['temperature']
            else 0
        )
        temperature = (
            'N/A'
            if celci == 0
            else f'{str(celci)}°C | {str(fahrenheit(celci))}°F'
        )
        text = f"""
<b>Waktuh Ibadah Umat Muslim</b>
{timefor}├ <b>Fajr :</b> <code>{response['items'][0]['fajr']}</code>
├ <b>Shuruq :</b> <code>{response['items'][0]['shurooq']}</code>
├ <b>Dzuhur :</b> <code>{response['items'][0]['dhuhr']}</code>
├ <b>Ashar :</b> <code>{response['items'][0]['asr']}</code>
├ <b>Maghrib :</b> <code>{response['items'][0]['maghrib']}</code>
└ <b>Isha :</b> <code>{response['items'][0]['isha']}</code>

<b>Additional</b>
├ <b>Code Country :</b> <code>{response['country_code']}</code>
├ <b>Temperature :</b> <code>{temperature}</code>
├ <b>Cordinates :</b> <code>{cordinates}</code>
└ <b>Map :</b> <code>{map}</code>
"""

    return text
