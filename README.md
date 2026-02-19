# Simulating-a-K-tape-Turing-Machine
This code simulates a K-tape turing machine, by taking in the input contents, from a .txt file itself. 
The input contents are 
1) number of tape(s),
2) blank-state-representation,
3) start-state,
4) accept-state,
5) reject-state,
6) input-string,
7) transitions

# How it works?
The simulation fundamentally works by translating the theoretical mechanics of a multi-tape Turing Machine into basic Python data structures. It begins by reading the configuration file to build a "rulebook" (a dictionary mapping current states and symbols to future actions) and sets up the physical "hardware" by representing infinitely long tapes as Python dictionaries—which cleverly allows the machine to move into negative indices without throwing errors—and read/write heads as simple integer trackers starting at position zero. Once the initial input string is loaded onto the first tape, the core simulation engine kicks off an infinite loop. In every single step of this loop, the machine reads the characters currently under all heads, looks up the corresponding instruction in its rulebook, writes new characters back to the tapes, adjusts the head tracker integers mathematically to simulate moving left or right, and transitions to its next internal state. This cycle repeats continuously until the machine shifts into a defined accept or reject state, or crashes due to a missing rule. Upon halting, it scans the dictionaries to find the highest and lowest positions the heads ever visited, allowing it to extract and print a neat, bounded string of the final tape contents.
