from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from langchain_groq import ChatGroq
from prompts import *
from states import *
from tools import *

llm = ChatGroq(model="llama-3.3-70b-versatile")

planner = llm.with_structured_output(Plan)

architect = llm.with_structured_output(ImplementationPlan)

coder = create_agent(
    model="groq:llama-3.3-70b-versatile",
    tools=[write_file, read_file, get_current_directory, list_files, run_cmd],
)


if __name__ == "__main__":

    # resp = planner.invoke(planner_prompt(user_prompt))
    res = architect.invoke(architect_prompt("""
    name='SimpleWebCalculator', 
    description='A simple web calculator that performs basic arithmetic operations', 
    techstack='HTML, CSS, JavaScript', 
    features=['Addition, subtraction, multiplication, and division', 'Clear entry and reset functionality', 'Responsive design for desktop and mobile', 'Keyboard input support', 'Display of current input and result'], 
    files=[File(path='index.html', purpose='HTML structure of the calculator UI'), File(path='style.css', purpose='Styling for a clean, responsive calculator layout'), File(path='script.js', purpose='JavaScript logic handling button clicks, calculations, and keyboard input')]
    """))
    print(res)
