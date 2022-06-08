# Yasaman Yazdandoost 9708193
# project 2
import tkinter as tk


def show_result(patrik_cards, bob_cards):
    second_page = tk.Tk()
    second_page.title("Result")
    second_page.geometry("200x170")

    lab = tk.Label(second_page, text="Patrik cards: " + str(patrik_cards)[1:-1], border=5, fg="blue")
    lab.pack()

    lab = tk.Label(second_page, text="Bob cards: " + str(bob_cards)[1:-1], border=5, fg="blue")
    lab.pack()

    cancel_button = tk.Button(second_page, height=1, width=10, text="Ok", command=second_page.destroy)
    cancel_button.pack()

    second_page.mainloop()


def divide_cards(cards, n):
    patrik_cards = []
    bob_cards = []
    sum_cards = sum(cards)
    average = sum_cards // 2
    cards = sorted(cards, reverse=True)

    if cards[0] >= average:
        patrik_cards.append(cards[0])
        bob_cards = cards[1:]
    else:
        patrik_cards.append(cards[0])
        for i in range(1, n):
            sum_patrik_cards = sum(patrik_cards)
            if sum_patrik_cards + cards[i] > average:
                bob_cards.append(cards[i])
            else:
                patrik_cards.append(cards[i])
    show_result(patrik_cards, bob_cards)


def get_input_text():
    entry = input_text.get("1.0", "end")
    entry = [int(i) for i in entry.split('\n')[0]]
    n = entry[0]
    entry.pop(0)
    divide_cards(entry, n)


first_page = tk.Tk()
first_page.title("Input")
first_page.geometry("180x150")

label = tk.Label(first_page, text="Enter Your Cards", border=5)
label.pack()

input_text = tk.Text(first_page, height=1, width=10, border=5)
input_text.pack()

Start_Button = tk.Button(first_page, height=1, width=10, text="Ok", command=get_input_text)
Quit_Button = tk.Button(first_page, height=1, width=10, text="Cancel", command=first_page.destroy)

Start_Button.pack()
Quit_Button.pack()

first_page.mainloop()
