import requests

url = "http://nbwk.online/api/index.php?act=cd"
phone = "19914282289"

# 测试不同的参数名
param_names = ["userName", "username", "user", "phone", "mobile", "tel", "account", "userid", "id"]

for name in param_names:
    print(f"\n=== 测试参数名: {name} ===")
    data = {name: phone}
    resp = requests.post(url, data=data, timeout=30)
    print(f"Status: {resp.status_code}")
    result = resp.json()
    print(f"Response: {result}")
    if result.get("code") == 1:
        print(f"✅ 找到正确的参数名: {name}")
        break
