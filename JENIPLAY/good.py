with open("text.txt", "r", encoding = "utf=8") as file:
    data=file.readlines()#считавание всю инфу с файла
    #print(data)
    ahkhcx=9
    for lain in data:#нере
        data2=lain.split(" ")#
        if int(data2[2])>ahkhcx:
            print(data2)

        