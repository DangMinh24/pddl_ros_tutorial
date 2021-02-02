
from lark import (
    Token, Tree
)


def extract_method(state):
    if (isinstance(state, Token)):
        return []
    elif (isinstance(state, Tree) and state.data == "method_def"):
        return [state]
    elif (isinstance(state, Tree)):
        children = []
        for child in state.children:
            child_result = extract_method(child)
            if (isinstance(child_result, list)):
                children.extend(child_result)
            else:
                raise ValueError("{} -- is not a list".format(child_result))
        return children


def get_tasknetwork(state):
    if (isinstance(state, Token)):
        return []
    elif (isinstance(state, Tree) and state.data == "tasknetwork_def"):
        return [state]
    elif (isinstance(state, Tree)):
        children = []
        for child in state.children:
            child_result = get_tasknetwork(child)
            if (isinstance(child_result, list)):
                children.extend(child_result)
            else:
                raise ValueError("{} -- is not a list".format(child_result))
        return children


def get_subtask_defs(state):
    if (isinstance(state, Token)):
        return []
    elif (isinstance(state, Tree) and state.data == "subtask_defs"):
        return [state]
    elif (isinstance(state, Tree)):
        children = []
        for child in state.children:
            child_result = get_subtask_defs(child)
            if (isinstance(child_result, list)):
                children.extend(child_result)
            else:
                raise ValueError("{} -- is not a list".format(child_result))
        return children


def get_subtask_def(state):
    if (isinstance(state, Token)):
        return []
    elif (isinstance(state, Tree) and state.data == "subtask_def"):
        return [state]
    elif (isinstance(state, Tree)):
        children = []
        for child in state.children:
            child_result = get_subtask_def(child)
            if (isinstance(child_result, list)):
                children.extend(child_result)
            else:
                raise ValueError("{} -- is not a list".format(child_result))
        return children


def get_task_symbol(state):
    if (isinstance(state, Token)):
        return []
    elif (isinstance(state, Tree) and state.data == "task_symbol"):
        return [state]
    elif (isinstance(state, Tree)):
        children = []
        for child in state.children:
            child_result = get_task_symbol(child)
            if (isinstance(child_result, list)):
                children.extend(child_result)
            else:
                raise ValueError("{} -- is not a list".format(child_result))
        return children


def get_leaves(state):
    if (isinstance(state, Token)):
        return [state.value]
    elif(isinstance(state, Tree)):
        children = []
        for child in state.children:
            child_result = get_leaves(child)
            if isinstance(child_result, list):
                children.extend(child_result)
            elif (isinstance(child_result, str)):
                children.append(child_result)

        return children
