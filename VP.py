import nltk
import streamlit as st
import speech_recognition as sr
from nltk.chat.util import Chat, reflections
# Sample patterns and responses
pairs = [
    ["my name is (.*)", ["Hello %1, how are you today?"]],
    ["(hi|hello|hey)", ["Hello", "Hi there"]],
    ["(.*) (location|city) ?", ["I am in a virtual world"]],
    ["how is the weather in (.*)", ["The weather in %1 is fantastic!"]],
    ["quit", ["Bye! Take care."]],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)
def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please say something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            st.write(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I did not understand that.")
            return None
        except sr.RequestError as e:
            st.write(f"Could not request results; {e}")
            return None
def chatbot_response(user_input):
    return chatbot.respond(user_input)
def main():
    st.title("Text and Speech Input Chatbot")
    
    input_type = st.radio("Choose input type:", ("Text", "Speech"))

    if input_type == "Text":
        user_input = st.text_input("You: ", "")
        if user_input:
            response = chatbot_response(user_input)
            st.write(f"Chatbot: {response}")

    elif input_type == "Speech":
        if st.button("Talk to Chatbot"):
            user_input = transcribe_speech()
            if user_input:
                response = chatbot_response(user_input)
                st.write(f"Chatbot: {response}")

if __name__ == "__main__":
    main()

