# AI Learning Path Creator 

An intelligent learning path generator built with CrewAI and GPT-4 that creates personalized educational content for any topic. Perfect for self-learners and educators looking to create structured learning experiences.

## Features 

- **Personalized Learning Paths**: Generate custom learning paths for any topic
- **Adaptive Content**: Adjusts to user's skill level and time commitment
- **Comprehensive Modules**: Daily structured content with learning objectives and examples
- **Interactive Quizzes**: Test understanding with end-of-chapter assessments
- **Progress Tracking**: Monitor learning progress through milestones

## Tech Stack 

- Backend: FastAPI
- Frontend: Streamlit
- AI Framework: CrewAI
- Language Model: GPT-4
- Python 3.9+

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

4. Create a `.env` file in the root directory and add your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

## Project Structure 

```
personalized-learning-instructor/
├── .env                    # Environment variables
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies
├── src/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py    # Pydantic models
│   ├── crew/
│   │   ├── __init__.py
│   │   ├── agents.py     # CrewAI agents
│   │   └── tasks.py      # CrewAI tasks
│   └── api/
│       ├── __init__.py
│       └── routes.py     # API routes
└── frontend/
    └── app.py            # Streamlit frontend
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

3. Open your browser and navigate to `http://localhost:8501`

4. Enter your learning preferences:
   - Topic(s) you want to learn
   - Current skill level
   - Time commitment
   - Desired content complexity

## How It Works 

The application uses two specialized AI agents:

1. **Course Designer Agent**: 
   - Structures the overall learning journey
   - Creates logical progression of topics
   - Determines appropriate pacing

2. **Content Generator Agent**: 
   - Creates detailed educational content
   - Generates examples and exercises
   - Develops assessment questions

These agents collaborate to create a comprehensive learning experience tailored to the user's needs.

## API Endpoints 

- `POST /api/learning-path`: Generate a new learning path
- `POST /api/chapter/{day}`: Generate detailed content for a specific day
- `GET /health`: Check API health

## Contributing 

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

