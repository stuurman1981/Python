import asyncio
import aiohttp
import json

async def request_data(url):
    # use aiohttp.request (as a context manager) to get data from url
    # then return data as str
    async with aiohttp.request('GET', url) as resp:
        return await resp.text()


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
    parsed_json = json.loads(await request_data(pattern))
    top_posts = {}
    posts = {}
    for post in parsed_json['data']['children']:
        post_title = post['data']['title']
        post_score = post['data']['score']
        post_link = f"https://www.reddit.com{post['data']['permalink']}"

        posts[post_title] = {'score': post_score, 'link': post_link}

    top_posts[subreddit] = posts
    return top_posts


async def main():
    # use asyncio.gather to get tops for reddits "python", "compsci", "microbork"
    # try to use *args instead of hardcoded function calls
    reddits = {
        "python",
        "compsci",
        "microbork"
    }
    return await asyncio.gather(*(get_reddit_top(r) for r in reddits))


asyncio.run(main())
