import cloudscraper
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

scraper = cloudscraper.create_scraper()

prev_data = []

def update_gui():
    r = scraper.get('https://api.bloxflip.com/live-feed/all-bets').json()
    bets = r['bets']

    if bets != prev_data:
        prev_data.clear()
        prev_data.extend(bets)

        # Clear the bet lists
        for child in bet_list_1.winfo_children():
            child.destroy()
        for child in bet_list_2.winfo_children():
            child.destroy()

        # Split bets into two lists
        num_bets = len(bets)
        first_half = bets[:num_bets // 2]
        second_half = bets[num_bets // 2:]

        # Display bets in first list
        for bet in first_half:
            gamemode = bet['gamemode']
            username = bet['username']
            bet_amount = bet['bet']
            winnings = bet['winnings']
            
            # Create a rounded rectangle image as the background
            size = (400, 220)
            radius = 10
            bet_image = Image.new('RGBA', size, (40, 40, 40, 120))
            draw = ImageDraw.Draw(bet_image)
            draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=(60, 60, 60, 255))
            bet_photo = ImageTk.PhotoImage(bet_image)

            # Create a bet box with the rounded rectangle image as the background
            bet_box = tk.Label(master=bet_list_1, image=bet_photo, bg='#282828', bd=0, relief='solid', padx=10, pady=10, borderwidth=0)
            bet_box.image = bet_photo
            bet_box.grid(sticky='nsew', padx=10, pady=10)

            # Add bet information to the bet box
            gamemode_label = tk.Label(master=bet_box, text=f"Gamemode: {gamemode}", font=('Helvetica', 14), fg='#e6e6e6', bg='#3c3c3c')
            username_label = tk.Label(master=bet_box, text=f"Username: {username}", font=('Helvetica', 12), fg='#e6e6e6', bg='#3c3c3c')
            bet_label = tk.Label(master=bet_box, text=f"Bet: {bet_amount}", font=('Helvetica', 12), fg='#e6e6e6', bg='#3c3c3c')
            winnings_label = tk.Label(master=bet_box, text=f"Winnings: {winnings}", font=('Helvetica', 12), fg='#e6e6e6', bg='#3c3c3c')
            gamemode_label.grid(row=0, column=0, sticky='w', padx=(10,0), pady=(10,0))
            username_label.grid(row=1, column=0, sticky='w', padx=(10,0), pady=(0,0))
            bet_label.grid(row=2, column=0, sticky='w', padx=(10,0), pady=(0,0))
            winnings_label.grid(row=3, column=0, sticky='w', padx=(10,0), pady=(0,10))

        # Display bets in second list
        for bet in second_half:
            gamemode = bet['gamemode']
            username = bet['username']
            bet_amount = bet['bet']
            winnings = bet['winnings']

            # Create a rounded rectangle image as the background
            size = (400, 220)
            radius = 10
            bet_image = Image.new('RGBA', size, (40, 40, 40, 120))
            draw = ImageDraw.Draw(bet_image)
            draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=(60, 60, 60, 255))
            bet_photo = ImageTk.PhotoImage(bet_image)

            # Create a bet box with the rounded rectangle image as the background
            bet_box = tk.Label(master=bet_list_2, image=bet_photo, bg='#282828', bd=0, relief='solid', padx=10, pady=10, borderwidth=0)
            bet_box.image = bet_photo
            bet_box.grid(sticky='nsew', padx=10, pady=10)

            # Add bet information to the bet box
            gamemode_label = tk.Label(master=bet_box, text=f"Gamemode: {gamemode}", font=('Helvetica', 14), fg='#e6e6e6', bg='#3c3c3c')
            username_label = tk.Label(master=bet_box, text=f"Username: {username}", font=('Helvetica', 12), fg='#e6e6e6', bg='#3c3c3c')
            bet_label = tk.Label(master=bet_box, text=f"Bet: {bet_amount}", font=('Helvetica', 12), fg='#e6e6e6', bg='#3c3c3c')
            winnings_label = tk.Label(master=bet_box, text=f"Winnings: {winnings}", font=('Helvetica', 12), fg='#e6e6e6', bg='#3c3c3c')
            gamemode_label.grid(row=0, column=0, sticky='w', padx=(10,0), pady=(10,0))
            username_label.grid(row=1, column=0, sticky='w', padx=(10,0), pady=(0,0))
            bet_label.grid(row=2, column=0, sticky='w', padx=(10,0), pady=(0,0))
            winnings_label.grid(row=3, column=0, sticky='w', padx=(10,0), pady=(0,10))



    root.after(2000, update_gui)



root = tk.Tk()
root.configure(bg='#282828')
root.title("Bloxflip Bets")

text = tk.Label(root, text="Made by Aspect#6889", bg="#282828", fg="white", font=('Helvetica', 12, "bold"))
text.pack()

left_frame = tk.Frame(master=root, bg='#282828')
left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)
bet_list_1 = tk.Frame(master=left_frame, bg='#282828')
bet_list_1.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

right_frame = tk.Frame(master=root, bg='#282828')
right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)
bet_list_2 = tk.Frame(master=right_frame, bg='#282828')
bet_list_2.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Make the window not resizable
root.resizable(False, False)

# Start the GUI
update_gui()
root.mainloop()
