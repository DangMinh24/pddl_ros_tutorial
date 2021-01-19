""" 
Grammar is based on:
    Pddl.g4: https://github.com/antlr/grammars-v4/blob/master/pddl/Pddl.g4
    PDDL -- Planning Domain Definition Language Version 1.2: https://homepages.inf.ed.ac.uk/mfourman/tools/propplan/pddl.pdf 
"""

from lark import Lark
pddl_grammar_str = """
pddl_doc : domain 
    | problem
domain: "(" "define" domain_name require_def? types_def? constants_def? predicates_def? functions_def? constraints? structure_def? ")"

problem: "(" "define" problem_decl problem_domain require_def? object_decl? init goal prob_constraints? metric_spec? ")"

problem_decl: "(" ":domain" NAME ")"

problem_domain: "(" ":domain" NAME ")"

goal: "(" ":goal" goal_desc ")"

object_decl: "(" ":objects" typed_name_list ")"

require_def: "(" ":requirements" REQUIRE_KEY+ ")"

prob_constraints: "(" ":constraints" pref_con_gd ")"

pref_con_gd: "(" "and" pref_con_gd ")"
    | "(" "forall" "(" typed_variable_list ")" pref_con_gd ")"
    | "(" "preference" NAME?  conGD ")"
    | conGD





types_def: "(" ":types" typed_name_list ")"

typed_name_list: NAME+

constants_def: "(" ":constants" typed_name_list ")"

predicates_def: "(" ":predicates" atomic_formula_skeleton ")"

atomic_formula_skeleton: "(" predicate  typed_variable_list ")"

predicate: NAME

typed_variable_list: VARIABLE+

functions_def: "(" ":functions" function_list ")"

function_list: atomic_function_skeleton

atomic_function_skeleton: "(" function_symbol typed_variable_list ")"

function_symbol: NAME

domain_name: "(" "domain" NAME ")"

constraints: "(" ":constraints"  con_gd ")"

structure_def: action_def 
    | durative_action_def 
    | derived_def

action_def: "(" ":action" action_symbol ":parameters" "(" typed_variable_list ")" action_def_body ")"

action_symbol: NAME

action_def_body: ":precondition"

con_gd: "(" "and" con_gd* ")" 
    | "(" "forall" "(" typed_variable_list ")" con_gd ")" 
    | "(" "at" "end" goal_desc ")" 
    | "(" "always" goal_desc ")" 
    | "(" "sometime" goal_desc ")" 
    | "(" "within" NUMBER goal_desc ")" 
    | "(" "at-most-once" goal_desc ")" 
    | "(" "sometime-after" goal_desc goal_desc ")" 
    | "(" "sometime-before" goal_desc goal_desc ")" 
    | "(" "always-within" NUMBER goal_desc goal_desc ")" 
    | "(" "hold-during" NUMBER NUMBER goal_desc ")" 
    | "(" "hold-after" NUMBER goal_desc ")"

goal_desc: atomic_term_formula 
    | "(" "and" goal_desc* ")" 
    | "(" "or" goal_desc* ")" 
    | "(" "not" goal_desc ")" 
    | "(" "imply" goal_desc goal_desc ")" 
    | "(" "exists" "(" typed_variable_list ")" goal_desc ")" 
    | "(" "forall" "(" typed_variable_list ")" goal_desc ")" 
    | f_comp    

atomic_term_formula: "(" predicate term* ")" 

f_comp: "(" binary_comp f_exp f_exp ")"

f_exp: NUMBER
    | "(" binary_op f_exp f_exp2 ")"
    | "(" "-" f_exp ")"
    | f_head

f_exp2: f_exp
f_head: "(" function_symbol term* ")"
    | function_symbol

binary_comp: ">" | "<" | "=" | ">=" | "<="

binary_op: "*" 
    | "+"
    | "-"
    | "/"

term: NAME 
    | VARIABLE



REQUIRE_KEY: ":strips" 
    | ":typing"
    | ":negative-preconditions" 
    | ":disjunctive-preconditions" 
    | ":equality" 
    | ":existential-preconditions" 
    | ":universal-preconditions" 
    | ":quantified-preconditions" 
    | ":conditional-effects" 
    | ":fluents" 
    | ":adl" 
    | ":durative-actions" 
    | ":derived-predicates" 
    | ":timed-initial-literals" 
    | ":preferences" 
    | ":constraints"
   
NAME: LETTER+
VARIALBE: "?" LETTER CNAME*

%import common.LETTER
%import common.CNAME
%import common.WS
%ignore WS
"""

parser = Lark(pddl_grammar_str, start="pddl_doc")
