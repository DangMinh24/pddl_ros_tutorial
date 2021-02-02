import unittest2 as unittest
import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))

from scripts.pddl_parser.pddl_parser import (
    pddl_grammar_str
)
from lark import Lark


class Test_PDDL_Components_Parsing(unittest.TestCase):
    def test_parse_action(self):
        inputs_ = [
            """
                (:action pick
                :parameters (?obj ?room ?gripper)
                :precondition  (and  (ball ?obj) (room ?room) (gripper ?gripper)
                        (at ?obj ?room) (at-robby ?room) (free ?gripper))
                :effect (and (carry ?obj ?gripper)
                    (not (at ?obj ?room)) 
                    (not (free ?gripper))))
            """
        ]
        parser = Lark(pddl_grammar_str, start="structure_def")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Description {}-th is not a valid description: \n{}".format(
                    i, input_)
                self.fail(error_msg)


class Test_PDDL_Parser(unittest.TestCase):
    # @unittest.skip("")
    def test_parser(self):
        inputs_ = [
            """
                (define (problem wumpus-a-1)
                  (:domain wumpus-a)
                  (:objects
                   sq-1-1 sq-1-2 sq-1-3
                   sq-2-1 sq-2-2 sq-2-3
                   the-gold
                   the-arrow
                   agent
                   wumpus)

                  (:init
                   (adj sq-1-1 sq-1-2) (adj sq-1-2 sq-1-1)
                   (adj sq-1-2 sq-1-3) (adj sq-1-3 sq-1-2)
                   (adj sq-2-1 sq-2-2) (adj sq-2-2 sq-2-1)
                   (adj sq-2-2 sq-2-3) (adj sq-2-3 sq-2-2)
                   (adj sq-1-1 sq-2-1) (adj sq-2-1 sq-1-1)
                   (adj sq-1-2 sq-2-2) (adj sq-2-2 sq-1-2)
                   (adj sq-1-3 sq-2-3) (adj sq-2-3 sq-1-3)

                   (pit sq-1-2)

                   (at the-gold sq-1-3)
                   (at agent sq-1-1)
                   (have agent the-arrow)
                   (at wumpus sq-2-3))

                  (:goal (and (have agent the-gold) (at agent sq-1-1)))
                  )            
            """,
            """
                (define (problem assem-x-1)
                (:domain assembly)
                (:objects bracket valve device frob fastener widget tube sprocket
                            wire doodad gimcrack connector hack plug contraption mount
                            socket unit hoozawhatsie - assembly
                            charger voltmeter - resource)
                (:init (available valve)
                        (available device)
                        (available fastener)
                        (available widget)
                        (available tube)
                        (available wire)
                        (available gimcrack)
                        (available connector)
                        (available hack)
                        (available contraption)
                        (available mount)
                        (available unit)
                        (available hoozawhatsie)
                        (available charger)
                        (available voltmeter)
                        (requires frob charger)
                        (requires sprocket charger)
                        (requires doodad voltmeter)
                        (requires plug voltmeter)
                        (requires socket voltmeter)
                        (part-of valve bracket)
                        (part-of device bracket)
                        (part-of frob bracket)
                        (part-of sprocket bracket)
                        (part-of plug bracket)
                        (part-of fastener frob)
                        (part-of widget frob)
                        (part-of tube frob)
                        (part-of mount sprocket)
                        (part-of wire sprocket)
                        (part-of doodad sprocket)
                        (part-of gimcrack doodad)
                        (part-of connector doodad)
                        (part-of hack doodad)
                        (part-of contraption plug)
                        (transient-part mount plug)
                        (part-of socket plug)
                        (part-of unit socket)
                        (part-of hoozawhatsie socket)
                        (assemble-order fastener tube frob)
                        (assemble-order widget tube frob)
                        (assemble-order mount contraption sprocket)
                        (assemble-order wire mount sprocket)
                        (assemble-order mount contraption plug)
                        (remove-order contraption mount plug)
                        (assemble-order hoozawhatsie unit socket))
                (:goal (complete bracket))
                )            
            """,
            """
                (define (domain domain_name)


                (:requirements :strips :typing :conditional-effects )

                (:types 
                    vehicle - physobj
                    truck   - vehicle
                    location    -   object
                    city        -   location
                )



                (:predicates 
                    (at ?x - object ?loc - location)
                    (in-city ?loc - location ?city - city)
                    (in ?x - object ?truck - truck)

                )



                (:action drive-truck
                    :parameters (?truck - truck ?loc-from - location ?loc-to - location ?city - city)
                    :precondition (and 
                                    (at ?truck ?loc-from)
                                    (in-city ?loc-from ?city)
                                    (in-city ?loc-to ?city)
                                )
                    :effect (and 
                        (at ?truck ?loc-to)
                        (not (at ?truck ?loc-from))
                        (forall (?x - obj)
                            (when (and (in ?x ?truck)) 

                                (and (not (at ?x ?loc-from))
                                        (at ?x ?loc-to)
                                )
                            )
                        )
                    )
                )

                )            
                """,
            """
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
        ]
        parser = Lark(pddl_grammar_str, start="pddl_doc")

        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Description {}-th is not a valid description: \n{}".format(
                    i, input_)
                self.fail(error_msg)


if __name__ == '__main__':
    unittest.main()
