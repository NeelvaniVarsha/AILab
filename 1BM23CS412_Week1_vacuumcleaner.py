class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment
        self.cleaned_cells = 0
        self.position = (0, 0)

    def clean(self):
        while True:
            x, y = self.position

            if self.environment[x][y] == 'D':
                self.environment[x][y] = 'C'  
                self.cleaned_cells += 1
                print(f"Cleaned position {self.position}")

            next_position = self.find_next_dirty()
            if next_position:
                print(f"Moving to next dirty position {next_position}")
                self.position = next_position
            else:
                print("No more dirty cells found. Cleaning complete.")
                break

    def find_next_dirty(self):
        for i in range(len(self.environment)):
            for j in range(len(self.environment[i])):
                if self.environment[i][j] == 'D':
                    return (i, j)  
        return None  

    def display_environment(self):
        for row in self.environment:
            print(" ".join(row))
        print(f"Total cleaned cells: {self.cleaned_cells}")


initial_environment = [
    ['D', 'C', 'D', 'D'],
    ['C', 'D', 'C', 'C'],
    ['D', 'C', 'D', 'C'],
    ['C', 'C', 'C', 'D']
]

agent = VacuumCleanerAgent(initial_environment)
print("Initial environment:")
agent.display_environment()

agent.clean()

print("\nFinal environment:")
agent.display_environment()
