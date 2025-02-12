# Q&A ChatBot Application

## 🚀 Project Overview
This is an AI-powered chatbot application built with **LangChain**, **Streamlit**, and the **Groq model** for answering user queries. The app leverages a conversational AI model to provide meaningful and helpful answers based on user input. The user interface is designed for simplicity and ease of use.

## ✨ Features
- Interactive chatbot interface to ask any question
- Support for various Groq language models
- Customizable parameters for **temperature** and **max tokens**
- Sidebar settings for API key management and model selection
- Clean and responsive UI with custom styling

## 🛠️ Technologies Used
- **LangChain**: For building the chatbot with language models
- **Streamlit**: To create a user-friendly web interface
- **Groq Models**: AI models for natural language understanding
- **dotenv**: For environment variable management

## 📁 Project Structure
```
project-folder/
├── app.py              # Main application file
├── .env                 # Environment variables (not shared)
├── requirements.txt     # Required Python libraries
└── README.md            # Project documentation
```

## 🧑‍💻 How to Run the Application Locally
### Prerequisites
- Python 3.8+
- Git installed

### Installation Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Zaheerkhn/Q-A-ChatBot.git
   cd Q-A-ChatBot

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables:**
   Create a `.env` file in the project root:
   ```env
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGCHAIN_PROJECT=your_project_name
   GROQ_API_KEY=your_groq_api_key
   ```

5. **Run the application:**
   ```bash
   streamlit run app.py
   ```

6. **Access the application:**
   Open [http://localhost:8501](http://localhost:8501) in your browser.

## 🌐 Deployment on Streamlit Cloud
1. Push your code to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository and deploy the app.
4. Set environment variables in Streamlit's Secrets section.

## 🔧 Customization Options
- Modify the prompt template for specific responses
- Change model settings in the sidebar
- Adjust temperature and max token values for diverse results

## ⚠️ Important Notes
- Do **not** upload the `.env` file to GitHub to protect sensitive information.
- Set API keys securely in Streamlit Secrets or `.env` files.

## 📜 License
This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.


## 💡 Acknowledgments
- [LangChain](https://www.langchain.com)
- [Streamlit](https://streamlit.io)
- [Groq](https://groq.com)




