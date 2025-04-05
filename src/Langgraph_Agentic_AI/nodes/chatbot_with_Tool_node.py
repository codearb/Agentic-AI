from src.Langgraph_Agentic_AI.state.state import State

class ChatbotWithToolNode:
    """
    A class representing a chatbot node that can interact with tools.
    """

    def __init__(self, model):
        self.llm = model

    def process(self, state: State) -> dict:
        """
        Process the state and return the response from the model with tools.
        """
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.model.invoke([{"role": "user", "content": user_input}])

        # Simulate tool-specific logic
        tools_response = f"Tool integration for: '{user_input}'"

        return {"messages": [llm_response, tools_response]}
    
    def create_chatbot(self, tools):
        """
        Returns a chatbot node function.
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        return chatbot_node