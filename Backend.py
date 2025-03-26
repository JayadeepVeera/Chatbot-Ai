import os
import google.generativeai as genai
genai.configure(api_key="AIzaSyBkSSyIjxl0qFd6b4Z1u1ZxX7KX11WuP88")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)
def GenerativeResponse(input_text):
   response = model.generate_content([
  "input: hello",
  "output: hi , im a chatbot",
  f"input:{input_text}",
  "output: ",
  ])
   return response.text

   
#while True:
  # string=str(input("enter your prompt:"))
   #print("Bot:" ,GenerativeResponse(string))
   
