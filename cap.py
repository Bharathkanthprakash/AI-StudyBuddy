import streamlit as st
from transformers import pipeline

# Page config
st.set_page_config(
    page_title="AI StudyBuddy",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 AI StudyBuddy")
st.markdown("### Your Smart Learning Assistant")

# Input
topic = st.text_input("📘 Enter Topic")

# Feature selection
option = st.selectbox(
    "Choose Feature",
    (
        "Explanation",
        "Summary",
        "Quiz",
        "Interview Prep"
    )
)

# Load model
@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="google/flan-t5-base"
    )

generator = load_model()

# Generate
if st.button("🚀 Generate"):

    if topic:
        with st.spinner("Thinking... 🤖"):

            if option == "Explanation":
                prompt = f"Instruction: Explain {topic} in simple terms.\nResponse:"

            elif option == "Summary":
                prompt = f"Instruction: Give short bullet point notes about {topic}.\nResponse:"

            elif option == "Quiz":
                prompt = f"Instruction: Create 5 quiz questions with answers about {topic}.\nResponse:"

            elif option == "Interview Prep":
                prompt = f"Instruction: Generate 5 interview questions about {topic}.\nResponse:"

            result = generator(
                prompt,
                max_length=200,
                temperature=0.3,
                do_sample=True
            )

            output = result[0]['generated_text']

            st.success("Done ✅")
            st.write(output)

            st.download_button(
                label="📥 Download Result",
                data=output,
                file_name="AI_StudyBuddy_Result.txt",
                mime="text/plain"
            )

    else:
        st.warning("Please enter a topic!")