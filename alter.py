import json
def change(a, b):
    f1 = open("j/" + str(a) + ".json", "w", encoding="utf-8")
    falter = open("j.b/" + str(b) + ".json", "r", encoding="utf-8")
    js = json.load(falter)
    json.dump(js, f1, ensure_ascii=False)

for i in range(1307, 1361):
    change(i, i - 1)

for i in range(1364, 1455):
    change(i, i - 3)

change(1306,1452)
change(1362,1453)
change(1363,1454)
