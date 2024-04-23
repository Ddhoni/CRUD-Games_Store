# Importing a Library
import tkinter as tk 
from tkinter import ttk, messagebox, simpledialog

# Nested List of Dictionaries
game_list = [
    { 
        "ps4": [
            {"name": "God of War", "price": 49.99, "stock": 10},
            {"name": "The Last of Us Remastered", "price": 39.99, "stock": 15},
            {"name": "Bloodborne", "price": 44.99, "stock": 20}
        ]
    },
    {
        "ps5": [
            {"name": "Demon's Souls", "price": 69.99, "stock": 12},
            {"name": "Spider-Man: Miles Morales", "price": 59.99, "stock": 8},
            {"name": "Astro's Playroom", "price": 19.99, "stock": 25}
        ]
    },
    {
        "nintendo_switch": [
            {"name": "The Legend of Zelda: Breath of the Wild", "price": 59.99, "stock": 18},
            {"name": "Animal Crossing: New Horizons", "price": 49.99, "stock": 20},
            {"name": "Mario Kart 8 Deluxe", "price": 59.99, "stock": 15}
        ]
    },
    {
        "pc": [
            {"name": "The Witcher 3: Wild Hunt", "price": 29.99, "stock": 30},
            {"name": "Cyberpunk 2077", "price": 59.99, "stock": 25},
            {"name": "Half-Life: Alyx", "price": 39.99, "stock": 20}
        ]
    },
    {
        "xbox_one": [
            {"name": "Halo: The Master Chief Collection", "price": 39.99, "stock": 10},
            {"name": "Forza Horizon 4", "price": 49.99, "stock": 15},
            {"name": "Gears 5", "price": 59.99, "stock": 20}
        ]
    },
    {
        "xbox_x": [
            {"name": "Assassin's Creed Valhalla", "price": 59.99, "stock": 12},
            {"name": "Watch Dogs: Legion", "price": 49.99, "stock": 18},
            {"name": "Call of Duty: Black Ops Cold War", "price": 69.99, "stock": 15}
        ]
    },
    {
        "xbox_s": [
            {"name": "Yakuza: Like a Dragon", "price": 49.99, "stock": 20},
            {"name": "Dirt 5", "price": 39.99, "stock": 25},
            {"name": "Minecraft Dungeons", "price": 29.99, "stock": 30}
        ]
    }
]


# CRUD Function

def display_console_list(): 
    consoles = set() # Create an empty set to store the names of game consoles
    for console in game_list: # Iterate through each game in the game_list
        consoles.update(console.keys()) # Update the consoles set with the key (console name) of each game

    console_list.delete(0, tk.END) # Delete the contents of the previous listbox (console_list)
    for console in consoles:  # Iterate through each console name in the consoles set
        console_list.insert(tk.END, console) # Insert the console name into the listbox (console_list)

def display_game_by_console(event=None):
    selected_indices = console_list.curselection() # Get the selected index from listbox console_list
    
    if not selected_indices: # If no console is selected, then no action needs to be taken
        # game_frame and menu_frame will not be hidden if no console is selected
        return
    
    selected_console = console_list.get(selected_indices[0])  # Get the name of the selected console from the console_list listbox
    games = [] #an empty list

    for console in game_list: # Search for games that match the selected console
        for key, value in console.items():
            if key.lower() == selected_console.lower():
                games.extend(value)

    game_tree.delete(*game_tree.get_children())  # Remove all items from the game_tree treeview
    for game in games:  # Display the corresponding game in the game_tree treeview
        game_tree.insert("", tk.END, values=(game["name"], game["price"], game["stock"]))

    if games: # Display the game frame and menu if there are games available, otherwise hide them
        game_frame.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
        menu_frame.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
    else:
        game_frame.grid_forget()
        menu_frame.grid_forget()

def on_game_select(event=None):
    selected_item = game_tree.selection() # Get the selected item from the game_tree treeview

    if selected_item: # If there is a selected item it will display frames containing buttons for buying, adding, editing, and removing games
        buy_frame.grid(row=0, column=1, padx=2, pady=2, sticky=tk.SW)
        add_frame.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W+tk.E)
        edit_frame.grid(row=2, column=0, padx=2, pady=5, sticky=tk.W+tk.E)
        remove_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)
        update_stock_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)
 
    else: # If no item is selected, hide all frames
        buy_frame.grid_forget()
        add_frame.grid_forget()
        edit_frame.grid_forget()
        remove_frame.grid_forget()
        pay_button.grid_forget() # Forgot to hide the pay_button
        update_stock_frame.grid_forget()
        bought_game_frame.grid_forget() # Forgot to hide the bought_game_frame
        
def add_game():
    console_name = console_entry.get().lower()
    game_name = game_name_entry.get().strip()
    game_price = game_price_entry.get().strip()

    # Check if any of the fields are empty
    if not console_name or not game_name or not game_price:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    try:
        game_price = float(game_price)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid price.")
        return

    # Check if the game already exists for the given console
    for console in game_list:
        if console_name in console.keys():
            for game in console[console_name]:
                if game_name.lower() == game["name"].lower():
                    messagebox.showwarning("Warning", "Game already exists.")
                    return
            
            # If the console exists and the game does not, add the game to the console's list of games
            console[console_name].append({"name": game_name.title(), "price": game_price, "stock": 0})
            
            # Show the game frame again
            game_frame.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
            
            # Show the menu frame again
            menu_frame.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
            
            # Don't need to call display_game_by_console() here
            messagebox.showinfo("Success", "Game added successfully!")
            return
    
    # If the console doesn't exist, show an error message
    messagebox.showwarning("Error", "Console not found. Game not added.")

# This function is responsible for editing a game's details.
def edit_game():
    # Retrieve the index of the selected item in the game_tree.
    selected_item = game_tree.selection()[0]
    # Get the name of the game from the selected item in the game_tree.
    game_name = game_tree.item(selected_item)["values"][0]
    
    # Iterate through each console in the game_list.
    for console in game_list:
        # Iterate through the keys (console names) in each console dictionary.
        for key in console:
            # Iterate through each game in the list of games for the current console.
            for game in console[key]:
                # Check if the name of the current game matches the selected game's name.
                if game_name == game["name"]:
                    try:
                        # Get the new name and price of the game from entry fields.
                        new_name = new_game_name_entry.get().title()
                        new_price = float(new_game_price_entry.get())
                        
                        # Update the game's name and price with the new values.
                        game["name"] = new_name
                        game["price"] = new_price
                        
                        # Update the display to reflect the changes.
                        display_game_by_console()
                        # Show a success message.
                        messagebox.showinfo("Success", "Game updated successfully!")
                    except ValueError:
                        # Show a warning message if the entered price is not valid.
                        messagebox.showwarning("Warning", "Please enter a valid price.")
                    return

# This function is responsible for removing a game from the game list.
def remove_game():
    # Retrieve the index of the selected item in the game_tree.
    selected_item = game_tree.selection()[0]
    # Get the name of the game from the selected item in the game_tree.
    game_name = game_tree.item(selected_item)["values"][0]

    # Iterate through each console in the game_list.
    for console in game_list:
        # Iterate through the keys (console names) in each console dictionary.
        for key in console:
            # Iterate through each game in the list of games for the current console.
            for game in console[key]:
                # Check if the name of the current game matches the selected game's name.
                if game_name == game["name"]:
                    # Remove the selected game from the list of games for the current console.
                    console[key].remove(game)
                    # Update the display to reflect the changes.
                    display_game_by_console()
                    # Show a success message.
                    messagebox.showinfo("Success", "Game removed successfully!")
                    return

# This function is responsible for updating the stock of a game.
def update_stock():
    # Retrieve the index of the selected item in the game_tree.
    selected_item = game_tree.selection()[0]
    # Get the name of the game from the selected item in the game_tree.
    game_name = game_tree.item(selected_item)["values"][0]
    
    # Iterate through each console in the game_list.
    for console in game_list:
        # Iterate through the keys (console names) in each console dictionary.
        for key in console:
            # Iterate through each game in the list of games for the current console.
            for game in console[key]:
                # Check if the name of the current game matches the selected game's name.
                if game_name == game["name"]:
                    try:
                        # Get the new stock value of the game from an entry field.
                        new_stock = int(new_stock_entry.get())
                        # Update the game's stock with the new value.
                        game["stock"] = new_stock
                        # Update the display to reflect the changes.
                        display_game_by_console()
                        # Show a success message.
                        messagebox.showinfo("Success", "Stock updated successfully!")
                    except ValueError:
                        # Show a warning message if the entered stock number is not valid.
                        messagebox.showwarning("Warning", "Please enter a valid stock number.")
                    return

# This dictionary is used to keep track of games that have been bought.
bought_games = {}

# Function to display the list of bought games
def display_bought_games():
    # Clear the contents of the bought_game_tree
    bought_game_tree.delete(*bought_game_tree.get_children())
    
    # Initialize total_payment variable to calculate the total payment
    total_payment = 0
    
    # Iterate through each bought game and its information in the bought_games dictionary
    for game_name, info in bought_games.items():
        # Insert the game's information into the bought_game_tree
        bought_game_tree.insert("", tk.END, values=(game_name, info['quantity'], info['price'], info['total_price']))
        # Calculate the total payment by adding the total price of each bought game
        total_payment += info['total_price']
    
    # Display the pay_button for payment
    pay_button.grid(row=2, column=1, padx=2, pady=2, sticky=tk.W+tk.E)

# Function to handle the buying process of games
def buy_game():
    # Get the selected item from the game_tree (the game to be bought)
    selected_item = game_tree.selection()[0]
    game_name = game_tree.item(selected_item)["values"][0]
    
    # Iterate through each console in the game_list to find the selected game
    for console in game_list:
        for key in console:
            for game in console[key]:
                if game_name == game["name"]:
                    try:
                        # Get the quantity of the game to be bought from the entry field
                        quantity = int(buy_quantity_entry.get())
                        # Check if the quantity exceeds the available stock
                        if quantity > game["stock"]:
                            messagebox.showwarning("Warning", "Insufficient stock.")
                            return
                        
                        # Calculate the total price of the bought games
                        total_price = game["price"] * quantity
                        
                        # Reduce the stock of the bought game from the available stock
                        game["stock"] -= quantity
                        
                        # Update the bought_games dictionary with the bought game's information
                        if game_name in bought_games:
                            bought_games[game_name]["quantity"] += quantity
                            bought_games[game_name]["total_price"] += total_price
                        else:
                            bought_games[game_name] = {
                                "quantity": quantity,
                                "total_price": total_price,
                                "price": game["price"]
                            }
                        
                        # Display the frame for bought games and update the display
                        bought_game_frame.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
                        display_bought_games()
                        
                        # Clear the quantity entry field after buying
                        buy_quantity_entry.delete(0, tk.END)
                        
                    except ValueError:
                        messagebox.showwarning("Warning", "Please enter a valid quantity.")
                    return

# Function to handle the payment process
def pay():
    # Calculate the total payment by summing up the total price of all bought games
    total_payment = sum(info['total_price'] for info in bought_games.values())
    
    # Create a pop-up window to input the payment amount
    payment_input = simpledialog.askfloat("Payment", f"Total Payment: ${total_payment:.2f}\nEnter Payment Amount:")
    
    # Check if payment_input is not None (i.e., the user entered a payment amount)
    if payment_input is not None:
        # If the payment amount is less than the total payment, show a warning message
        if payment_input < total_payment:
            messagebox.showwarning("Warning", "Insufficient payment.")
        # If the payment amount is equal to or greater than the total payment, proceed with the payment process
        else:
            # Calculate the change (if any)
            change = payment_input - total_payment
            # Show a success message with the change amount
            messagebox.showinfo("Payment Successful", f"Payment Successful!\nChange: ${change:.2f}")
    
    # Clear the list of bought games and update the display
    bought_games.clear()
    display_bought_games()

# Function to switch between frames (not defined in the provided code snippet)
def show_frame(frame):
    frame.tkraise()
    
# Create the main window for the application
root = tk.Tk()
root.title("Game Store")

# Configure grid weights
for i in range(2):
    root.grid_rowconfigure(i, weight=1)
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

# Frame for displaying the list of consoles
console_frame = ttk.LabelFrame(root, text="Consoles")
console_frame.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

# Create a scrollbar for the console list
console_scroll = ttk.Scrollbar(console_frame, orient=tk.VERTICAL)
console_list = tk.Listbox(console_frame, yscrollcommand=console_scroll.set)
console_scroll.config(command=console_list.yview)
console_scroll.pack(side=tk.RIGHT, fill=tk.Y)
console_list.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
display_console_list() # Display the list of consoles

# Frame for displaying the list of games
game_frame = ttk.LabelFrame(root, text="Games")
game_frame.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
game_frame.grid_forget()
columns = ("Name", "Price", "Stock") # Define columns for the game tree

# Create a scrollbar for the game tree
game_scroll = ttk.Scrollbar(game_frame, orient=tk.VERTICAL)
game_tree = ttk.Treeview(game_frame, columns=columns, show="headings", yscrollcommand=game_scroll.set)

# Set headings for the columns
for col in columns: 
    game_tree.heading(col, text=col)

# Configure scrollbar for the game tree
game_scroll.config(command=game_tree.yview)
game_scroll.pack(side=tk.RIGHT, fill=tk.Y)
game_tree.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Bind events to the console list and game tree
console_list.bind("<<ListboxSelect>>", display_game_by_console)
game_tree.bind("<<TreeviewSelect>>", on_game_select)

# Frame for action menu
menu_frame = ttk.LabelFrame(root, text="Actions")
menu_frame.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

# Frame for adding a game
add_frame = ttk.LabelFrame(root, text="Add Game")
add_frame.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W+tk.E)
add_frame.grid_forget() # Hide the add game frame initially

# Create labels and entry fields for adding a game
tk.Label(add_frame, text="Console Name:").grid(row=0, column=0, padx=5, pady=5)
console_entry = ttk.Combobox(add_frame, values=[console.capitalize() for game in game_list for console in game.keys()], state="readonly")
console_entry.grid(row=0, column=1, padx=5, pady=5)
console_entry.set("Select Console")

tk.Label(add_frame, text="Game Name:").grid(row=1, column=0, padx=5, pady=5)
game_name_entry = tk.Entry(add_frame)
game_name_entry.grid(row=1, column=1, padx=5, pady=5)
game_name_entry.insert(0, "Enter Game Name")

tk.Label(add_frame, text="Game Price:").grid(row=2, column=0, padx=5, pady=5)
game_price_entry = tk.Entry(add_frame)
game_price_entry.grid(row=2, column=1, padx=5, pady=5)
game_price_entry.insert(0, "0.00")

add_button = ttk.Button(add_frame, text="Add Game", command=add_game)
add_button.grid(row=3, column=0, columnspan=2, pady=5)

# Frame for editing a game
edit_frame = ttk.LabelFrame(root, text="Edit Game")
edit_frame.grid(row=2, column=0, padx=2, pady=5, sticky=tk.W+tk.E)
edit_frame.grid_forget()
tk.Label(edit_frame, text="New Game Name:").grid(row=0, column=0, padx=5, pady=5)
new_game_name_entry = tk.Entry(edit_frame)
new_game_name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(edit_frame, text="New Game Price:").grid(row=1, column=0, padx=5, pady=5)
new_game_price_entry = tk.Entry(edit_frame)
new_game_price_entry.grid(row=1, column=1, padx=5, pady=5)

edit_button = ttk.Button(edit_frame, text="Edit Game", command=edit_game)
edit_button.grid(row=2, column=0, columnspan=2, pady=5)

# Frame for displaying the list of bought games
bought_game_frame = ttk.LabelFrame(root, text="List of Purchased Games")
bought_game_frame.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W+tk.E)
bought_game_frame.grid_forget()
columns = ("Name", "Quantity", "Price", "Total Price")
bought_game_tree = ttk.Treeview(bought_game_frame, columns=columns, show="headings")

# Define columns for the bought game tree
for col in columns:
    bought_game_tree.heading(col, text=col)

# Pack the bought_game_tree widget to fill the available space in its container
bought_game_tree.pack(padx=10, pady=5, fill=tk.BOTH, expand=True) 

buy_frame = ttk.LabelFrame(root, text="Buy Game") # Create a LabelFrame named buy_frame to contain the widgets for buying a game
buy_frame.grid(row=0, column=1, padx=2, pady=2, sticky=tk.SW)  # Place the frame in the grid
buy_frame.grid_forget()# Initially hide the buy_frame

tk.Label(buy_frame, text="Quantity:").grid(row=0, column=0, padx=2, pady=2) # Create a label widget for displaying "Quantity:" and place it inside the buy_frame
buy_quantity_entry = tk.Entry(buy_frame) # Create an entry widget for entering the quantity of the game to buy and place it inside the buy_frame
buy_quantity_entry.grid(row=0, column=1, padx=2, pady=2)

buy_button = ttk.Button(buy_frame, text="Next..", command=buy_game) # Create a button widget labeled "Next.." to trigger the buy_game function and place it inside the buy_frame
buy_button.grid(row=0, column=2, padx=2, pady=2)


# Frame for pay button
pay_button = tk.Button(root, text="Pay", command=pay, width=2)
pay_button.grid(row=2, column=1, padx=2, pady=2, sticky=tk.W+tk.E)
pay_button.grid_forget()

# Hide the game list frame purchased at the beginning
bought_game_frame.grid_forget()

# Frame to delete the game
remove_frame = ttk.LabelFrame(root, text="Remove Game")
remove_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W+tk.E)
remove_frame.grid_forget()
remove_button = ttk.Button(remove_frame, text="Remove Game", command=remove_game)
remove_button.grid(row=0, column=0, columnspan=2, pady=5)

# Frame to update the game stock
update_stock_frame = ttk.LabelFrame(root, text="Update Stock")
update_stock_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=tk.W+tk.E)
update_stock_frame.grid_forget()
tk.Label(update_stock_frame, text="New Stock:").grid(row=0, column=0, padx=2, pady=1)
new_stock_entry = tk.Entry(update_stock_frame)
new_stock_entry.grid(row=0, column=1, padx=2, pady=1)

update_stock_button = ttk.Button(update_stock_frame, text="Update Stock", command=update_stock)
update_stock_button.grid(row=1, column=0, columnspan=2, padx=2, pady=5)

# This line starts the Tkinter event loop, which is necessary for running the GUI application.
root.mainloop()
