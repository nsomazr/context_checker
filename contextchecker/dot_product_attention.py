from imports import *

def dot_product_attention(previous_state, hidden_state):
    
    #calculate the score weight for each element

    scores = np.dot(hidden_state,np.transpose(previous_state))
    
    #calculate the weight vector , usinng softmax
    
    w_n =  np.exp(scores)/np.sum(np.exp(scores), axis=1)
    
    # calculate the context vector
    
    c_t = np.dot(w_n, hidden_state)
    
    return w_n, c_t