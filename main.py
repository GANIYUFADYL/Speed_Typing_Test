import tkinter as tk
import time
import random


class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")

        self.sentences = [
            "The quick brown fox jumps over the lazy dog.",
            "A journey of a thousand miles begins with a single step.",
            "To be or not to be, that is the question.",
            "All that glitters is not gold.",
            "In the middle of difficulty lies opportunity."
        ]

        self.selected_sentence = random.choice(self.sentences)
        self.start_time = None

        self.label = tk.Label(master, text="Type the following sentence:")
        self.label.pack(pady=10)

        self.sentence_label = tk.Label(master, text=self.selected_sentence, font=("Helvetica", 12))
        self.sentence_label.pack(pady=10)

        self.text_entry = tk.Text(master, height=5, width=50)
        self.text_entry.pack(pady=10)

        self.start_button = tk.Button(master, text="Start", command=self.start_test)
        self.start_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def start_test(self):
        self.start_time = time.time()
        self.text_entry.delete(1.0, tk.END)  # Clear previous text
        self.text_entry.bind("<KeyRelease>", self.check_text)

    def check_text(self, event):
        typed_text = self.text_entry.get(1.0, tk.END).strip()
        if typed_text == self.selected_sentence:
            end_time = time.time()
            time_taken = end_time - self.start_time
            words_per_minute = (len(typed_text.split()) / time_taken) * 60
            self.result_label.config(text=f"Well done! Your typing speed is {words_per_minute:.2f} WPM.")
            self.text_entry.unbind("<KeyRelease>")  # Stop checking after completion


if __name__ == "__main__":
    root = tk.Tk()
    typing_test = TypingSpeedTest(root)
    root.mainloop()