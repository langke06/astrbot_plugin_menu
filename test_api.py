import aiohttp
import asyncio

async def test_api():
    url = "http://nbwk.online/api/index.php?act=cd"
    phone = "19914282289"
    
    # 测试不同的提交方式
    
    # 方式1: 普通字典 (aiohttp 会自动编码为 form-data)
    print("=== 方式1: 普通字典 ===")
    async with aiohttp.ClientSession() as session:
        data = {"userName": phone}
        async with session.post(url, data=data) as resp:
            print(f"Status: {resp.status}")
            print(f"Content-Type: {resp.headers.get('content-type')}")
            text = await resp.text()
            print(f"Response: {text[:500]}")
    
    print("\n=== 方式2: 手动编码为 x-www-form-urlencoded ===")
    async with aiohttp.ClientSession() as session:
        from urllib.parse import urlencode
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = urlencode({"userName": phone})
        async with session.post(url, data=data, headers=headers) as resp:
            print(f"Status: {resp.status}")
            print(f"Content-Type: {resp.headers.get('content-type')}")
            text = await resp.text()
            print(f"Response: {text[:500]}")
    
    print("\n=== 方式3: 使用 params 传递参数 ===")
    async with aiohttp.ClientSession() as session:
        params = {"act": "cd", "userName": phone}
        base_url = "http://nbwk.online/api/index.php"
        async with session.post(base_url, params=params) as resp:
            print(f"Status: {resp.status}")
            print(f"Content-Type: {resp.headers.get('content-type')}")
            text = await resp.text()
            print(f"Response: {text[:500]}")
    
    print("\n=== 方式4: 使用 FormData (multipart/form-data) ===")
    async with aiohttp.ClientSession() as session:
        form = aiohttp.FormData()
        form.add_field("userName", phone)
        async with session.post(url, data=form) as resp:
            print(f"Status: {resp.status}")
            print(f"Content-Type: {resp.headers.get('content-type')}")
            text = await resp.text()
            print(f"Response: {text[:500]}")

if __name__ == "__main__":
    asyncio.run(test_api())
