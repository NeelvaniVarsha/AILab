class ForwardReasoning:
    def __init__(self, rules, facts):
        self.rules = rules  
        self.facts = set(facts)  

    def infer(self, query):
        applied_rules = True

        while applied_rules:
            applied_rules = False
            for condition, result in self.rules:
                if condition.issubset(self.facts) and result not in self.facts:
                    self.facts.add(result)  
                    applied_rules = True
                    print(f"Applied rule: {condition} -> {result}")
                    if query in self.facts:
                        return True

        return query in self.facts

rules = [
    ({"American(Robert)", "Missile(m1)", "Owns(CountryA, m1)"}, "Sells(Robert, m1, CountryA)"),  
    ({"Sells(Robert, m1, CountryA)", "American(Robert)", "Hostile(CountryA)"}, "Criminal(Robert)"),  
]

facts = {
    "American(Robert)",
    "Hostile(CountryA)",
    "Missile(m1)",
    "Owns(CountryA, m1)",
}

query = "Criminal(Robert)"

reasoner = ForwardReasoning(rules, facts)
result = reasoner.infer(query)

print("\nFinal facts:")
print(reasoner.facts)
print(f"\nQuery '{query}' inferred: {result}")
