import tkinter as tk
from ai import (
    init_replicant,
    send_message,
)


# Create a function to send the prompt to ChatGPT and display the response
def send_prompt():
    prompt = input_text.get("1.0")

    default_prompt = "Compose a poem that explains the concept of recursion in programming."
    if prompt == '':
        prompt = default_prompt

    # Send out Basic Message
    response = send_message(message=prompt)

    output_text.insert("1.0", response)


if __name__ == '__main__':
    # Create the main application window
    app = tk.Tk()
    app.title("ChatGPT UI")
    app.geometry("800x600")

    # Create a label for the question and center it over the Text widget
    question_label = tk.Label(app, text="Question")
    question_label.grid(row=0, column=0, columnspan=2)  # Centered over 2 columns
    question_label.configure(anchor='center')

    # Create an input field for the user's prompts
    input_text = tk.Text(app, height=10, width=80)
    input_text.grid(row=1, column=0, padx=10, pady=10)  # Use grid layout

    # Create a button to send the prompt
    send_button = tk.Button(app, text="Send", command=send_prompt)
    send_button.grid(row=2, column=0, pady=10)

    # Create a label for the question and center it over the Text widget
    response_label = tk.Label(app, text="Response")
    response_label.grid(row=3, column=0, columnspan=2)  # Centered over 2 columns
    response_label.configure(anchor='center')

    # Create an input field for the user's prompts
    output_text = tk.Text(app, height=10, width=80)
    output_text.grid(row=4, column=0, padx=10, pady=10)  # Use grid layout

    # Setup Replicant
    init_replicant()

    # Start the tkinter main loop
    app.mainloop()
