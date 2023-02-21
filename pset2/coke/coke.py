def main():
    due = int(50)
    while(True):
        if due <= 0:
            print("Change Owed:", -due)
            break
        print("Amount Due:", due)
        insert = int(input("Insert Coin: "))
        if insert == 25 or insert == 10 or insert == 5:
            due -= insert

if __name__ == "__main__":
    main()