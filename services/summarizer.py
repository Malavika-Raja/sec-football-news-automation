import os
from openai import OpenAI
from config import OPENAI_API_KEY
import openai

client =openai.OpenAI(api_key=OPENAI_API_KEY)

def generate_summary(text):
  response = client.chat.completions.create(
      model = "gpt-4o-mini",
      messages =[
          {
              "role":"system",
              "content":"You are a sports analyst summarizing weekly SEC football news"
          },
          {
              "role":"user",
              "content":f"Summarize the following SEC college football news into a concise weekly report(2-3 elaborate paragraphs, covering all important details):\n{text}"
          }
      ],
      temperature=0.6,
  )
  return response.choices[0].message.content