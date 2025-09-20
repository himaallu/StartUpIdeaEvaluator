import streamlit as st
from agents import generate_market_research, analyze_competitors, generate_pitch_summary

st.set_page_config(page_title="Startup Idea Evaluator 🚀", layout="wide")
st.title("Startup Idea Evaluator 🚀")

# Input area
idea = st.text_area("Describe your startup idea:")

if st.button("Evaluate Idea"):
    if not idea.strip():
        st.warning("Please enter a startup idea first!")
    else:
        with st.spinner("Generating Market Research..."):
            market_output = generate_market_research(idea)
        with st.spinner("Analyzing Competitors..."):
            competitor_output = analyze_competitors(idea)
        with st.spinner("Generating Pitch Deck Summary..."):
            pitch_output = generate_pitch_summary(idea)

        # Display outputs
        st.subheader("📊 Market Research")
        st.write(market_output)

        st.subheader("🕵️ Competitor Analysis")
        st.write(competitor_output)

        st.subheader("📝 Pitch Deck Summary")
        st.write(pitch_output)

