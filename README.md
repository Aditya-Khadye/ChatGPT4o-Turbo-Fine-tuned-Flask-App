# Finetuned GPT4o-Turbo GenAI Assistant

### Author: Aditya Khadye  
**Date**: January 22, 2025  

---

## Project Overview

The ** Personalized AI Assistant** is a chatbot application designed to interact with users by providing intelligent, context-aware responses. This project is implemented with a Flask backend, a responsive frontend, and an integrated SQLite database for storing chat history. The assistant also supports mock or customizable AI responses, with an optional feature for using fine-tuned training data. Being prior author, Aditya Khadye, Asim Ilter, Atahan Gozet, First Version 1.0, provided to Dr. Xudong Liu. This version is significantly, optimized by upto 50% reduction in code and memory requirements. Also made it modular for future integration.

---

## Key Features

1. **Interactive Chatbot**:
   - Accepts user input via a web interface and provides responses in real-time.
   - Option to customize responses using a JSONL-based training dataset.

2. **Chat History**:
   - Stores user prompts and chatbot responses in an SQLite database.
   - Retrieves and displays past conversations for better user experience.

3. **Responsive Frontend**:
   - Clean and user-friendly interface designed with HTML, CSS, and JavaScript.
   - Real-time interaction without requiring page reloads.

4. **Extensible Backend**:
   - Flask-based RESTful API for seamless communication between frontend and backend.
   - Modular design to integrate external AI models or APIs.

---

## Technologies Used

- **Backend**: Flask, Flask-CORS, Flask-SQLAlchemy
- **Frontend**: HTML5, CSS3, JavaScript (ES6)
- **Database**: SQLite
- **Optional Training Data**: JSONL format for fine-tuning responses

---

## Project Structure

```
Finetuned-AI-Assistant/
├── server.py               # Flask backend with routes for chat and database management
├── templates/
│   └── index.html          # Main HTML interface
├── static/
│   ├── script.js           # Frontend JavaScript for chat interactions
│   ├── styles.css          # CSS for UI styling
├── chat_history.db         # SQLite database storing chat history
├── trainingData.jsonl      # JSONL file for optional fine-tuned training data
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Setup Instructions

### 1. Prerequisites
- Python 3.7 or higher
- Pip (Python package manager)

### 2. Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Finetuned-AI-Assistant.git
   cd Finetuned-AI-Assistant
   ```

2. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # For macOS/Linux
   .\env\Scripts\activate   # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Ensure the SQLite database (`chat_history.db`) is initialized:
   ```bash
   python server.py
   ```

5. (Optional) Add or modify training data in `trainingData.jsonl` for custom responses.

---

## How to Run

1. Start the Flask server:
   ```bash
   python server.py
   ```

2. Open the application in your browser:
   ```
   http://127.0.0.1:5500
   ```

3. Interact with the chatbot:
   - Type a question or statement in the input box.
   - Click "Send" to receive a response.
   - View past conversations in the "Chat History" section.

---

## Endpoints

### GET `/`
- Serves the main HTML interface.

### POST `/get-chatgpt-response`
- **Description**: Processes user prompts and returns chatbot responses.
- **Input**: JSON object with `prompt` key.
- **Output**: JSON object with `response` key.

### POST `/save-chat`
- **Description**: Saves a conversation (prompt and response) to the SQLite database.
- **Input**: JSON object with `prompt` and `response` keys.
- **Output**: Success or error message.

### GET `/history`
- **Description**: Retrieves all saved conversations from the database.
- **Output**: JSON array of objects containing `prompt` and `response`.

---

## Customization

1. **Training Data**:
   - Modify or extend the `trainingData.jsonl` file to provide custom prompts and responses.

2. **Styling**:
   - Edit `styles.css` to change the appearance of the chatbot interface.

3. **Backend Logic**:
   - Enhance `server.py` to integrate with external AI APIs like OpenAI's GPT or Hugging Face.

---

## Sample Training Data

Below is an example of the `trainingData.jsonl` file:
```jsonl
{"prompt": "Hello", "completion": "Hi there! How can I assist you today?"}
{"prompt": "What is AI?", "completion": "AI stands for Artificial Intelligence, the simulation of human intelligence in machines."}
```

---

## Future Improvements

1. **AI Integration**:
   - Connect the backend to an external AI service for generating dynamic responses.

2. **User Authentication**:
   - Add login functionality to personalize chat history for individual users.

3. **Deployment**:
   - Deploy the application to AWS, Azure, or Heroku for public access.

4. **Mobile-Friendly Design**:
   - Optimize the frontend for better usability on mobile devices.

---

## Contribution Guidelines

Welcoming any contributions to improve the project. Please follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to your fork:
   ```bash
   git commit -m "Add new feature"
   git push origin feature-name
   ```
4. Submit a pull request for review.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
