# app.py
import gradio as gr

def rag_chatbot(query):
    # Dummy logic — simulate RAG response
    if "account" in query.lower():
        return "You can create an account by visiting the Angel One sign-up page."
    else:
        return "I Don't know"

iface = gr.Interface(fn=rag_chatbot,
                     inputs=gr.Textbox(placeholder="Ask your support question here..."),
                     outputs="text",
                     title="Angel One Support Chatbot",
                     description="Ask anything related to Angel One support. (RAG logic placeholder)"
                     )

if __name__ == "__main__":
    iface.launch()
