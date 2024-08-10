import random

def draw_card():
    """Simulate drawing a card from a deck (values 1-11, where Ace is 11)."""
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11])  # 10 represents 10, J, Q, K, 11 represents Ace

def calculate_score(hand):
    """Calculate the score for a given hand."""
    score = sum(hand)
    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)  # Ace counts as 1 instead of 11 if over 21
        score = sum(hand)
    return score

def play_game():
    user_hand = [draw_card(), draw_card()]
    computer_hand = [draw_card(), draw_card()]

    print(f"User's cards: {user_hand}, score: {calculate_score(user_hand)}")
    print(f"Computer's cards: {computer_hand[0]}")

    # Ask the user if they want another card
    while calculate_score(user_hand) < 21:
        another_card = input("Do you want another card? (yes/no): ").lower()
        if another_card == 'yes':
            user_hand.append(draw_card())
            print(f"User's cards: {user_hand}, score: {calculate_score(user_hand)}")
        else:
            break

    # Computer's turn: draw cards until the score is at least 17
    while calculate_score(computer_hand) < 17:
        computer_hand.append(draw_card())
        print(f"Computer's cards: {computer_hand}, score: {calculate_score(computer_hand)}")

    # Final Scores
    user_score = calculate_score(user_hand)
    computer_score = calculate_score(computer_hand)

    print(f"Final User's cards: {user_hand}, score: {user_score}")
    print(f"Final Computer's cards: {computer_hand}, score: {computer_score}")

    # Determine the outcome
    if user_score > 21:
        print("User busts! Computer wins.")
    elif computer_score > 21:
        print("Computer busts! User wins.")
    elif user_score > computer_score:
        print("User wins!")
    elif user_score < computer_score:
        print("Computer wins!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()