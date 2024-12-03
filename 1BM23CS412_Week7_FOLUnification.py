class UnificationError(Exception):
    pass
def unify(term1, term2, substitution=None, level=0):
    if substitution is None:
        substitution = {}
    indent = "  " * level 
    print(f"{indent}Unifying: {term1} and {term2}")
    if term1 == term2:
        print(f"{indent}Terms are identical, no substitution.")
        return substitution
    elif is_variable(term1):
        print(f"{indent}Unifying variable {term1} with {term2}")
        return unify_variable(term1, term2, substitution, level + 1)
    elif is_variable(term2):
        print(f"{indent}Unifying variable {term2} with {term1}")
        return unify_variable(term2, term1, substitution, level + 1)
    elif isinstance(term1, tuple) and isinstance(term2, tuple):
        if term1[0] != term2[0]: 
            raise UnificationError(f"Cannot unify {term1} with {term2}, different function names.")
        for t1, t2 in zip(term1[1], term2[1]):
            substitution = unify(t1, t2, substitution, level + 1)
        return substitution
    else:
        raise UnificationError(f"Cannot unify {term1} with {term2}, they are incompatible.")
def unify_variable(var, term, substitution, level):
    indent = "  " * level  
    if var in substitution:
        print(f"{indent}Variable {var} is already substituted as {substitution[var]}")
        return unify(substitution[var], term, substitution, level + 1)
    if term == var:
        print(f"{indent}Variable {var} is the same as the term, no substitution.")
        return substitution
    if is_variable(term) and var in get_variables(term):
        raise UnificationError(f"{indent}Cannot unify variable {var} with {term} (circular unification).")
    print(f"{indent}Substituting {var} with {term}")
    substitution[var] = term
    return substitution
def is_variable(term):
    return isinstance(term, str) and term.islower()
def get_variables(term):
    if is_variable(term):
        return {term}
    elif isinstance(term, tuple):
        variables = set()
        for arg in term[1]:
            variables.update(get_variables(arg))
        return variables
    else:
        return set()
if __name__ == "__main__":
    print("\nExample 1: Unifying P(x, a, b) and P(y, z, b)\n")
    term1 = ('P', ['x', 'a', 'b'])
    term2 = ('P', ['y', 'z', 'b'])
    try:
        substitution = unify(term1, term2)
        print("\nFinal Unification Result:", substitution)
    except UnificationError as e:
        print("Unification failed:", e)
    print("\nExample 2: Unifying P(x, f(Y)) and P(Z, f(a))\n")
    term3 = ('P', ['x', ('f', ['Y'])])
    term4 = ('P', ['Z', ('f', ['a'])])
    try:
        substitution = unify(term3, term4)
        print("\nFinal Unification Result:", substitution)
    except UnificationError as e:
        print("Unification failed:", e)
