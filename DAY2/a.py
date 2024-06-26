def start_repl():
    banner = "Welcome to the Python REPL. Type 'exit()' to quit."
    exit_commands = ('exit()', 'quit()')
    
    print(banner)
    while True:
        try:
            user_input = input(">>> ")
            if user_input in exit_commands:
                print("Exiting REPL. Goodbye!")
                break
            
            # Use exec for more complex statements
            exec(user_input)
        except Exception as e:
            print(f"Error: {e}")

# Start the REPL
start_repl()
