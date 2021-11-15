# GUI for Hangman

import tkinter as tk
from functools import partial
from func.hangman_func import StartGame, PlayGame, hangman_pic


def ResetButton():
    global letters, used_letters, lp, last_chr
    letters, used_letters, lp, last_chr = StartGame()
    lbl_answer2["text"] = letters["gui"]
    lbl_used2["text"] = used_letters["gui"]
    lbl_pic["text"] = hangman_pic[6-lp]
    lbl_life["text"] = lp
    lbl_last1["text"] = "Last character : ".format(last_chr["character"])
    lbl_last2["text"] = last_chr["check"]
    ent_input.delete(0, tk.END)

def SubmitButton():
    global letters, used_letters, lp, last_chr
    letters, used_letters, lp, last_chr = PlayGame(letters_guess_param=ent_input.get(),
        letters_param=letters,
        used_letters_param=used_letters,
        lp_param=lp
    )

    if last_chr["check"] == "LOSE":
        lbl_answer2["text"] = letters["playgame_str"]
        lbl_used2["text"] = used_letters["gui"]
        lbl_pic["text"] = hangman_pic[6-lp]
        lbl_life["text"] = lp
        lbl_last1["text"] = "Game Over : "
        lbl_last2["text"] = "You lose"
        ent_input.delete(0, tk.END)
    elif last_chr["check"] == "WIN":
        lbl_answer2["text"] = letters["playgame_str"]
        lbl_used2["text"] = used_letters["gui"]
        lbl_pic["text"] = hangman_pic[6-lp]
        lbl_life["text"] = lp
        lbl_last1["text"] = "Game Over : "
        lbl_last2["text"] = "You win"
        ent_input.delete(0, tk.END)
    else:
        lbl_answer2["text"] = letters["gui"]
        lbl_used2["text"] = used_letters["gui"]
        lbl_pic["text"] = hangman_pic[6-lp]
        lbl_life["text"] = lp
        lbl_last1["text"] = "Last character '{}' : ".format(last_chr["character"])
        lbl_last2["text"] = last_chr["check"]
        ent_input.delete(0, tk.END)

letters, used_letters, lp, last_chr = StartGame()

# window
window = tk.Tk()
window.title("Hangman")
window.rowconfigure(0, minsize=200, weight=1)
window.columnconfigure(0, minsize=200, weight=1)
window.columnconfigure(1, minsize=100, weight=1)
window.columnconfigure(2, minsize=100, weight=1)

# frame
frm_a = tk.Frame(master=window)
frm_b = tk.Frame(master=window)
frm_c = tk.Frame(master=window)
frm_a.grid(row=0, column=0, sticky="ns")
frm_b.grid(row=0, column=1, sticky="ns")
frm_c.grid(row=0, column=2, sticky="ns")

# label
lbl_pic = tk.Label(master=frm_a, text=hangman_pic[6-lp])
lbl_life = tk.Label(master=frm_a, text=lp)
lbl_pic.grid(row=0, column=0, sticky="ew")
lbl_life.grid(row=1, column=0, sticky="ew")

lbl_answer1 = tk.Label(master=frm_b, text="Answer : ")
lbl_used1 = tk.Label(master=frm_b, text="Letters you\'ve guess : ")
lbl_last1 = tk.Label(master=frm_b, text="Last character : ")
lbl_input = tk.Label(master=frm_b, text="Input : ")
lbl_answer1.grid(row=0, column=1, sticky="e")
lbl_used1.grid(row=1, column=1, sticky="e")
lbl_last1.grid(row=2, column=1, sticky="e")
lbl_input.grid(row=3, column=1, sticky="e")

lbl_answer2 = tk.Label(master=frm_c, text=letters["gui"])
lbl_used2 = tk.Label(master=frm_c, text=used_letters["gui"])
lbl_last2 = tk.Label(master=frm_c, text=last_chr["character"])
lbl_answer2.grid(row=0, column=2, sticky="w")
lbl_used2.grid(row=1, column=2, sticky="w")
lbl_last2.grid(row=2, column=2, sticky="w")

# entry
ent_input = tk.Entry(master=frm_c)
ent_input.grid(row=3, column=2, sticky="w")

# button
btn_input = tk.Button(master=frm_c, text="Submit", command=SubmitButton)
btn_reset = tk.Button(master=frm_a, text="Reset", command=ResetButton)
btn_input.grid(row=3, column=2, sticky="e")
btn_reset.grid(row=2, column=0)

window.mainloop()