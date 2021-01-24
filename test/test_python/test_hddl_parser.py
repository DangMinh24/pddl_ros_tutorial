import unittest2 as unittest
import sys
from pathlib import Path
workspace_directory = Path(Path(__file__).parent.parent.parent)
sys.path.insert(0, str(workspace_directory))

from scripts.pddl_parser.hddl_parser import (
    hddl_grammar_str
)
from lark import Lark


class Test_HDDL_Component(unittest.TestCase):
    def test_hddl_goal(self):
        inputs_ = [
            """
             (:goal (and
                     (clear b8)
                     (on-table b8)
                     (clear b3)
                     (on-table b6)
                     (on b3 b6)
                     (clear b4)
                     (on-table b1)
                     (on b4 b7)
                     (on b7 b5)
                     (on b5 b2)
                     (on b2 b10)
                     (on b10 b9)
                     (on b9 b1)))

            """
        ]
        parser = Lark(hddl_grammar_str, start="p_goal")
        for i, input_ in enumerate(inputs_):
            try:
                result = parser.parse(input_)
            except:
                error_msg = "Sentence {}-th:\n{}\nis not valid.".format(
                    i, input_)
                self.fail(error_msg)


class Test_HDDL_Parser(unittest.TestCase):

    def test_hddl_parser(self):
        inputs_ = [
            """
            (define
             (problem pfile_010)
             (:domain blocks)
             (:objects b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 - BLOCK)
             (:init
              (hand-empty)
              (clear b10)
              (on-table b10)
              (clear b9)
              (on-table b8)
              (on b9 b2)
              (on b2 b6)
              (on b6 b7)
              (on b7 b5)
              (on b5 b1)
              (on b1 b3)
              (on b3 b4)
              (on b4 b8))
             (:goal (and
                     (clear b8)
                     (on-table b8)
                     (clear b3)
                     (on-table b6)
                     (on b3 b6)
                     (clear b4)
                     (on-table b1)
                     (on b4 b7)
                     (on b7 b5)
                     (on b5 b2)
                     (on b2 b10)
                     (on b10 b9)
                     (on b9 b1)))
            )        
            """
        ]
        parser = Lark(hddl_grammar_str, start="hddl_file")
        for i, input_ in enumerate(inputs_):
            result = parser.parse(input_)
            print(result)


if __name__ == "__main__":
    unittest.main()
