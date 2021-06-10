# Termpaper and Implementation: solvability of instances of the 15-Puzzle 


The 15-puzzle first gained public attention in the 1870s when Sam Loyd promised$1000in prize money to anyone who could solve his puzzle, which became known as the 14-15puzzle.
It was not until nearly a decade later that authors of the American Journal of Mathematicspublished a proof that the puzzle is unsolvable. Today, the 15-puzzle is a classic use casewhen it comes to modelling algorithms with heuristics, such as A* or IDA*. 

The main purpose of this work is to outline and implement the algorithm for checking thesolvability of an instance of the 15-puzzle. This algorithm is based on Bradlow’s approachwhere a puzzle is considered solvable, if the parity of the transposition count and the man-hattan distance of the blank field match.

The In the process written source-code can be found within the appendix. To test thisimplementation, an evaluation of specific test-cases is conducted. Altough the algorithm specifies the solvability for a given puzzle instance, it remains un-certain how many steps are required to obtain this solution. Hence the algorithm providesno indicator for computing time.III
