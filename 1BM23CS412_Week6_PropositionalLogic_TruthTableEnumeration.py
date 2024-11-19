import itertools

symbols = ['A', 'B', 'C']

A_or_C = lambda A, B, C: A or C
B_or_not_C = lambda A, B, C: B or not C

KB = lambda A, B, C: A_or_C(A, B, C) and B_or_not_C(A, B, C)

query = lambda A, B, C: A or B

def print_truth_table(symbols, A_or_C, B_or_not_C, KB, query):
    print(f"{'A':<6}{'B':<6}{'C':<6}{'A∨C':<8}{'B∨¬C':<8}{'KB':<8}{'α (A∨B)':<8}")
    for values in itertools.product([False, True], repeat=len(symbols)):
        assignment = dict(zip(symbols, values))
        A_val = assignment['A']
        B_val = assignment['B']
        C_val = assignment['C']
        A_or_C_val = A_or_C(A_val, B_val, C_val)
        B_or_not_C_val = B_or_not_C(A_val, B_val, C_val)
        KB_val = KB(A_val, B_val, C_val)
        query_val = query(A_val, B_val, C_val)
        print(f"{str(A_val):<6}{str(B_val):<6}{str(C_val):<6}"
              f"{str(A_or_C_val):<8}{str(B_or_not_C_val):<8}"
              f"{str(KB_val):<8}{str(query_val):<8}")

    entails = all(KB(**dict(zip(symbols, values))) <= query(**dict(zip(symbols, values)))
                  for values in itertools.product([False, True], repeat=len(symbols)))
    print("\nResult:")
    if entails:
        print("KB entails the query (α).")
    else:
        print("KB does not entail the query (α).")

print_truth_table(symbols, A_or_C, B_or_not_C, KB, query)
