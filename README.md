# Article Explainer - Multi-Agent Research Paper Assistant

An intelligent document analysis system that uses a swarm of specialized AI agents to help you understand complex research papers. Built with LangGraph's swarm architecture, agents dynamically delegate work to each other based on what you need.

## Overview

Upload a research paper and ask questions. The system routes your query to the most appropriate agent, and agents hand off to each other as needed:

- **Developer**: Writes code examples demonstrating concepts
- **Explainer**: Breaks down complex ideas step-by-step
- **Analogy Creator**: Translates technical concepts into relatable metaphors
- **Summarizer**: Distills information into key takeaways
- **Vulnerability Expert**: Critiques methodology and identifies weaknesses

## Architecture

This project demonstrates the **swarm pattern** in multi-agent systems. Unlike supervisor patterns where one agent controls others, agents in a swarm delegate work between themselves:

```
User asks about transformer architecture
    ↓
Developer writes attention code
    ↓ (realizes math unclear)
Explainer breaks down formula
    ↓ (still abstract)
Analogy Creator explains with metaphor
    ↓ (user asks about weaknesses)
Vulnerability Expert critiques approach
```

Each agent decides who should handle the next part of the conversation.

## Features

- **PDF Upload & Processing**: Extract text from research papers
- **Interactive Chat Interface**: Ask questions in natural language
- **Dynamic Agent Coordination**: Agents hand off control based on context
- **Persistent Conversation**: Maintains state across multiple interactions
- **PDF Viewer**: View your document alongside the chat

## Prerequisites

- Python 3.10+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd article-explainer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or if you have `uv`:
```bash
uv sync
```

3. Set up environment variables:
```bash
export OPENAI_API_KEY="your-api-key-here"
```

## Project Structure

```
.
├── explainer/
│   ├── graph.py              # Swarm graph setup and agent definitions
│   ├── prompts.py            # System prompts for each agent
│   └── service/
│       ├── config.py         # Model configuration
│       └── content_loader.py # PDF processing
├── article_explainer_page.py # Streamlit web interface
├── requirements.txt          # Python dependencies
└── README.md
```

## Usage

### Web Interface

Launch the Streamlit application:

```bash
streamlit run article_explainer_page.py
```

Or with `uv`:

```bash
uv run streamlit run article_explainer_page.py
```

Open your browser at `http://localhost:8501`

### Docker

Build and run with Docker:

```bash
docker build -t article_explainer .
docker compose up -d
```

Access at `http://localhost:8501`

## How It Works

### Agent Coordination

Each agent has **handoff tools** that allow them to transfer control:

```python
transfer_to_developer = create_handoff_tool(
    agent_name="developer",
    description="Tool to hand control to the Developer for code examples..."
)
```

When an agent calls a handoff tool:
1. Full conversation history is passed
2. The active agent is updated
3. The new agent takes over the conversation

### Memory Management

The system uses LangGraph's `InMemorySaver` to:
- Track which agent is currently active
- Maintain conversation history across turns
- Enable seamless agent handoffs

### Example Queries

**Getting Started:**
- "Summarize this paper"
- "What are the key contributions?"

**Deep Dive:**
- "Explain the methodology in detail"
- "What are the most complex concepts?"

**Code Examples:**
- "Show me code implementing the main algorithm"
- "Provide code samples for the key techniques"

**Critical Analysis:**
- "Are there any weaknesses in this approach?"
- "What assumptions does this research make?"

**Making It Accessible:**
- "Explain this using analogies"
- "Break down the most technical parts"

## Customization

### Adding New Agents

1. Define the agent's system prompt in `prompts.py`:
```python
NEW_AGENT_SYSTEM_PROMPT = """
You are the [agent name].
Goal: [what this agent does]
...
"""
```

2. Create handoff tools in `graph.py`:
```python
transfer_to_new_agent = create_handoff_tool(
    agent_name="new_agent",
    description="When to transfer to this agent..."
)
```

3. Create the agent and add to swarm:
```python
new_agent = create_react_agent(
    model,
    prompt=NEW_AGENT_SYSTEM_PROMPT,
    tools=[...handoff_tools...],
    name="new_agent",
)

agent_swarm = create_swarm(
    [developer, summarizer, explainer, analogy_creator, 
     vulnerability_expert, new_agent],
    default_active_agent="explainer",
)
```

### Modifying Agent Behavior

Edit the system prompts in `explainer/prompts.py` to change:
- Agent goals and instructions
- When agents should hand off to others
- Output format and style

### Changing the LLM Model

Update `explainer/service/config.py`:
```python
def get_chat_model():
    return ChatOpenAI(model="gpt-4o", temperature=0.7)
```

## Technical Details

### Swarm Pattern vs Supervisor Pattern

**Supervisor Pattern:**
- One agent calls others as tools
- Centralized control
- Good for predictable workflows

**Swarm Pattern:**
- Agents delegate to each other
- Decentralized control
- Better for unpredictable conversations

This project uses the swarm pattern because explaining research papers requires different expertise at unpredictable moments.

### Key Dependencies

- `langgraph`: Graph-based agent orchestration
- `langgraph-swarm`: Swarm architecture implementation
- `langchain-openai`: OpenAI model integration
- `streamlit`: Web interface
- `pypdf`: PDF text extraction
- `streamlit-pdf-viewer`: In-app PDF viewing

## Troubleshooting

**Agent not responding:**
- Check your OpenAI API key is set correctly
- Verify the API key has sufficient credits

**PDF processing fails:**
- Ensure the PDF contains extractable text (not scanned images)
- Try a different PDF or reduce the `max_chunks` parameter

**Agents not handing off:**
- Check handoff tool descriptions are clear
- Review agent system prompts for handoff instructions

## References

- [LangGraph Swarm Documentation](https://langchain-ai.github.io/langgraph/agents/multi-agent/#swarm)
- [Swarm Architecture Article](https://medium.com/@caldasdcardoso/swarm-architecture-agents-in-langgraph-b8b1b53c61b3)
- [Original Implementation](https://github.com/duartecaldascardoso/article-explainer)

## Contributing

Contributions are welcome! Areas for improvement:
- Additional specialized agents
- Better PDF processing for complex layouts
- Support for other document formats
- Enhanced memory and context management

## License

[Add your license here]

## Author

[Add your information here]

## Acknowledgments

Inspired by the article explainer project by Duarte Caldas Cardoso and LangGraph's swarm architecture pattern.
