import requests

url = "http://nbwk.online/api/index.php?act=cd"
phone = "19914282289"

print("=== 使用 requests 测试 ===")

# 方式1: form-data
data = {"userName": phone}
resp = requests.post(url, data=data, timeout=30)
print(f"Status: {resp.status_code}")
print(f"Response: {resp.text[:500]}")

print("\n=== 查看请求头 ===")
print(f"Request headers: {resp.request.headers}")
print(f"Request body: {resp.request.body}")
