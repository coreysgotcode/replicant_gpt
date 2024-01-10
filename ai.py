from openai import OpenAI

# Replace 'YOUR_API_KEY' with your OpenAI API key
DEFAULT_API_KEY = "<YOUR_API_KEY>"
OPEN_AI_API_KEY = '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' # TODO: Read API Key FROM OS

if OPEN_AI_API_KEY == DEFAULT_API_KEY:
    raise ValueError("Please set the OPEN_AI_API_KEY to a valid value")

client = OpenAI(api_key=OPEN_AI_API_KEY)

def init_replicant() -> None:
    """
    Set up the initial personality of the replicant via system messages
    """
    client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a poetic assistant, skilled in explaining complex programming concepts with "
                           "creative flair. "
            },
        ]
    )


def send_message(message: str) -> str:
    """
    Sends out Message and returns response
    :param message: Prompt for GPT as User Role
    :return: Response to User
    """

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message}
        ]
    )

    return completion.choices[0].message