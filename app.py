import streamlit as st
from feedback_generator import generate_feedback  # assumes both files are in the same folder

st.title("Classroom Observation Feedback Generator")

st.write("Paste your observation notes below:")

notes = st.text_area("Observation Notes", height=300)

if st.button("Generate Feedback"):
    if notes.strip() == "":
        st.warning("Please enter some observation notes.")
    else:
        highlights, recommendations = generate_feedback(notes)

        for category in highlights:
            st.subheader(f"Category: {category}")
            st.markdown(f"**Highlights:** {highlights[category]['summary']}")
            st.markdown(f"**Recommendation:** {recommendations[category]['suggestion']}")
            st.markdown(f"**Reflection Prompt:** {highlights[category]['reflection']}")
            st.markdown("---")
