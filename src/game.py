import random

# Function to assign values to each card in the deck
def cardValue(card):
    if card == "A":  # Ace is worth 1
        return 1
    elif card in ["J", "Q", "K"]:  # Face cards are worth 10
        return 10
    else:  # All other cards are worth their numeric value
        return int(card)

# Function to randomly select a card from the deck
def dealCard():
    card = random.choice(["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])
    return card

# Function to calculate the total value of a player's hand
def calculateHand(hand):
    total = 0
    for card in hand:  # Add the value of each card in the hand
        total += cardValue(card)
    
    # Adjust for Aces: if total is 11 or less, Ace can be worth 11
    for card in hand:
        if card == "A" and total <= 11:
            total += 10
    
    return total

# Function to display the player's hand and its total value
def displayHand(playerName, hand, total):
    handStr = ", ".join(hand)  # Create a string of the cards in the hand
    print(playerName + " hand: " + handStr + " | Total: " + str(total))

# Function to run the game
def playGame():
    # Deal two cards each to the player and dealer
    playerHand = [dealCard(), dealCard()]
    dealerHand = [dealCard(), dealCard()]

    while True:
        # Calculate and display the player's hand total
        playerTotal = calculateHand(playerHand)
        displayHand("Player", playerHand, playerTotal)

        # Check if the player busts (goes over 21)
        if playerTotal > 21:
            print("Player busts! Dealer wins!")
            return  # End the game if the player busts

        # Ask the player whether they want to 'Hit' or 'Stay'
        move = input("Do you want to 'Hit' or 'Stay'? ").lower()
        if move == 'hit':
            playerHand.append(dealCard())  # Give the player another card
        elif move == 'stay':
            break  # End the player's turn if they choose to stay
        else:
            print("Invalid input. Please choose 'Hit' or 'Stay'.")

    # Dealer's turn: they must draw cards until they reach 16 or more
    dealerTotal = calculateHand(dealerHand)
    while dealerTotal < 16:
        dealerHand.append(dealCard())  # Dealer draws another card
        dealerTotal = calculateHand(dealerHand)

    # Display the dealer's final hand
    displayHand("Dealer", dealerHand, dealerTotal)

    # Determine the winner based on the totals
    if dealerTotal > 21:
        print("Dealer busts! Player wins!")  # Dealer busts if their total is over 21
    elif dealerTotal > playerTotal:
        print("Dealer wins!")  # Dealer wins if their total is higher
    elif dealerTotal < playerTotal:
        print("Player wins!")  # Player wins if their total is higher
    else:
        print("It's a tie!")  # It's a tie if both have the same total

# Start the game
playGame()
