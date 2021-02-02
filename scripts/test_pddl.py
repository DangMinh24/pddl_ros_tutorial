from lark import (
    Lark,
    Token,
    Tree,
    Visitor
)

from pddl_parser.pddl_parser import (
    pddl_grammar_str
)


def get_atomic_name_formula(state):
    if (isinstance(state, Token)):
        return []
    if (isinstance(state, Tree) and (state.data == "predicate" or state.data == "predicate_argument")):
        return [state]
    elif (isinstance(state, Tree)):
        children = []

        for child in state.children:
            child_result = get_atomic_name_formula(child)
            if (isinstance(child_result, list) and child_result != []):
                children.append(child_result)

        if (state.data == "atomic_name_formula"):
            new_children = []
            first_child = children[0][0]
            predicate = "".join(get_leaves(first_child))
            arguments = []
            for child_element in children[1:]:
                child_result = child_element[0]
                child_result_str = "".join(get_leaves(child_result))
                arguments.append(child_result_str)
            new_children.append((predicate, arguments))
            return new_children
        else:
            return children


def get_init(state):
    if (isinstance(state, Token)):
        return []
    elif (isinstance(state, Tree) and state.data == "init"):
        return [state]

    if (isinstance(state, Tree)):
        children = []
        for child in state.children:
            child_result = get_init(child)
            if (isinstance(child_result, list)):
                children.extend(child_result)
        return children


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


def preprocessing_predicate_header(predicate_header):
    result_predicate_header = predicate_header.replace("-", "_")
    result_predicate_header = result_predicate_header[0].capitalize(
    ) + result_predicate_header[1:]
    return result_predicate_header


def create_expression(predicate, arguments):
    expression = ""
    expression += predicate
    expression += "("
    expression += arguments[0]
    if len(arguments) > 1:
        for argument in arguments[1:]:
            expression += ", {}".format(argument)

    expression += ")"

    return expression


class GetFormulas(Visitor):
    def __init__(self):
        self._formulas = []
        self._atomic_name_formula = []
        self._predicate_arguments = []
        self._predicate_header = []

    def predicate_argument(self, tree):
        data = "".join(get_leaves(tree))
        tree._shared_data = data
        self._predicate_arguments.append(data)

    def predicate(self, tree):
        data = "".join(get_leaves(tree))
        data = preprocessing_predicate_header(data)
        tree._shared_data = data
        self._predicate_header.append(data)

    def atomic_name_formula(self, tree):
        children = []
        for child in tree.children:
            child_result = child._shared_data
            children.append(child_result)

        predicate_header = children[0]
        arguments = children[1:]

        expression = create_expression(predicate_header, arguments)
        self._formulas.append(expression)


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

    visitor = GetFormulas()
    visitor.visit(result)

    init_state = visitor._formulas
    print(init_state)