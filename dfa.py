def main():
    print("DFA Simulator")
    alphabet = input('Enter the alphabet you want to use: ')
    states = int(input('How many states do you want to have? (from 0 to n): '))
    
    initial_state = get_valid_state_input(
        f"Type the initial state (between 0 and {states}): ", states)

    final_state = get_valid_state_input(
        f"Type the final state (between 0 and {states}): ", states)

    transition_table = get_transition_table(states, alphabet)

    display_transition_table(transition_table)
    test_word(alphabet, transition_table, initial_state, final_state)


def test_word(alphabet, transition_table, initial_state, final_state):
    word = input('Type a word using your alphabet ({}).\n (Type exit to exit the program) '.format(alphabet))

    if word == 'exit':
        return

    state = initial_state

    for letter in word:
        if letter not in alphabet:
            print("The word contains invalid symbols. Please try again.")
            test_word(alphabet, transition_table, initial_state, final_state)
            return 

        next_state = transition_table[state][letter]
        state = next_state

    if state == final_state:
        print('ACCEPTED')
        test_word(alphabet, transition_table, initial_state, final_state)
    else:
        print('REJECTED')
        test_word(alphabet, transition_table, initial_state, final_state)


def get_valid_state_input(prompt, max_state):
    while True:
        try:
            state = int(input(prompt))
            if 0 <= state <= max_state:
                return state
            else:
                print(
                    f"State must be between 0 and {max_state}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_transition_table(states, alphabet):
    transition_table = {}
    for state in range(states + 1):
        state_transitions = {}
        for symbol in alphabet:
            while True:
                try:
                    action = int(
                        input(f"State: {state}, Symbol: {symbol}, Enter next state: "))
                    if 0 <= action < states + 1:
                        state_transitions[symbol] = action
                        break
                    else:
                        print(
                            f"Action must be between 0 and {states}. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
        transition_table[state] = state_transitions
    return transition_table

def display_transition_table(transition_table):
    print("\nTransition Table:")
    print("{Symbol: action, Symbol: action}")
    for state, transitions in transition_table.items():
        print(f"State {state}: {transitions}")

if __name__ == "__main__":
    main()