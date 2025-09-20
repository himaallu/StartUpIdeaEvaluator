from transformers import pipeline

# Load Hugging Face text-generation model
generator = pipeline("text-generation", model="tiiuae/falcon-7b-instruct")

def market_research(agent_input):
    """Agent 1: Market Researcher"""
    prompt = f"Do detailed market research for this startup idea: {agent_input}"
    response = generator(prompt, max_new_tokens=200)[0]['generated_text']
    return response

def competitor_analysis(agent_input):
    """Agent 2: Competitor Analyst"""
    prompt = f"Identify top competitors for this startup idea: {agent_input} and analyze their strengths and weaknesses."
    response = generator(prompt, max_new_tokens=200)[0]['generated_text']
    return response

def pitch_deck_summary(agent_input, market, competitors):
    """Agent 3: Pitch Deck Generator"""
    prompt = (
        f"Generate a concise pitch deck summary for the startup idea: {agent_input}\n\n"
        f"Include the following sections:\n"
        f"- Problem\n- Solution\n- Market (use this info: {market})\n"
        f"- Competitors (use this info: {competitors})\n- Business Model\n- Next Steps"
    )
    response = generator(prompt, max_new_tokens=300)[0]['generated_text']
    return response
