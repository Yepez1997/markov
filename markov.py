import numpy as np

#must assert a n x n matrix

""" Computes the nth state of the Markov Chain """
def compute_markov(markov_matrix, state_vector):
    # Multiply markov_matrix * state_vector to obtain a new state 
    matrix_result = np.matmul(markov_matrix, state_vector)
    print(matrix_result)
    #print(matrix_result)
    return matrix_result


""" Computes the Markov Chain n times """
def compute_state(markov_matrix, state_vector, num_times):
    counts = 0 
    while (counts < num_times):  
        print("FFFFFFFFF")      
        new_state = compute_markov(markov_matrix, state_vector)
        counts += 1 
        new_state * 100000
        compute_markov(markov_matrix, new_state)
        counts += 1
    return 0 
    
    
""" Set up n probibility vectors """      
def setup_markov_matrix():
    a = np.array([[.95,.05]])
    prob_vec_one  = np.transpose(a)
    b = np.array([[.03,.97]])
    prob_vec_two = np.transpose(b)
    markov_matrix = np.concatenate((prob_vec_one,prob_vec_two), axis = 1)
    return markov_matrix

""" Set state vectors """   
def setup_state_vector():
    state_vector = np.array([[600000, 400000]])
    state_vector = np.transpose(state_vector)
    return state_vector


mm = setup_markov_matrix()
sv = setup_state_vector()
compute_state(mm,sv, 1)


