from lark import (
    Lark,
    Token,
    Tree
)

from pddl_parser.pddl_parser import (
    pddl_grammar_str
)


def get_init(state):
    if (isinstance(state, Token)):
        return []
    elif (isinstance(state, Tree) and state.data == "init"):
        print(state.data)
        return [state]

    elif (isinstance(state, Tree)):
        children = []
        for child in state.children:
            child_result = get_init(child)
            if (isinstance(child_result, list)):
                children.extend(child_result)
        return child_result


def get_list_of_objects_str(state):
    objects_state = get_objects(state)
    if (len(objects_state) == 0):
        return []
    else:
        NAMES = get_NAMES(objects_state[0])
        return NAMES


def get_NAMES(state):
    if (isinstance(state, Token) and state.type == "NAME"):
        return [state.value]
    elif (isinstance(state, Token)):
        return []

    else:
        children = []
        for child in state.children:
            child_result = get_NAMES(child)
            if (isinstance(child_result, list)):
                children.extend(child_result)
        return children


def get_objects(state):
    if (isinstance(state, Token)):
        return []
    elif (isinstance(state, Tree) and state.data == "object_decl"):
        return [state]
    else:
        children = []
        for child in state.children:
            child_result = get_objects(child)
            if (isinstance(child_result, list)):
                children.extend(child_result)
        return children


def get_leaves(state):
    if (isinstance(state, Token)):
        return [state.value]

    else:
        children = []
        for child in state.children:
            child_result = get_leaves(child)

            if (isinstance(child_result, list)):
                children.extend(child_result)
            elif (isinstance(child_result, str)):
                children.append(child_result)

        return children


if __name__ == "__main__":
    input_ = """
        (define (domain gripper-strips)
        (:predicates (room ?r)
                (ball ?b)
                (gripper ?g)
                (at-robby ?r)
                (at ?b ?r)
                (free ?g)
                (carry ?o ?g))

        (:action move
            :parameters  (?from ?to)
            :precondition (and  (room ?from) (room ?to) (at-robby ?from))
            :effect (and  (at-robby ?to)
                    (not (at-robby ?from))))



        (:action pick
            :parameters (?obj ?room ?gripper)
            :precondition  (and  (ball ?obj) (room ?room) (gripper ?gripper)
                        (at ?obj ?room) (at-robby ?room) (free ?gripper))
            :effect (and (carry ?obj ?gripper)
                    (not (at ?obj ?room))
                    (not (free ?gripper))))


        (:action drop
            :parameters  (?obj  ?room ?gripper)
            :precondition  (and  (ball ?obj) (room ?room) (gripper ?gripper)
                        (carry ?obj ?gripper) (at-robby ?room))
            :effect (and (at ?obj ?room)
                    (free ?gripper)
                    (not (carry ?obj ?gripper)))))
    """

    input_ = """
        (define (problem strips-gripper-x-1)
        (:domain gripper-strips)
        (:objects rooma roomb ball4 ball3 ball2 ball1 left right)
        (:init (room rooma)
                (room roomb)
                (ball ball4)
                (ball ball3)
                (ball ball2)
                (ball ball1)
                (at-robby rooma)
                (free left)
                (free right)
                (at ball4 rooma)
                (at ball3 rooma)
                (at ball2 rooma)
                (at ball1 rooma)
                (gripper left)
                (gripper right))
        (:goal (and (at ball4 roomb)
                    (at ball3 roomb)
                    (at ball2 roomb)
                    (at ball1 roomb))))
    """

    parser = Lark(pddl_grammar_str, start="pddl_doc")

    result = parser.parse(input_)

    leaves = get_leaves(result)
    # print(leaves)

    objects = get_objects(result)
    # print(objects)

    NAMES = get_list_of_objects_str(result)
    domain = set(NAMES)
    print (domain)

    actions = []
    state = []

    init_state = get_init(result)
    print(len(init_state))
