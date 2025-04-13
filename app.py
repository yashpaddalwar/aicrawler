import requests
from bs4 import BeautifulSoup
from langchain.llms import OpenAI

def crawl_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text()
    return text

def summarize_text(text):
    llm = OpenAI(temperature=0, model_name="text-davinci-003")
    summary = llm(f"Summarize this text: {text}")
    return summary

if __name__ == "__main__":
    url = "https://www.example.com"
    text = crawl_website(url)
    summary = summarize_text(text)
    print(summary)
