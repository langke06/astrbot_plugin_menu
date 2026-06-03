# 测试解码
remarks1 = "ãä½ç­è®°å½ï¼41/41ï¼ç­é¢å®æ¯ï¼è¯·åå¾æäº¤ã"
remarks2 = " |  |æ£æµæ¶é´:2026-05-17 09:26:17,ææ èè¯"

# 方式1: 直接解码（假设是utf-8编码的字符串被错误显示了）
print("=== 方式1: 直接编码再解码 ===")
try:
    decoded = remarks1.encode('latin1').decode('utf-8')
    print(f"Decoded: {decoded}")
except Exception as e:
    print(f"Error: {e}")

# 方式2: 使用 unicode_escape
print("\n=== 方式2: unicode_escape ===")
try:
    decoded = remarks1.encode('utf-8').decode('unicode_escape')
    print(f"Decoded: {decoded}")
except Exception as e:
    print(f"Error: {e}")

# 方式3: 原始字符串测试
print("\n=== 测试原始字符串 ===")
raw = "〖作答记录：41/41；答题完毕，请前往提交〗"
print(f"Original: {raw}")
print(f"Encoded: {raw.encode('utf-8')}")
