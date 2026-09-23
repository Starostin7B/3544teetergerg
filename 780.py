n = int(input())

for _ in range(n):
    name, s, status = input().split()
    try:
        s = float(s)
        if s < 100:
            c = "дрібнота"
        elif s < 1000:
            c = "середнячок"
        else:
            c = "великий клієнт"
        if status == "clean":
            result = "працювати без питань"
        elif status == "suspicious":
            result = "перевірити документи"
        elif status == "fraud":
            result = "чорний список"
        else:
            result = "невідомий статус"
        print(name, c, result)
    except ValueError:
        print("фальшиві дані")