from llama_index.core.chat_engine import SimpleChatEngine
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.tools import FunctionTool

from lib.agent.tools import deploy_contract, transfer, get_account_balance


deployer_tool = FunctionTool.from_defaults(fn=deploy_contract)
transfer_tool = FunctionTool.from_defaults(fn=transfer)
get_account_balance_tool = FunctionTool.from_defaults(fn=get_account_balance)

tools = [deployer_tool, transfer_tool, get_account_balance_tool]
agent = OpenAIAgent.from_tools(tools, verbose=True)

def get_agent():
    return agent

