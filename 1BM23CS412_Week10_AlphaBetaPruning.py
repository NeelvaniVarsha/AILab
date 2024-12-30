import math

def minimax(depth, index, maximizing_player, values, alpha, beta):
    if depth == 0:
        return values[index]

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2): 
            eval = minimax(depth - 1, index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:  
                break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):  
            eval = minimax(depth - 1, index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:  
                break
        return min_eval

leaf_values = list(map(int, input("Enter the leaf node values separated by spaces: ").split()))

if math.log2(len(leaf_values)) % 1 != 0:
    print("Error: The number of leaf nodes must be a power of 2 (e.g., 2, 4, 8, 16).")
else:
    tree_depth = int(math.log2(len(leaf_values)))

    optimal_value = minimax(depth=tree_depth, index=0, maximizing_player=True, values=leaf_values, alpha=float('-inf'), beta=float('inf'))

    print("Optimal value calculated using Minimax:", optimal_value)
