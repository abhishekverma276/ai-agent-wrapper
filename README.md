# 🧠 AI Agent Creation API Wrapper

This FastAPI app exposes a single endpoint `/create-agent` that wraps around both [Vapi.ai](https://docs.vapi.ai/api-reference/assistants/create) and [Retell.ai](https://docs.retellai.com/api-references/create-agent).

## ✅ Features

- Unified request body
- Clean, modular code structure
- Uses environment variables for API keys

## 🛠 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/yourusername/ai-agent-wrapper.git
cd ai-agent-wrapper

# Create and activate virtual env
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from template
cp .env.example .env
# Add your actual API keys to the .env file

# Run the API
uvicorn app.main:app --reload
