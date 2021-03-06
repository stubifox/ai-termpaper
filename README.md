# Termpaper and Implementation: solvability of instances of the 15-Puzzle 


The 15-puzzle first gained public attention in the 1870s when Sam Loyd promised $1000 in prize money to anyone who could solve his puzzle, which became known as the 14-15puzzle.
It was not until nearly a decade later that authors of the American Journal of Mathematics published a proof that the puzzle is unsolvable. Today, the 15-puzzle is a classic use case when it comes to modelling algorithms with heuristics, such as A* or IDA*. 

The main purpose of this work is to outline and implement the algorithm for checking the solvability of an instance of the 15-puzzle. This algorithm is based on Bradlow’s approach where a puzzle is considered solvable, if the parity of the transposition count and the manhattan distance of the blank field match.

The In the process written source-code can be found within the appendix. To test this implementation, an evaluation of specific test-cases is conducted. Altough the algorithm specifies the solvability for a given puzzle instance, it remains uncertain how many steps are required to obtain this solution. Hence the algorithm provides no indicator for computing time.
