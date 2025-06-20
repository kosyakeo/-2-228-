strs = [
  "https://youtube.com",
  "https://google.com",
  "https://www.apple.com",
  "http://yandex.ru",
  "http://discord.com"
]
res = []
for i in strs:
    if i.startswith("http://"):
      res.append(i)
print(res)
