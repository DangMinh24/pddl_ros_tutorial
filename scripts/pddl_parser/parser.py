""" 
Grammar is based on:
    Pddl.g4: https://github.com/antlr/grammars-v4/blob/master/pddl/Pddl.g4
    PDDL -- Planning Domain Definition Language Version 1.2: https://homepages.inf.ed.ac.uk/mfourman/tools/propplan/pddl.pdf 
"""

from lark import Lark
pddl_grammar_str = """
pddl_doc : domain 
    | problem
domain: "(" "define" domain_name 
            require_def? 
            type_def? 
            constant_def?
            predicate_def?
            function_def
            constraints?
            structure_def?
        ")"
"""
