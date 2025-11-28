import streamlit as st
from agent import generate_summary, generate_quiz
from utils import extract_text_from_pdf

def main():
    st.set_page_config(page_title="Study Notes Summarizer & Quiz Generator", layout="wide")
    st.title("📚 Study Notes Summarizer & Quiz Generator")
    st.markdown("Upload your study notes in PDF format, and let the AI agent help you summarize the key points and generate a quiz to test your knowledge.")

    st.sidebar.title("Controls")
    uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file:
        try:
            pdf_text = extract_text_from_pdf(uploaded_file)
            st.success("PDF successfully processed. You can now generate a summary or a quiz.")

            if st.sidebar.button("Generate Summary"):
                with st.spinner("Generating summary..."):
                    summary = generate_summary(pdf_text)
                    st.subheader("Summary")
                    st.write(summary)

            if st.sidebar.button("Generate Quiz"):
                with st.spinner("Generating quiz..."):
                    quiz = generate_quiz(pdf_text)
                    st.subheader("Quiz")
                    st.write(quiz)

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
