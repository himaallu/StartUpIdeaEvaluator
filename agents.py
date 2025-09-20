from transformers import pipeline

# Initialize Hugging Face pipelines for each "agent"
market_agent = pipeline("text-generation", model="gpt2")
competitor_agent = pipeline("text-generation", model="gpt2")
pitch_agent = pipeline("summarization", model="facebook/bart-large-cnn")

# Functions to run the agents
def generate_market_research(idea: str):
    prompt = f"Conduct market research for this startup idea: {idea}"
    result = market_agent(prompt, max_length=150, do_sample=True)[0]['generated_text']
    return result

def analyze_competitors(idea: str):
    prompt = f"Analyze competitors for this startup idea: {idea}"
    result = competitor_agent(prompt, max_length=150, do_sample=True)[0]['generated_text']
    return result

def generate_pitch_summary(text: str):
    summary = pitch_agent(text, max_length=500, min_length=50, do_sample=False)[0]['summary_text']
    return summary
