THEME_COLOR = "#375362"

from tkinter import*
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 15))
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, #width ustawia nam jak a chcemy szerokość tekstu, żeby nie wyleciał nam za obręb canvasa
            text="Dupa", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)

        self.button_right = Button()
        image_right = PhotoImage(file="images/true.png")
        self.button_right.config(image=image_right, highlightthickness=0, command=self.is_right)
        self.button_right.grid(row=2, column=0)

        image_false = PhotoImage(file="images/false.png")
        self.button_false = Button(image=image_false, highlightthickness=0, command=self.is_wrong)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.button_right.config(state="disabled") # sprawia, że nie możemy wcisnąć guzików
            self.button_false.config(state="disabled")

    def is_right(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))

    def is_wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)