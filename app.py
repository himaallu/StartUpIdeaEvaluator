import streamlit as st
from agents import evaluate_startup

st.set_page_config(page_title="Startup Idea Evaluator", page_icon="🚀")
st.title("🚀 Startup Idea Evaluator (CrewAI)")

idea = st.text_area("💡 Describe your startup idea:")

if st.button("Evaluate Idea"):
    if not idea.strip():
        st.warning("Please enter a startup idea!")
    else:
        with st.spinner("Running CrewAI agents..."):
            market, competitors, pitch = evaluate_startup(idea)
            
            st.subheader("📊 Market Research")
            st.write(market)
            
            st.subheader("⚔️ Competitor Analysis")
            st.write(competitors)
            
            st.subheader("📝 Pitch Deck Summary")
            st.write(pitch)
            
        st.success("✅ Evaluation Complete!")
