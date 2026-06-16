from langchain_core.globals import set_debug, set_verbose
from langgraph.graph import END, MessagesState, StateGraph
from nodes import *
from prompts import *
from states import CoderState

set_debug(True)
set_verbose(True)


def planner_node(state: dict):
    user_prompt = state["user_prompt"]
    plan = planner.invoke(planner_prompt(user_prompt))
    return {"plan": plan}


def architect_node(state: dict):
    plan = state["plan"]
    implementationplan = architect.invoke(architect_prompt(plan))
    return {"task_plan": implementationplan}


def coder_node(state: dict):
    coder_state: CoderState = state.get("coder_state")

    if coder_state is None:
        coder_state = CoderState(task_plan=state["task_plan"], current_step_index=0)

    steps = coder_state.task_plan.implementation_steps
    if coder_state.current_step_index >= len(steps):
        return {"coder_state": coder_state, "status": "DONE"}

    current_task = steps[coder_state.current_step_index]
    existing_content = read_file.run(current_task.filepath)

    USER_PROMPT = (
        f"Task: {current_task.description}\n"
        f"File: {current_task.filepath}\n"
        f"Existing content:\n{existing_content}\n"
        "Use write_file(path, content) to save your changes."
    )
    coder.invoke(
        {
            "messages": [
                {"role": "system", "content": coder_prompt()},
                {"role": "user", "content": USER_PROMPT},
            ]
        }
    )
    coder_state.current_step_index += 1

    return {"coder_state": coder_state}


graph = StateGraph(dict)

graph.add_node("planner", planner_node)
graph.set_entry_point("planner")
graph.add_node("architect", architect_node)
graph.add_node("coder", coder_node)
graph.add_edge("planner", "architect")
graph.add_edge("architect", "coder")
graph.add_conditional_edges(
    "coder",
    lambda state: END if state.get("status") == "DONE" else "coder",
    {END: END, "coder": "coder"},
)

agent = graph.compile()

agent.get_graph().draw_mermaid_png(output_file_path="agent.png")

agent.invoke(input={"user_prompt": "create a simple web calculator."})

# print(response)
