seasons = {"春": [1, 2, 3],  "夏": [4, 5, 6], "秋": [7, 8, 9], "冬": [10, 11, 12]}
min_month = min(min(seasons.values()))
max_month = max(max(seasons.values()))

while True:
    try:
        month = int(input("月を入力して:"))
        if month < min_month or max_month < month:
            print("入力方法が違います。もう一度入力してください")
            continue
        for key in seasons.keys():
            if month in seasons[key]:
                print(key)
                break
    except ValueError:
        print("整数を入力してください！！！")
