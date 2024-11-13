from langchain_groq import ChatGroq

model = ChatGroq(model='llama-3.1-70b-versatile',api_key='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')

#query = 'what is the largest planet ?'
query = str(input("What would you like to prompt?"))
result = model.invoke(query)
print(result.content)