import asyncio
import aiohttp
import json

async def request_data(url):
    # use aiohttp.request (as a context manager) to get data from url
    # then return data as str
    async with aiohttp.request('GET', url) as resp:
        data = await resp.text()
        return data


async def get_reddit_top(subreddit):
    # use request_data coroutine to get reddit top
    # url pattern - f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5'
    # then unpack data to json:
    # %reddit_name%: {
    #     %post_title%: {
    #         %score%: int,
    #         %link%: str
    #     },
    #     %post_title%: {
    #         %score%: int,
    #         %link%: str
    #     }
    # }
    pattern = f'https://www.reddit.com/r/{subreddit}/top.json?sort=top&t=day&limit=5'
    parsed_json = json.dumps(request_data(pattern))


async def main():
    # use asyncio.gather to get tops for reddits "python", "compsci", "microbork"
    # try to use *args instead of hardcoded function calls
    reddits = {
        "python",
        "compsci",
        "microbork"
    }
    res = await asyncio.gather(*(get_reddit_top(r) for r in reddits))


asyncio.run(main())