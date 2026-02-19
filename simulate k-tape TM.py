def load_and_simulate_tm(file_path):      #we upload my .txt file and read it + simulate it

    with open(file_path, 'r') as file:     #open the file

        lines = [line.strip() for line in file]    #for each line, we strip out the leading and trailing whitespaces and select them

    num_tapes = int(lines[0])   #the first line in the input file contains the number of tapes for the TM, we convert it to an integer
    blank_sym = lines[1]    #the empty/blank symbol to denote for the empty cell of TM, in second line
    start_state = lines[2]  #the start state in line 3,
    accept_state = lines[3] #the accept state in line 4,
    reject_state = lines[4] #the reject state in line 5,
    input_string = lines[5] #the input string

    transitions = {}    #used to store the transition table/rules w.r.t states and input
    for line in lines[6:]:  #we have input from line 6 onwards

        # NOTE : IN THIS CODE, even though it is a K-tape TM, but we dont specifically mention separate Finite COntrol, instead 
        # everything depends on the transition function, if needed, we need to give the 2^k transitions for the K-tape TM/


        parts = [p.strip() for p in line.split(',')]    #for each line, split w.r.t comma, split it to different parts
        curr_state = parts[0]   #the 1st part contains my current state of TM
        curr_alpha = parts[1]   #the 2nd part, contains the symbols being read by the tape
        next_state = parts[2]   #the 3rd part, contains the next state it goes to after reading the i/p
        new_alpha = parts[3]    #the 4th part, the new symbol, for each tape
        actions = parts[4]      #the 5th part, L:left, R:right, S:stationary
        
        # it maps (current state and i/p) as key and (next state, symbols to write and directions) as its corresponding value
        transitions[(curr_state, curr_alpha)] = (next_state, new_alpha, actions)

    # INITIALIZE TAPES AND HEADS

    tapes = [{} for i in range(num_tapes)]  #empty disctionaries for each tape is created
    
    heads = [0 for i in range(num_tapes)]   #head pointer for each tape is created, the location initizalized to 0

    for i, char in enumerate(input_string): #read through the string and its indices (index, character) and store them in the first tape, other tape are still blank
        tapes[0][i] = char

    current_state = start_state
    print("--- Turing Machine Simulation Started ---\n")


    # RUN SIMULATION LOOP-this is the place where we run the TM


    #we store the current symbols for each tape, our main moto is to check it w.r.t. our defined transitions dictionary
    
    step = 0 #basically, the T(n) steps taken for the TM to get the output
    while True: # Run infitely, till we get to accept/reject/no transition availiable conditions

        current_symbols = ""    #we use it for every symbol read from the 1st read-tape

        for i in range(num_tapes):  #using this loop we see the symbols for each tape's head

            current_symbols += tapes[i].get(heads[i], blank_sym) #we get the current position of the head on out current tape
                                                                #.. .get() is used, if the tape's head is in a spot where there is no 
                                                                #...symbol yet i.e. no {0, 1, _} we simply return '_' as the current symbol

        print(f"Step {step} | State: {current_state} | Reading: '{current_symbols}'")

        # Check for Halt conditions
        if current_state == accept_state:       
            print("\nResult: MACHINE ACCEPTED")
            break
        if current_state == reject_state:
            print("\nResult: MACHINE REJECTED")
            break

        # if no such valid transition exists then we break the loop and return error
        key = (current_state, current_symbols)
        if key not in transitions:
            print(f"\nResult: MACHINE CRASHED (No transition defined for state '{current_state}' reading '{current_symbols}')")
            break


        next_state, new_symbols, actions = transitions[key] #if all's right, then we fetch the values of out key from trnansactions.

        # Apply new symbols and move heads
        for i in range(num_tapes):

            tapes[i][heads[i]] = new_symbols[i] #update the position pointed to by the head(for each tape) with the new symbol as given in the trainsition table

            #now, as per the action defined in the transition, increment/decrement the head position 
            if actions[i] == 'R':
                heads[i] += 1
            elif actions[i] == 'L':
                heads[i] -= 1

        current_state = next_state
        step += 1 


    # PRINT FINAL TAPE CONTENTS

    print("\n--- Final Tape Contents ---")
    for t_no in range(num_tapes):      #loop through the tape to print the final content/output string
        if not tapes[t_no]:             # We see if the dictionary representing our current tape is empty or not
            print(f"Tape {t_no}: [All Blanks]")
            continue
            
        # Find the boundaries of what was written on this tape
        min_idx = min(tapes[t_no].keys())   #leftmost key in the tape's dictionary
        max_idx = max(tapes[t_no].keys())   #rightmost key in the tape's dictionary
        
        content = ""        #content to hod the final string 
        for i in range(min_idx, max_idx + 1):   #loop through the final tape from leftmost to the rightmost position
            content += tapes[t_no].get(i, blank_sym)    #for the ith symbol on the specific tape, we add it to out final output, if not,
                                                        #.. we add the '_' symbol over there
            
        # The line below basically states,
        # if tape number equals 0, label it as "input tape"
        # or, if tape number is between 1 to k-1, label it as "working tape"
        # or, if tape number is k, label it as "work tape"


        label = " (Input Tape)" if t_no == 0 else " (Output Tape)" if t_no == num_tapes - 1 else " (Work Tape)"
        print(f"Tape {t_no}{label}: {content}")

# Run the program#
if __name__ == "__main__":
    load_and_simulate_tm('tm_config.txt')