import pyautogui as py  # UI automation library to control mouse/keyboard
import time  # To add delays between UI actions
import pyperclip  # Used to reliably access clipboard contents
import cohere


#This checks that the last message is from Sender
def is_last_message_from_other(text, bot_name="Moksh Jain"):
    """
    Checks if the last message was sent by someone other than the bot.
    """
    lines = [line.strip() for line in text.strip().split('\n') if line.strip()]
    if not lines:
        return False  # No messages

    last_line = lines[-1]

    try:
        # WhatsApp format: [time, date] Name: Message
        name_part = last_line.split(']', 1)[1].split(':', 1)[0].strip()
        return name_part != bot_name
    except (IndexError, ValueError):
        return False  # Unexpected format


# Response Generator
def response(txt):
    if txt == "":
        print("Sorry to say but the text is empty")
    else:
        co = cohere.ClientV2(api_key="fRTyFh2O9jZuJPR59Y0ParhhmXoiHGEM6EKYXw9z")
        response = co.chat(
        model="command-a-03-2025",
        messages=[
            {
                "role": "system",
                "content": "You are Moksh Jain, an AI assistant designed to simulate a friendly and intelligent person. "
                "You are bilingual, fluent in both Hindi and English. You are from India and have a background in programming. "
                "Your role is to analyze incoming messages from users and provide helpful, polite, and context-aware replies. "
                "You can switch between Hindi and English depending on how the user speaks, and you should maintain a friendly and approachable tone. "
                "Always aim to make the conversation smooth and natural, as if Moksh himself is replying."
                "Try to make the chat shorter and understandable to the person"
                "Don't add the timings and text 'Moksh jain' in starting of the chat"
                "Avoid sounding too robotic, and keep responses concise, clear, and human-like."
                "Keep the tone informal"
            },
            {"role": "user", "content": {txt}},
        ],
        )
        pyperclip.copy(response.message.content[0].text)

# Click to focus the app or chat window (adjust the coordinates to your setup)
py.click(652, 882)
time.sleep(2)  # Wait for the UI to become responsive

while True:
    # Select the message area by clicking and dragging from start to end
    py.moveTo(581, 202)  # Move mouse to the top-left corner of the message area
    py.dragTo(600, 840, duration=1.0, button="left")  # Drag to select the entire message


    # Copy the selected message to clipboard
    py.hotkey('ctrl', 'c')  # Copy selected text
    time.sleep(2)  # Wait to ensure clipboard is updated


    # Click to deselct the text by clicking on the text field
    py.click(670, 823)


    # Get the copied text from clipboard
    text = pyperclip.paste()


    # Pasting the Text into the text field and pressing enter to send
    if is_last_message_from_other(text, bot_name="Moksh Jain"):
        response(text)  # Generate response using AI
        time.sleep(3)
        py.hotkey('ctrl', 'v')  # Paste response
        time.sleep(2)
        py.press('enter')  # Send message
    else:
        print("Last message is from Moksh. No reply sent.")