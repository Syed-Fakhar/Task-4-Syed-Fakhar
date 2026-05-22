# gui_quiz.py
import tkinter as tk
from tkinter import font as tkfont

class ModernQuizApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Python Premium Quiz")
        self.geometry("520x450")
        self.resizable(False, False)
        
        # Color Palette - Premium Sleek Dark Mode
        self.bg_main = "#121218"        # Deep rich background
        self.bg_card = "#1e1e28"        # Card background
        self.color_accent = "#6366f1"   # Indigo accents
        self.color_accent_hover = "#4f46e5"
        self.color_text_main = "#f8fafc"# Off-white
        self.color_text_muted = "#94a3b8"# Slate blue/gray
        self.color_success = "#10b981"  # Emerald Green
        self.color_error = "#f43f5e"    # Rose Red
        self.color_input_bg = "#27273a" # Slightly lighter input area
        
        self.configure(bg=self.bg_main)
        
        # Configure modern fonts
        self.font_title = tkfont.Font(self, family="Helvetica", size=20, weight="bold")
        self.font_header = tkfont.Font(self, family="Helvetica", size=13, weight="bold")
        self.font_body = tkfont.Font(self, family="Helvetica", size=11, weight="normal")
        self.font_button = tkfont.Font(self, family="Helvetica", size=11, weight="bold")
        
        # Quiz data
        self.questions = [
            {
                "question": "What is the capital of France?",
                "correct_answer": "paris",
                "display_correct": "Paris"
            },
            {
                "question": "Which programming language is named after a type of snake?",
                "correct_answer": "python",
                "display_correct": "Python"
            },
            {
                "question": "What is the result of 2 + 3 * 4 in Python?",
                "correct_answer": "14",
                "display_correct": "14"
            }
        ]
        
        # State variables
        self.score = 0
        self.current_question_idx = 0
        self.quiz_active = False
        
        # Container frame
        self.container = tk.Frame(self, bg=self.bg_main)
        self.container.pack(fill="both", expand=True, padx=30, pady=30)
        self.container.pack_propagate(False)
        
        # Show welcome screen
        self.show_welcome_screen()
        
    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_welcome_screen(self):
        self.clear_container()
        self.score = 0
        self.current_question_idx = 0
        
        # Main Title
        title_label = tk.Label(
            self.container, 
            text="Python Trivia Quiz", 
            fg=self.color_text_main, 
            bg=self.bg_main,
            font=self.font_title
        )
        title_label.pack(pady=(40, 10))
        
        # Subtitle / Description
        desc_label = tk.Label(
            self.container, 
            text="Test your knowledge with our quick 3-question quiz.\nCan you score a perfect 3/3?", 
            fg=self.color_text_muted, 
            bg=self.bg_main,
            font=self.font_body,
            justify="center"
        )
        desc_label.pack(pady=(0, 40))
        
        # Start Card / Button Frame
        card = tk.Frame(self.container, bg=self.bg_card, bd=0, highlightthickness=0)
        card.pack(fill="x", padx=20, pady=10)
        
        # A simple visual detail to simulate rounded aesthetic
        card_inner = tk.Frame(card, bg=self.bg_card, padx=20, pady=30)
        card_inner.pack()
        
        start_btn = tk.Button(
            card_inner,
            text="START QUIZ",
            bg=self.color_accent,
            fg=self.color_text_main,
            activebackground=self.color_accent_hover,
            activeforeground=self.color_text_main,
            font=self.font_button,
            bd=0,
            cursor="hand2",
            padx=30,
            pady=12,
            relief="flat",
            command=self.start_quiz
        )
        start_btn.pack()
        
        # Dynamic button hover effects
        start_btn.bind("<Enter>", lambda e: start_btn.config(bg=self.color_accent_hover))
        start_btn.bind("<Leave>", lambda e: start_btn.config(bg=self.color_accent))

    def start_quiz(self):
        self.quiz_active = True
        self.show_question()

    def show_question(self):
        self.clear_container()
        
        q_data = self.questions[self.current_question_idx]
        
        # Top bar: Progress indicator & Score indicator
        top_bar = tk.Frame(self.container, bg=self.bg_main)
        top_bar.pack(fill="x", pady=(0, 20))
        
        progress_lbl = tk.Label(
            top_bar,
            text=f"Question {self.current_question_idx + 1} of {len(self.questions)}",
            fg=self.color_text_muted,
            bg=self.bg_main,
            font=self.font_body
        )
        progress_lbl.pack(side="left")
        
        score_lbl = tk.Label(
            top_bar,
            text=f"Score: {self.score}",
            fg=self.color_accent,
            bg=self.bg_main,
            font=self.font_header
        )
        score_lbl.pack(side="right")
        
        # Question Card
        card = tk.Frame(self.container, bg=self.bg_card, padx=24, pady=24)
        card.pack(fill="both", expand=True)
        
        # Question Text
        self.q_label = tk.Label(
            card,
            text=q_data["question"],
            fg=self.color_text_main,
            bg=self.bg_card,
            font=self.font_header,
            wraplength=400,
            justify="center"
        )
        self.q_label.pack(pady=(10, 25))
        
        # Input Field Frame (For styling borders nicely)
        self.entry_frame = tk.Frame(card, bg=self.color_input_bg, padx=10, pady=5)
        self.entry_frame.pack(fill="x", pady=(0, 20))
        
        self.answer_entry = tk.Entry(
            self.entry_frame,
            fg=self.color_text_main,
            bg=self.color_input_bg,
            insertbackground=self.color_text_main, # cursor color
            font=self.font_body,
            bd=0,
            highlightthickness=0
        )
        self.answer_entry.pack(fill="x")
        self.answer_entry.focus_set()
        
        # Feedback placeholder Label
        self.feedback_label = tk.Label(
            card,
            text="",
            fg=self.color_text_main,
            bg=self.bg_card,
            font=self.font_body
        )
        self.feedback_label.pack(pady=(0, 15))
        
        # Action button (Submit / Next)
        self.action_btn = tk.Button(
            card,
            text="SUBMIT",
            bg=self.color_accent,
            fg=self.color_text_main,
            activebackground=self.color_accent_hover,
            activeforeground=self.color_text_main,
            font=self.font_button,
            bd=0,
            cursor="hand2",
            pady=10,
            relief="flat",
            command=self.submit_answer
        )
        self.action_btn.pack(fill="x")
        
        # Bindings
        self.action_btn.bind("<Enter>", lambda e: self.on_btn_hover())
        self.action_btn.bind("<Leave>", lambda e: self.on_btn_leave())
        self.bind("<Return>", lambda e: self.action_btn.invoke())

    def on_btn_hover(self):
        # Only hover to hover colors if state allows
        bg = self.action_btn.cget("bg")
        if bg == self.color_accent:
            self.action_btn.config(bg=self.color_accent_hover)

    def on_btn_leave(self):
        bg = self.action_btn.cget("bg")
        if bg == self.color_accent_hover:
            self.action_btn.config(bg=self.color_accent)

    def submit_answer(self):
        q_data = self.questions[self.current_question_idx]
        user_ans = self.answer_entry.get().strip()
        
        # If user submits an empty string, prevent submission or ignore
        if not user_ans and self.action_btn.cget("text") == "SUBMIT":
            return
            
        # If the state of the button is "NEXT", proceed to next screen
        if self.action_btn.cget("text") == "NEXT":
            self.current_question_idx += 1
            if self.current_question_idx < len(self.questions):
                self.show_question()
            else:
                self.show_results_screen()
            return
            
        # Disable editing
        self.answer_entry.config(state="disabled")
        self.entry_frame.config(bg="#1a1a24") # Darker out
        self.answer_entry.config(bg="#1a1a24")
        
        # Logic comparison
        is_correct = False
        if q_data["correct_answer"] == "14":
            is_correct = (user_ans == "14")
        else:
            is_correct = (user_ans.lower() == q_data["correct_answer"])
            
        if is_correct:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg=self.color_success)
            self.entry_frame.config(highlightbackground=self.color_success, highlightthickness=1)
        else:
            self.feedback_label.config(
                text=f"Wrong answer. The correct answer is: {q_data['display_correct']}", 
                fg=self.color_error
            )
            self.entry_frame.config(highlightbackground=self.color_error, highlightthickness=1)
            
        # Update button to next question
        self.action_btn.config(text="NEXT", bg=self.color_accent)

    def show_results_screen(self):
        self.clear_container()
        self.unbind("<Return>")
        
        title_label = tk.Label(
            self.container, 
            text="Quiz Complete!", 
            fg=self.color_text_main, 
            bg=self.bg_main,
            font=self.font_title
        )
        title_label.pack(pady=(40, 10))
        
        # Card container
        card = tk.Frame(self.container, bg=self.bg_card, padx=30, pady=30)
        card.pack(fill="x", padx=10, pady=10)
        
        # Final Score display
        score_percent = int((self.score / len(self.questions)) * 100)
        
        result_text = f"Quiz over! Your final score is {self.score}/{len(self.questions)}."
        
        score_label = tk.Label(
            card,
            text=result_text,
            fg=self.color_text_main,
            bg=self.bg_card,
            font=self.font_header,
            pady=10
        )
        score_label.pack()
        
        percentage_label = tk.Label(
            card,
            text=f"Grade: {score_percent}%",
            fg=self.color_success if score_percent >= 60 else self.color_error,
            bg=self.bg_card,
            font=self.font_title,
            pady=10
        )
        percentage_label.pack()
        
        restart_btn = tk.Button(
            card,
            text="RESTART QUIZ",
            bg=self.color_accent,
            fg=self.color_text_main,
            activebackground=self.color_accent_hover,
            activeforeground=self.color_text_main,
            font=self.font_button,
            bd=0,
            cursor="hand2",
            pady=10,
            relief="flat",
            command=self.show_welcome_screen
        )
        restart_btn.pack(fill="x", pady=(20, 0))
        
        restart_btn.bind("<Enter>", lambda e: restart_btn.config(bg=self.color_accent_hover))
        restart_btn.bind("<Leave>", lambda e: restart_btn.config(bg=self.color_accent))
        self.bind("<Return>", lambda e: restart_btn.invoke())

if __name__ == "__main__":
    app = ModernQuizApp()
    app.mainloop()
