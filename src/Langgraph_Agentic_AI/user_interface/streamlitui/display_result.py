import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase= usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase= self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase =="Basic Chatbot":
                for event in graph.stream({'messages':("user",user_message)}):
                    print(event.values())
                    for value in event.values():
                        print(value['messages'])
                        with st.chat_message("user"):
                            st.write(user_message)
                        with st.chat_message("assistant"):
                            st.write(value["messages"].content)

        elif usecase=="Chatbot with Tool":
             # Prepare state and invoke the graph
            initial_state = {"messages": [user_message]}
            with st.chat_message("user"):
                st.write(user_message)
            for event in graph.stream(initial_state):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    for message in value['messages']:
                        if type(message) == HumanMessage:
                            continue
                        if type(message)==ToolMessage:
                            with st.chat_message("ai"):
                                st.write("Tool Call Start")
                                st.write(message.content)
                                st.write("Tool Call End")
                        elif type(message)==AIMessage and message.content:
                            with st.chat_message("assistant"):
                                st.write(message.content)