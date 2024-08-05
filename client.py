from openai import OpenAI

client = OpenAI(

    api_key="sk-proj-hqmWpnBwmzTIsWufqbZYT3BlbkFJBku252bvSmbxLAaoUJ9C"
) 
completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are virtual assistant named jarvis skilled in general tasks like alexa and google cloud."},
    {"role": "user", "content": "what is coding."}
  ]
)

print(completion.choices[0].message.content)