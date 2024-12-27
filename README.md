# AI Learning Path Creator 

An intelligent learning path generator built with CrewAI that creates personalized, day-by-day learning paths for any topic. The system generates textbook-style content, complete with examples, quizzes, and daily milestones.

## Features 

- **Personalized Learning**: Adapts to your skill level and available time
- **Day-by-Day Structure**: One module per day, designed for 1-2 hours of focused learning
- **Rich Content**:
  - Detailed textbook-style explanations
  - Real-world examples
  - Interactive quizzes
  - Daily progress milestones
- **Flexible Time Frames**: From 1 week to 1 year
- **Adjustable Complexity**: Choose how technical or simplified you want the content

## Demo
https://substack.com/@shreyabhargava/note/p-153654935


## Tech Stack 

- **Backend**: FastAPI + CrewAI
- **Frontend**: Streamlit
- **AI Engine**: GPT-4 (via CrewAI)
- **Language**: Python 3.9+

## Installation 

1. Clone the repository:
```bash
git clone https://github.com/yourusername/learning-path-creator.git
cd learning-path-creator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Create a `.env` file in the root directory
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage 

1. Start the backend server:
```bash
uvicorn src.main:app --reload
```

2. In a new terminal, start the frontend:
```bash
streamlit run frontend/app.py
```

3. Open your browser and go to http://localhost:8501

4. Create your learning path:
   - Enter the topic(s) you want to learn
   - Select your current skill level
   - Choose your time commitment
   - Adjust the content complexity
   - Click "Create Learning Path"

## Project Structure 

```
learning-path-creator/
├── src/
│   ├── main.py           # FastAPI application
│   ├── models/
│   │   └── schemas.py    # Data models
│   └── crew/
│       ├── agents.py     # CrewAI agents
│       └── tasks.py      # CrewAI tasks
├── frontend/
│   └── app.py           # Streamlit interface
├── requirements.txt
└── README.md
```

## How It Works 

The system uses CrewAI to orchestrate specialized AI agents:
1. **Curriculum Designer**: Structures the overall learning journey
2. **Content Generator**: Creates detailed educational content
3. **Progress Tracker**: Designs milestones and assessments

These agents collaborate to create a comprehensive learning experience tailored to your needs.


## Acknowledgments 🙏

- [CrewAI](https://github.com/joaomdmoura/crewAI)
- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
