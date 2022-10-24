while True:
    n = float(input('整数値を入力してください -> '))
    if n % 1 == 0:
        if n >= 0:
            print("あなたは普通の人")

        else:
            print("あなたは理系")

    else:
        print("あなたは指示も聞けないお馬鹿さん")
