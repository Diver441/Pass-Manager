### Password manager
Overview

This project is a command-line password manager application that allows users to manage their password storage securely. It supports user registration, login, creating and managing password storage, and generating secure passwords.

The application is designed with an administrative functionality that includes user management capabilities.
Requirements

    Python 3.x
    Pass_gen_man module

Setup and Installation

    Ensure you have Python 3.x installed on your machine.
    Install the Pass_gen_man module.
        If the module is not available via pip, make sure it's accessible in your project directory or installed through other means.
    Save the main script (password_manager.py) and run it.

How to Use
Main Menu

When you start the application, you'll be presented with the main menu:


------------------------------
'Main Menu'
'1 --> Login' 
'2 --> Register' 

'0 --> Exit'



    Login: Log in as an existing user.
    Register: Register a new user.
    Exit: Exit the application.

Login and Registration
Login

    Choose to login as either an Admin or a User.
    Upon successful login, you will be directed to the main menu or an admin-specific menu.

Register

    Choose to register as either an Admin or a User.
    Follow the prompts to complete registration.

Main Menu (After Login)

After logging in, you'll see:

'

Main Menu: 
1 --> Add/Create a Password storage (1 item at a time) 
2 --> Goto my storage 
3 --> Delete my storage 

0 --> Log out and goto Startscreen

'

    Add/Create a Password Storage: Create a new storage item.
    Goto My Storage: Manage your existing storage items.
    Delete My Storage: Delete all your stored items.
    Log Out: Log out and return to the start screen.

Storage Menu

When managing storage:


'
----------------------------------------------
 [User], here are your storage options:
1 --> Show my storage
2 --> Edit item
3 --> Delete Item

0 --> Goto Main Menu
'

    Show My Storage: Display all stored items.
    Edit Item: Edit a specific stored item.
    Delete Item: Delete a specific stored item.
    Go to Main Menu: Return to the main menu.

Creating a Password Item

    Enter a name for the storage item.
    Provide a login or other relevant information.
    Choose to generate or manually enter a password.
    Confirm and save the item.

Password Generation

If choosing to generate a password:

    Enter the desired length (6-32 characters).
    Confirm the generated password or generate a new one.

Administration Features (Admin Only)

Admins can ban or unban users. The functionality is designed but not implemented in this script.
Functions Overview
Main Functions

    start_screen(): Display the main menu and handle navigation.
    log_in(): Handle user login.
    register_user(): Handle user registration.
    main_menu(): Display the main menu after login.
    stor_menu(): Display storage management options.
    create_pass_item(): Create a new password storage item.
    generate_pass(): Generate a secure password.
    enter_pass(): Manually enter a password.
    save_item(): Save the created storage item.
    show_item_list(): Show all stored items.
    edit_item(): Edit a stored item.
    delete_item(): Delete a stored item.
    perform_check(): Check for duplicate entries.
    exit_me(): Exit the application.
    log_out(): Log out and return to the start screen.

Utility Functions

    input_me(command): Handle user input and command execution.
    del_my_storage(): Delete all user storage.
    save_pass(): Placeholder for saving password generation.
    ban_user(): Placeholder for banning a user.
    unban_user(): Placeholder for unbanning a user.

Main Execution

    main(): Entry point of the application. Displays greeting and starts the main menu.

Note:
It is not finished!

Enjoy managing your passwords securely!
