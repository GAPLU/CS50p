def main():
    list = {}
    while True:
        try:
            item = input().upper()
            try:
                list[item] += 1
            except KeyError:
                list[item] = 1
        except EOFError:
            sorted_dict = {key: value for key, value in sorted(list.items())}
            for it in sorted_dict:
                print(list[it], " ", it, sep="")
            break

main()