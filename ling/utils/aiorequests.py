"""
Thia file is part of KASTA ID
"""
# Copyright (C) 2022 Unknown <https://github.com/unknownkz/universe>
# All Rights Reserved
#
# Credits : @unknownkz (axel)
# This file is a part of < https://github.com/kastaid/getter/ >
# PLease read the GNU Affero General Public License in;
# < https://www.github.com/unknownkz/universe/main/LICENSE/ >

from typing import Optional, Set, Any
from sys import version_info
from ling import ClientSession 


aiover=ClientSession

async def __aiohttpRequests(
    url: Optional[str],
    post: Optional[bool] = None,
    headers: Optional[dict] = None,
    params: Optional[dict] = None,
    json: Optional[dict] = None,
    data: Optional[dict] = None,
    ssl: Any = None,
    re_json: Optional[bool] = False,
    re_content: Optional[bool] = False,
    real: Optional[bool] = False,
    statuses: Optional[Set[int]] = None,
    *args,
    **kwargs,
) -> Any:
    """Credits : KASTA ID"""
    statuses = statuses or {}
    if not headers:
        headers = {
            'User-Agent': 'Python/{0[0]}.{0[1]} aiohttp/{1} rams/'.format(
                version_info,
                aiover,
            )
        }
    async with ClientSession(headers=headers) as session:
        try:
            if post:
                resp = await session.post(
                    url=url,
                    json=json,
                    data=data,
                    ssl=ssl,
                    raise_for_status=False,
                    *args,
                    **kwargs,
                )
            else:
                resp = await session.get(
                    url=url,
                    params=params,
                    ssl=ssl,
                    raise_for_status=False,
                    *args,
                    **kwargs,
                )
        except BaseException:
            return None
        if resp.status not in {*{200, 201}, *statuses}:
            return None
        if re_json:
            return await resp.json(content_type=None)
        if re_content:
            return await resp.read()
        return resp if real else await resp.text()
