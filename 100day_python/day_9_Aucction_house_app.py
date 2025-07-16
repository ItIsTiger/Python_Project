def auction_house():
    print("Welcome to the Auction House!")
    bill_person = {}
    continue_auction = True
    highest_bid = 0
    highest_bidder = ""
    while continue_auction:
        print("\n"*50)  # Clear the screen
        name = input("Enter your name: ")
        bid = float(input("Enter your bid amount: $"))
        bill_person[name] = bid
        
        another_bid = input("Is there another bidder? (yes/no): ").strip().lower()
        if another_bid != 'yes':
            continue_auction = False
    print("\n"*50)  # Clear the screen   


    #Highet bidder logic
    # for key in bill_person:
    #     print(f"{key}: ${bill_person[key]}")
    #     if bill_person[key] > highest_bid:
    #         highest_bid = bill_person[key]
    #         highest_bidder = key
    
    # print(f"\nThe highest bidder is {highest_bidder} with a bid of ${highest_bid}!")
    # #Highet bidder logic
    # print("\nThank you for participating in the auction!")

    highest_bidder = max(bill_person, key=bill_person.get)
    highest_bid = bill_person[highest_bidder]
    print(f"\nThe highest bidder is {highest_bidder} with a bid of ${highest_bid:.2f}.")


auction_house()

