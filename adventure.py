game_state = {
    "current_room": "start_room",
    "inventory": [],
    "failed_door_attempts": 0,
    "rooms": {
        "start_room": {
            "description": "You wake up in a mysterious room. There's a door in front of you and a window to your left.",
            "choices": {
                "open door": {
                    "condition": lambda state: "key" in state["inventory"],
                    "room_if_true": "unlocked_door_room",
                    "room_if_false": "locked_door"
                },
                "look window": "window_view"
            }
        },
        "locked_door": {
            "description": "The door is locked. You need a key.",
            "on_enter": lambda state: state.update({"failed_door_attempts": state["failed_door_attempts"] + 1}),
            "choices": {
                "back": "start_room"
                # Potential: Add another choice here that could lead to a different outcome or hint
            }
        },
        "window_view": {
            "description": "You look out the window. It's dark outside and you see a faint light in the distance. You also spot a small, shiny object on the window sill.",
            "choices": {
                "take object": "get_key",
                "back": "start_room"
            }
        },
        "get_key": {
            "description": "You found a key!",
            "on_enter": lambda state: state["inventory"].append("key") if "key" not in state["inventory"] else None,
            "choices": {
                "back": "start_room"
            }
        },
        "unlocked_door_room": { # WIN CONDITION
            "description": "You use the key and the door creaks open. You've escaped the room! Congratulations!",
            "is_terminal": True # Indicates game ends here
        },
        "lose_room": { # LOSE CONDITION
            "description": "You jiggled the door handle too many times. The lock is now completely jammed! You're stuck.",
            "is_terminal": True # Indicates game ends here
        },
        "quit_game": { # A dummy room to signify quitting via command
            "description": "Game ended by player.",
            "is_terminal": True
        }
    }
}

def display_current_room(state):
    """Displays the current room description and choices."""
    room_data = state["rooms"].get(state["current_room"])
    if not room_data or room_data.get("is_terminal", False) and state["current_room"] != "unlocked_door_room" and state["current_room"] != "lose_room" : # Don't display if game has ended, unless it's the win/lose message itself
        if state["current_room"] == "quit_game": # Specific message for quit command
             print(state["rooms"]["quit_game"]["description"])
        return

    print(room_data["description"])

    if room_data.get("is_terminal", False): # No choices if it's a terminal state (win/lose)
        return

    print("What do you do? (type one of the following options):")
    # Corrected: room_data instead of room
    for choice_text in room_data.get("choices", {}):
        print(f"- {choice_text}")

def handle_action(state, action):
    """Handles the player's action and updates the game state."""
    current_room_data = state["rooms"].get(state["current_room"])
    # Game ends if current room is terminal, so no actions handled.
    if not current_room_data or current_room_data.get("is_terminal", False):
        return

    if action == "quit": # Centralize quit action
        state["current_room"] = "quit_game"
        # display_current_room will print the quit_game message, and start_game loop will terminate.
        return

    if action in current_room_data.get("choices", {}):
        choice_outcome = current_room_data["choices"][action]
        next_room_name = ""

        if isinstance(choice_outcome, str): # Simple transition
            next_room_name = choice_outcome
        elif isinstance(choice_outcome, dict) and "condition" in choice_outcome: # Conditional transition
            if choice_outcome["condition"](state):
                next_room_name = choice_outcome["room_if_true"]
            else:
                next_room_name = choice_outcome["room_if_false"]
        else:
            print("Error: Choice outcome configured incorrectly.")
            return # Avoid further processing on bad config

        state["current_room"] = next_room_name

        new_room_data_on_enter = state["rooms"].get(state["current_room"])
        if new_room_data_on_enter and "on_enter" in new_room_data_on_enter:
            new_room_data_on_enter["on_enter"](state) # Execute on_enter for the new room

        # Check for lose condition specifically after trying to open door and failing
        if state["current_room"] == "locked_door" and state["failed_door_attempts"] >= 2:
            state["current_room"] = "lose_room"
            # The display_current_room called in the main loop will show the lose message.
            # And the main loop will terminate as lose_room is terminal.

    else:
        print(f"Invalid action: '{action}'. Try one of the listed options.")


def start_game():
    """Starts the adventure game."""
    print("Welcome to the Adventure Game!")
    global game_state

    # Reset game state for a fresh run
    game_state["current_room"] = "start_room"
    game_state["inventory"] = []
    game_state["failed_door_attempts"] = 0

    # --- Test Scenarios ---
    # Win:
    # commands = ["look window", "take object", "back", "open door"]
    # Lose by too many attempts:
    # commands = ["open door", "back", "open door"] # Should trigger lose_room
    # Quit command test:
    commands = ["look window", "quit"]

    command_index = 0

    while True:
        current_room_details = game_state["rooms"].get(game_state["current_room"])
        display_current_room(game_state) # Display current state first

        if current_room_details and current_room_details.get("is_terminal", False):
            # Message for terminal states like quit_game is handled by display_current_room if needed
            # or the description of win/lose room is the final message.
            break # Exit loop if current room is terminal (win, lose, quit)

        if command_index >= len(commands):
            print("\nRan out of automated commands. The story ends here for now.")
            break

        action = commands[command_index]
        print(f"\nAction: {action}") # Print action being taken
        command_index += 1

        handle_action(game_state, action)

        # Separator, but not after the very last action if it leads to a terminal state
        if not (game_state["rooms"].get(game_state["current_room"]) and \
                game_state["rooms"].get(game_state["current_room"]).get("is_terminal", False)):
            print("-" * 20)


if __name__ == "__main__":
    start_game()
