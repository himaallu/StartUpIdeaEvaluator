from crewai import Agent, Crew

# Define Market Research Agent
market_agent = Agent(
    name="Market Researcher",
    role="Collect market trends, customer needs, and growth opportunities.",
    goal="Provide market insights for a given startup idea."
)

# Define Competitor Analysis Agent
competitor_agent = Agent(
    name="Competitor Analyst",
    role="Analyze competitors in the same space.",
    goal="Provide top competitors, their strengths, and weaknesses."
)

# Define Pitch Deck Generator Agent
pitch_agent = Agent(
    name="Pitch Deck Generator",
    role="Generate pitch deck summary.",
    goal="Create a concise pitch deck using the market and competitor data."
)

# Function to run CrewAI workflow
def evaluate_startup(idea):
    # Create Crew with all agents
    crew = Crew(agents=[market_agent, competitor_agent, pitch_agent])
    
    # Step 1: Market research
    market = market_agent.run(f"Do market research for this startup idea: {idea}")
    
    # Step 2: Competitor analysis
    competitors = competitor_agent.run(f"Identify competitors for this startup idea: {idea}")
    
    # Step 3: Pitch deck summary
    pitch = pitch_agent.run(
        f"Generate a pitch deck for this startup idea: {idea}\n"
        f"Market info: {market}\nCompetitor info: {competitors}"
    )
    
    return market, competitors, pitch
