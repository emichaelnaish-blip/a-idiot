import time
import streamlit as st

# Page setup for mobile-like framing
st.set_page_config(page_title="A-Idiot Bot", page_icon="🤖", layout="centered")

# Custom CSS to style it like a sleek, dark-mode mobile chat app
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    /* Hide Streamlit branding for clean film look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""",
    unsafe_allow_html=True,
)

# App Header
st.markdown(
    "<h3 style='text-align: center; color: #00ffcc;'>A-Idiot Bot</h3>",
    unsafe_allow_html=True,
)
st.markdown("---")

# Initialize chat history in session state so it scrolls
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display existing chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input box (acts like the phone keyboard trigger)
if prompt := st.chat_input("Ask A-Idiot Bot anything..."):
    # 1. Display whatever the actor types immediately
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Fixed pre-scripted response that triggers for ANY input
    scripted_response = """That's an ambitious goal and there's no better time to start saving than the present! To make $200,000 in 24 hours, you have a couple options to choose from:

1. **Stock Liquidation** -- if you have over $200k in stocks in your investment account, this will be the quickest way to instantly get $200k in your bank account! Just call your broker and have them set up a withdrawal ASAP.

2. **Inheritance** -- A wealthy family member to which you are the heir passing away is also a quick process compared to most wealth building enterprises. Do you have any family members that have recently passed away?

3. **Selling material items** --- If neither of the above, I'd suggest selling enough of your material investments -- such as your house, cars, boats, and other valuables -- although this process certainly can take longer than 24 hours!"""

    # 3. Simulate the bot typing out the response word-by-word
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        full_response = ""

        for chunk in scripted_response.split():
            full_response += chunk + " "
            time.sleep(
                0.04
            )  # Adjust this speed higher or lower for typing effect
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    # Save assistant response to history so it stays on screen when scrolling
    st.session_state.messages.append(
        {"role": "assistant", "content": scripted_response}
    )