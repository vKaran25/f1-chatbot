# 🏎️ F1 Chatbot  

**Status:** 🚧 Work in Progress  

This is an **F1-themed chatbot** that generates **banter and jokes** inspired by Formula 1 culture.  
It will be trained on **Reddit meme page data** (e.g., r/formuladank, r/F1Memes) and fine-tuned on a **Large Language Model (LLM)** to produce creative, witty, and context-aware responses.  

---

## 📌 Project Goals  

- Scrape **F1 meme data** from Reddit (images + post text).  
- **Clean & preprocess** the scraped content.  
- **Fine-tune** a chatbot model (LLM) on the curated dataset.  
- Make the bot capable of **Formula 1 banter** and quick-witted jokes.  

---

## 🔧 Current Features  

- ✅ **Reddit Scraper** for F1 meme pages (old.reddit.com for easier parsing).  
- ✅ Extracts:
  - Post **titles** (meme captions / banter text).  
  - **Image links** from meme posts.  
- ✅ Saves images locally and stores metadata in `posts.json`.  
- ✅ Works with **Selenium + BeautifulSoup** for dynamic page scraping.  

---

## 🚀 Planned Features  

- ⏳ Add **scrolling & pagination** to scrape more than just the first page.  
- ⏳ Handle **image-text association** for training.  
- ⏳ **Fine-tune** a GPT-like model on collected F1 banter data.  
- ⏳ Deploy chatbot with **Streamlit / Django** web interface.  
- ⏳ Optional: Meme generation based on user prompts.  

---

## 🛠️ Tech Stack  

- **Python** (Main language)  
- **Selenium** (Web scraping automation)  
- **BeautifulSoup** (HTML parsing)  
- **Requests** (Image downloading)  
- **Streamlit** (Prototype web interface)  
- **LangChain** (Planned integration for LLM pipeline)  

---

(current steps to run it locally)
1. install the requirement in 'requirements.txt' file - pip install -r requirements.txt
2. run command on terminal 'streamlit run main.py'
  

