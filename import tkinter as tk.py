import tkinter as tk


root = tk.Tk()
root.title("Survey Form")


question1_label = tk.Label(root, text="Question 1:")
question1_label.pack()
question1_entry = tk.Entry(root)
question1_entry.pack()

question2_label = tk.Label(root, text="Question 2:")
question2_label.pack()
question2_entry = tk.Entry(root)
question2_entry.pack()




submit_button = tk.Button(root, text="Submit", command=lambda: print_answers())
submit_button.pack()


def print_answers():
    answers = {
        "Question 1": question1_entry.get(),
        "Question 2": question2_entry.get(),
        
    }
    print("Survey Answers:")
    for question, answer in answers.items():
        print(f"{question}: {answer}")


root.mainloop()
