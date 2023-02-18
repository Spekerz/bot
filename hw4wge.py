import openai
import streamlit as st

# Set your API key
openai.api_key = "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"

# Define the Streamlit app
def app():
    # Set the page title
    st.set_page_config(page_title="NASAIChatBot")

    # Display the page header
    st.header("NASAIChatBot")

    # Prompt the user to enter some text
    prompt = st.text_input("Enter your prompt, be specific:")

    # Generate the OpenAI API response
    if st.button("Generate"):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=3950,
            n=1,
            stop=None,
            temperature=1,
        )

        # Display the API response
        st.write(response.choices[0].text)

if __name__ == "__main__":
    app()
