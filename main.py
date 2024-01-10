import argparse
import tkinter as tk
from ai import (
    init_replicant,
    send_message,
)


class UI:

    def __init__(self, mode: str = "offline"):
        self._build_app()
        self._input_text: tk.Text
        self._output_text


    # Create a function to send the prompt to ChatGPT and display the response
    def send_prompt(self) -> str:
        """
        Send message and receive response
        """

        message = self._input_text.get("1.0")

        default_message = "Compose a poem that explains the concept of recursion in programming."
        if message == '':
            message = default_message

        # Send out Basic Message
        response = send_message(message=message)

        default_response = "Test Response"
        if response == '':
            response = default_response

        self._output_text.insert("1.0", response)

        return response

    def _build_app(self,):

        # Create the main application window
        app = tk.Tk()
        app.title("ChatGPT UI")
        app.geometry("800x600")

        # Create a label for the question and center it over the Text widget
        question_label = tk.Label(app, text="Question")
        question_label.grid(row=0, column=0, columnspan=2)  # Centered over 2 columns
        question_label.configure(anchor='center')

        # Create an input field for the user's prompts
        self._input_text = tk.Text(app, height=10, width=80)
        self._input_text.grid(row=1, column=0, padx=10, pady=10)  # Use grid layout

        # Create a button to send the prompt
        send_button = tk.Button(app, text="Send", command=self.send_prompt)
        send_button.grid(row=2, column=0, pady=10)

        # Create a label for the question and center it over the Text widget
        response_label = tk.Label(app, text="Response")
        response_label.grid(row=3, column=0, columnspan=2)  # Centered over 2 columns
        response_label.configure(anchor='center')

        # Create an input field for the user's prompts
        self._output_text = tk.Text(app, height=10, width=80)
        self._output_text.grid(row=4, column=0, padx=10, pady=10)  # Use grid layout

        # Start the tkinter main loop
        app.mainloop()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="CLI with 'mode' option")

    # Add the 'mode' argument with choices 'online' and 'offline'
    parser.add_argument(
        '--mode',
        choices=['online', 'offline'],
        required=True,
        help="Select 'online' or 'offline' mode"
    )

    args = parser.parse_args()

    # Access the selected mode
    selected_mode = args.mode
    print(f"Selected mode: {selected_mode}")

    # Input AI System Prompts
    if selected_mode == 'online':
        print("Setting up System Prompts...")
        # Setup Replicant
        init_replicant()
        print("Done Setting up System Prompts...")

    print("Building App...")
    app = UI(mode=selected_mode)
