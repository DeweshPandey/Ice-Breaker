# ICE BREAKER

## 🚀 Project Overview
ICE BREAKER is a web application designed to generate insightful summaries and interesting facts about individuals based on their LinkedIn and Twitter profiles. By simply entering a name, users can gain a quick overview enriched with social media data, including a profile picture and two intersecting facts.

## 🛠️ Tech Stack
- **Python**: Core backend logic
- **Flask**: Web framework for building the webpage
- **LangChain**: Framework for integrating LLMs (Large Language Models)
- **OpenAI GPT-3.5-turbo**: LLM used for generating summaries and insights
- **Proxycurl API**: For scraping LinkedIn profile data
- **Twitter API**: For fetching recent tweets
- **Tavily Search API**: For searching LinkedIn and Twitter profiles
- **Pydantic Output Parser**: Ensures structured and readable output
- **HTML**: For building the user interface

## 📊 Project Workflow
1. User enters a name on the web interface.
2. The **Tavily Search API** identifies LinkedIn and Twitter profiles.
3. Data is scraped using **Proxycurl API** (LinkedIn) and **Twitter API** (Tweets).
4. Information is passed to **LangChain**, which utilizes OpenAI's LLM to generate:
   - A short summary of the individual.
   - Two interesting facts derived from both platforms.
5. The result, along with the LinkedIn profile picture, is displayed on the webpage.

## 🧩 Key Features
- Dynamic profile lookup using ReAct agents.
- Integration with LinkedIn and Twitter APIs.
- Structured and readable outputs with **Pydantic Output Parser**.
- User-friendly Flask web interface.

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ice-breaker.git
   cd ice-breaker
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   PROXYCURL_API_KEY=your_proxycurl_api_key
   TWITTER_API_KEY=your_twitter_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open the application in your browser:
   ```
   http://127.0.0.1:5000
   ```

## 📑 Usage
1. Open the web interface.
2. Enter the name of the person you want to search.
3. Click the **"Get Information"** button.
4. View the summary, interesting facts, and profile picture.

## 🛡️ Environment Variables
- `OPENAI_API_KEY`
- `PROXYCURL_API_KEY`
- `TWITTER_API_KEY`
- `TAVILY_API_KEY`

## 🤝 Contributing
Contributions are welcome! Please fork the repository and create a pull request.

## 📄 License
This project is licensed under the MIT License.

## 📬 Contact
For inquiries or feedback, reach out at [your.email@example.com](mailto:your.email@example.com).

---

**ICE BREAKER** – Your quick insight generator powered by LLMs and social intelligence APIs.

