"""
Grammar is based on:
    antlrHDDL.g4: https://github.com/panda-planner-dev/pandaPIparser/blob/master/doc/antlrHDDL.g4
"""
from lark import Lark

hddl_grammar_str = """
hddl_file : domain | problem

domain : "(" "define" "(" "domain" domain_symbol ")" require_def? type_def? const_def? predicates_def? funtions_def? comp_task_def*  method_def*  action_def* ")"

domain_symbol : NAME

require_def : "(" ":requirements" require_defs ")"
require_defs : REQUIRE_NAME+

type_def : "(" ":types" type_def_list ")"
type_def_list : NAME* | (new_types "-" var_type type_def_list) 
new_types : NAME+


const_def : "(" ":constants" typed_obj_list ")" 

predicates_def : "(" ":predicates" atomic_formula_skeleton+ ")" 
atomic_formula_skeleton : "(" predicate typed_var_list ")" 

funtions_def : "(" ":functions" ( atomic_formula_skeleton ("-" "number" | var_type )?)+")" 

comp_task_def : "(" ":task" task_def 

task_def : task_symbol ":parameters" "(" typed_var_list ")" (":precondition" gd)? (":effect" effect)? ")" 

task_symbol : NAME 


method_def : "(" ":method" method_symbol ":parameters" "(" typed_var_list ")" ":task" "(" task_symbol var_or_const* ")" (":precondition" gd)? (":effect" effect)? tasknetwork_def 


tasknetwork_def : ((":subtasks" | ":tasks" | ":ordered-subtasks" | ":ordered-tasks") subtask_defs)? ((":ordering" | ":order") ordering_defs)? (":constraints" constraint_defs)? ((":causal-links" | ":causallinks") causallink_defs)? ")" 

method_symbol : NAME 

subtask_defs : "(" ")" | subtask_def | "(" "and" subtask_def+ ")" 
subtask_def : ("(" task_symbol var_or_const* ")" | "(" subtask_id "(" task_symbol var_or_const* ")" ")") 
subtask_id : NAME 


ordering_defs : "(" ")" | ordering_def | "(" "and" ordering_def+ ")" 
ordering_def : "(" subtask_id "<" subtask_id ")" 


constraint_defs : "(" ")" | constraint_def | "(" "and" constraint_def+ ")" 
constraint_def : "(" ")" | "(" "not" equallity var_or_const var_or_const")" ")" | equallity var_or_const var_or_const ")"
                 | "(" ("type" | "typeof" | "sort" | "sortof") typed_var ")"
                 | "(" "not" "(" ("type" | "typeof" | "sort" | "sortof") typed_var ")" ")"  

causallink_defs : "(" ")" | causallink_def | "(" "and" causallink_def+ ")" 
causallink_def : "(" subtask_id literal subtask_id ")" 

action_def : "(" ":action" task_def 

gd : gd_empty | atomic_formula | gd_negation | gd_implication | gd_conjuction | gd_disjuction | gd_existential | gd_universal | gd_equality_constraint
              | gd_ltl_at_end | gd_ltl_always | gd_ltl_sometime | gd_ltl_at_most_once | gd_ltl_sometime_after | gd_ltl_sometime_before
              | gd_preference 

gd_empty : "(" ")" 
gd_conjuction : "(" "and" gd+ ")" 
gd_disjuction : "(" "or" gd+ ")" 
gd_negation : "(" "not" gd ")" 
gd_implication : "(" "imply" gd gd ")"  // new
gd_existential : "(" "exists" "(" typed_var_list ")" gd ")" 
gd_universal : "(" "forall" "(" typed_var_list ")" gd ")" 

gd_equality_constraint : equallity var_or_const var_or_const ")" 

gd_ltl_at_end : "(" "at end" gd ")" 
gd_ltl_always : "(" "always" gd ")" 
gd_ltl_sometime : "(" "sometime" gd ")" 
gd_ltl_at_most_once : "(" "at-most-once" gd ")" 
gd_ltl_sometime_after : "(" "sometime-after" gd gd ")" 
gd_ltl_sometime_before : "(" "sometime-before" gd gd ")" 

gd_preference : "(" "preference" NAME gd ")" 


effect : eff_empty | eff_conjunction | eff_universal | eff_conditional | literal | p_effect 

eff_empty : "(" ")" 
eff_conjunction : "(" "and" effect+ ")" 
eff_universal : "(" "forall" "(" typed_var_list ")" effect ")" 
eff_conditional : "(" "when" gd effect ")" 

literal : neg_atomic_formula | atomic_formula 
neg_atomic_formula : "(" "not" atomic_formula ")" 

p_effect : "(" assign_op f_head f_exp ")" 

assign_op : "assign" | "scale-down" | "scale-up" | "increase" | "decrease" 

f_head : func_symbol | "(" func_symbol term* ")" 

f_exp : NUMBER | "(" bin_op f_exp f_exp ")" | "(" multi_op f_exp f_exp+ ")" | "(" "-" f_exp ")" | f_head 

bin_op : multi_op | "-" | "/" 

multi_op : "+" | "*" 

atomic_formula : "("predicate var_or_const*")" 
predicate : NAME 

equallity : "(" "=" | "(=" 

typed_var_list : typed_vars* 
typed_obj_list : typed_objs* 

typed_vars : VAR_NAME+ "-" var_type 
typed_var : VAR_NAME "-" var_type 
typed_objs : new_consts+ "-" var_type 
new_consts : NAME 
var_type : NAME | "(" "either" var_type+ ")" 

var_or_const : NAME | VAR_NAME 


term : NAME | VAR_NAME | functionterm 
functionterm : "(" func_symbol term* ")" 
func_symbol : NAME 


problem : "(" "define" "(" "problem" NAME ")" "(" ":domain" NAME ")" require_def? p_object_declaration? p_htn? p_init p_goal? p_constraint? metric_spec? ")" 

p_object_declaration : "(" ":objects" typed_obj_list")" 
p_init : "(" ":init" init_el*")" 
init_el : literal | num_init 
num_init : equallity f_head NUMBER ")" 
p_goal : "(" ":goal" gd ")" 

p_htn : "(" (":htn"|":htnti") (":parameters" "(" typed_var_list ")")? tasknetwork_def 

metric_spec : "(" ":metric" optimization ground_f_exp")" 
optimization : "minimize" | "maximize" 
ground_f_exp : "(" bin_op ground_f_exp ground_f_exp ")"
             | "(" multi_op ground_f_exp ground_f_exp+ ")"
             | ("(" "-" | "(-") ground_f_exp ")"
             | NUMBER
             | "(" func_symbol NAME* ")"
             | "total-time"
             | func_symbol 

p_constraint : "(" ":constraints" gd ")" 


VAR_NAME : "?" NAME
NAME: LETTER+ ("_"|"-"|LETTER|DIGIT)*
REQUIRE_NAME: ":" NAME
VARIABLE: "?" LETTER ("_"|"-"|LETTER|DIGIT)*

%import common.LETTER
%import common.DIGIT
%import common.CNAME
%import common.NUMBER
%import common.WS
%ignore WS
"""

parser = Lark(hddl_grammar_str, start="hddl_file")
