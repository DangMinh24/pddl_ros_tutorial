""" 
Grammar is based on:
    Pddl.g4: https://github.com/antlr/grammars-v4/blob/master/pddl/Pddl.g4
    PDDL -- Planning Domain Definition Language Version 1.2: https://homepages.inf.ed.ac.uk/mfourman/tools/propplan/pddl.pdf 
"""

from lark import Lark
pddl_grammar_str = """
pddl_doc : domain 
    | problem
domain: "(" "define" domain_name require_def? types_def? constants_def? predicates_def? functions_def? constraints? structure_def* ")"

domain_name: "(" "domain" NAME ")"

require_def: "(" ":requirements" REQUIRE_KEY+ ")"

types_def: "(" ":types" typed_name_list ")"

typed_name_list: (NAME* | single_type_name_list+ NAME* )

single_type_name_list: (NAME+ "-" type)

type: prim_type

prim_type: NAME

functions_def: "(" ":functions" function_list ")"

function_list: ( atomic_function_skeleton+ ("-" function_type)? )*

atomic_function_skeleton: "(" function_symbol typed_variable_list ")"

function_symbol: NAME

function_type: "number"

constants_def: "(" ":constants" typed_name_list ")"

predicates_def: "(" ":predicates" atomic_formula_skeleton+ ")"

atomic_formula_skeleton: "(" predicate typed_variable_list ")"

predicate: NAME

typed_variable_list: (VARIABLE* |single_type_var_list+ VARIABLE*)

single_type_var_list: (VARIABLE+ "-" type )

constraints: "(" ":constraints"  con_gd ")"

structure_def: action_def 
    | durative_action_def 
    | derived_def

action_def: "(" ":action" action_symbol ":parameters" "(" typed_variable_list ")" action_def_body ")"

action_symbol: NAME

action_def_body: ( ":precondition" (("(" ")" ) | goal_desc) )? (":effect" (("(" ")" ) | effect))?


goal_desc: atomic_term_formula 
    | "(" "and" goal_desc* ")" 
    | "(" "or" goal_desc* ")" 
    | "(" "not" goal_desc ")" 
    | "(" "imply" goal_desc goal_desc ")" 
    | "(" "exists" "(" typed_variable_list ")" goal_desc ")" 
    | "(" "forall" "(" typed_variable_list ")" goal_desc ")" 
    | f_comp    

f_comp: "(" binary_comp f_exp f_exp ")"

atomic_term_formula: "(" predicate term* ")" 

term: NAME 
    | VARIABLE


durative_action_def: "(" ":durative-action" action_symbol ":parameters" "(" typed_variable_list ")" da_def_body ")"


da_def_body: ":duration" duration_constraint
    | ":condition" ( ( "("  ")" ) | da_gd)
    | ":effect" ( ( "(" ")") | da_effect )


da_gd: pref_timed_gd 
    | "(" "and" da_gd ")"
    | "(" "forall" "(" typed_variable_list ")" da_gd ")"


pref_timed_gd: timed_gd
    | "(" "preference" NAME? timed_gd ")"

timed_gd: "(" "at" time_specifier goal_desc ")"
    | "(" "over" interval  goal_desc ")"

time_specifier: "start" 
    | "end"

interval: "all"


derived_def: "(" ":derived" typed_variable_list goal_desc ")"


f_exp: NUMBER
    | "(" binary_op f_exp f_exp2 ")"
    | "(" "-" f_exp ")"
    | f_head


f_exp2: f_exp


f_head: "(" function_symbol term* ")"
    | function_symbol


effect: "(" "and" c_effect* ")"
    | c_effect

c_effect: "(" "forall" "(" typed_variable_list ")" effect ")"
    | "(" "when" goal_desc cond_effect ")"
    | p_effect

p_effect: "(" assign_op f_head f_exp ")"
    | "(" "not" atomic_term_formula ")"
    | atomic_term_formula


cond_effect: "(" "and" p_effect* ")"
    | p_effect


assign_op: "assign"
    | "scale-up"
    | "scale-down"
    | "increase"
    | "decrease"


simple_duration_constraint: "(" dur_op  "?duration" dur_value ")"
    | "(" "at" time_specifier simple_duration_constraint ")"

dur_op: "<=" 
    | ">=" 
    | "="

dur_value: NUMBER
    | f_exp



duration_constraint: "(" "and" simple_duration_constraint+ ")"
    | "(" ")"
    | simple_duration_constraint
    

da_effect: "(" "and" da_effect ")"
    | timed_effect 
    | "(" "forall" "(" typed_variable_list ")" da_effect ")"
    | "(" "when" da_gd timed_effect ")"
    | "(" assign_op f_head f_exp_da ")"

timed_effect: "(" "at" time_specifier da_effect ")"
    | "(" "at" time_specifier f_assign_da ")"
    | "(" assign_op f_head f_exp ")"

f_assign_da: "(" assign_op f_head f_exp_da ")"

f_exp_da: "(" (( binary_op f_exp_da f_exp_da ) | ("-" f_exp_da)) ")"
    | "?duration"
    | f_exp



problem: "(" "define" problem_decl problem_domain require_def? object_decl? init goal prob_constraints? metric_spec? ")"

problem_decl: "(" "problem" NAME ")"

problem_domain: "(" ":domain" NAME ")"

object_decl: "(" ":objects" typed_name_list ")"

init: "(" ":init" init_e1* ")"

init_e1: name_literal
    | "(" "=" f_head NUMBER ")" 
    | "(" "at" NUMBER name_literal ")"

name_literal: atomic_name_formula 
    | "(" "not" atomic_name_formula ")"


atomic_name_formula: "(" predicate predicate_argument* ")"

predicate_argument: NAME

goal: "(" ":goal" goal_desc ")"


prob_constraints: "(" ":constraints" pref_con_gd ")"

pref_con_gd: "(" "and" pref_con_gd ")"
    | "(" "forall" "(" typed_variable_list ")" pref_con_gd ")"
    | "(" "preference" NAME?  con_gd ")"
    | con_gd

metric_spec: "(" ":metric" optimization metric_f_exp ")"

optimization: "minimize"
    | "maximize"

metric_f_exp: "(" binary_op metric_f_exp metric_f_exp ")" 
    | "(" ( "*" | "/" ) metric_f_exp metric_f_exp+ ")" 
    | "(" "-" metric_f_exp ")" 
    | NUMBER 
    | "(" function_symbol NAME* ")" 
    | function_symbol 
    | "total-time" 
    | "(" "is-violated" NAME ")"

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



binary_comp: ">" | "<" | "=" | ">=" | "<="

binary_op: "*" 
    | "+"
    | "-"
    | "/"


   
NAME: LETTER+ ("_"|"-"|LETTER|DIGIT)*
VARIABLE: "?" LETTER ("_"|"-"|LETTER|DIGIT)*

%import common.LETTER
%import common.DIGIT
%import common.CNAME
%import common.NUMBER
%import common.WS
%ignore WS
"""
