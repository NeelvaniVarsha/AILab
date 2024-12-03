import itertools

# Define a simple way to evaluate a formula in propositional logic
def evaluate_formula(formula, valuation):
    # Replace variables in the formula with their truth values from the valuation
    formula = formula.replace('p', str(valuation['p']))
    formula = formula.replace('q', str(valuation['q']))

    # Replace logical operators with their Python equivalents
    formula = formula.replace('and', 'and')   # Logical AND
    formula = formula.replace('or', 'or')     # Logical OR
    formula = formula.replace('not', 'not')   # Logical NOT
    formula = formula.replace('!=', '!=')     # Logical inequality
    formula = formula.replace('->', 'or not') # Implication p -> q = not p or q
    formula = formula.replace('<->', '==')    # Equivalence p <-> q = p == q

    # Evaluate the formula using Python's eval() function
    return eval(formula)

# Extract all the variables (propositional symbols) from a formula
def extract_variables(formula):
    variables = set()
    for char in formula:
        if char.isalpha() and char not in ['and', 'or', 'not', '!=', '->', '<->', '(', ')']:  # Only single-letter variables
            variables.add(char)
    return list(variables)

# Generate the truth table and print rows where KB or Query is True, and check entailment
def generate_truth_table(KB, query):
    # Extract all the propositional variables from the KB and query
    variables = extract_variables(KB) + extract_variables(query)
    variables = list(set(variables))  # Remove duplicates

    # Print headers for the truth table
    print("Truth Table (where KB or Query are True):")
    print(" | ".join(variables + ["KB", "Query"]))
    print("-" * (len(variables) * 4 + 12))

    # Track whether KB entails query
    kb_entails_query = True  # Assume it entails unless we find evidence to the contrary

    # Generate all possible truth assignments for the variables
    for assignment in itertools.product([False, True], repeat=len(variables)):
        valuation = dict(zip(variables, assignment))

        # Evaluate KB and query under this assignment
        KB_truth = evaluate_formula(KB, valuation)
        query_truth = evaluate_formula(query, valuation)

        # Print only the rows where either KB or query is True
        if KB_truth or query_truth:
            row = [str(valuation[var]) for var in variables]  # Values for variables
            row.append(str(KB_truth))  # KB truth value
            row.append(str(query_truth))  # Query truth value
            print(" | ".join(row))

        # If KB is True and query is False, then KB does not entail query
        if KB_truth and not query_truth:
            kb_entails_query = False  # Found a counterexample to entailment

    # Print whether KB entails query
    if kb_entails_query:
        print("\nKB entails the query (KB ⊨ query): True")
    else:
        print("\nKB entails the query (KB ⊨ query): False")

# Example usage: Accepting user input for KB and query
KB = input("Enter the knowledge base (e.g., 'p and (p != q)'): ")
query = input("Enter the query (e.g., 'q'): ")

# Call the function to generate the truth table and check entailment
generate_truth_table(KB, query)
