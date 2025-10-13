from collections import deque

class KnowledgeBase:
    def __init__(self):
        self.facts = set()
        self.rules = []
        self.inferred = set()
        
    def add_fact(self, fact):
        if fact not in self.facts:
            print(f"Adding fact: {fact}")
            self.facts.add(fact)
            return True
        return False
    
    def add_rule(self, premises, conclusion):
        self.rules.append((premises, conclusion))
        
    def forward_chain(self):
        agenda = deque(self.facts)
        
        while agenda:
            fact = agenda.popleft()
            if fact in self.inferred:
                continue
            self.inferred.add(fact)
            
            for (premises, conclusion) in self.rules:
                if all(p in self.inferred for p in premises):
                    if conclusion not in self.facts:
                        print(f"Inferred new fact: {conclusion} from {premises} => {conclusion}")
                        self.facts.add(conclusion)
                        agenda.append(conclusion)
                        
                        if conclusion == 'Criminal(West)':
                            print("\n Goal Reached: West is Criminal")
                            return True
        return False

# Instantiate KB
kb = KnowledgeBase()

# --------- FACTS FROM PROBLEM STATEMENT ---------
kb.add_fact('American(West)')
kb.add_fact('Enemy(Nono, America)')
kb.add_fact('Missile(M1)')
kb.add_fact('Owns(Nono, M1)')  # Nono has missiles owned by Nono

# --------- RULES ---------

# 1. Missile(x) => Weapon(x)
kb.add_rule(premises=['Missile(M1)'], conclusion='Weapon(M1)')

# 2. Missile(x) ∧ Owns(Nono, x) => Sells(West, x, Nono)
kb.add_rule(premises=['Missile(M1)', 'Owns(Nono, M1)'], conclusion='Sells(West, M1, Nono)')

# 3. Enemy(x, America) => Hostile(x)
kb.add_rule(premises=['Enemy(Nono, America)'], conclusion='Hostile(Nono)')

# 4. American(p) ∧ Weapon(q) ∧ Sells(p, q, r) ∧ Hostile(r) => Criminal(p)
kb.add_rule(premises=['American(West)', 'Weapon(M1)', 'Sells(West, M1, Nono)', 'Hostile(Nono)'], conclusion='Criminal(West)')

# --------- EXECUTE FORWARD CHAINING ---------
kb.forward_chain()


#########################OUTPUT#############################

Adding fact: American(West)
Adding fact: Enemy(Nono, America)
Adding fact: Missile(M1)
Adding fact: Owns(Nono, M1)
Inferred new fact: Hostile(Nono) from ['Enemy(Nono, America)'] => Hostile(Nono)
Inferred new fact: Weapon(M1) from ['Missile(M1)'] => Weapon(M1)
Inferred new fact: Sells(West, M1, Nono) from ['Missile(M1)', 'Owns(Nono, M1)'] => Sells(West, M1, Nono)
Inferred new fact: Criminal(West) from ['American(West)', 'Weapon(M1)', 'Sells(West, M1, Nono)', 'Hostile(Nono)'] => Criminal(West)

 Goal Reached: West is Criminal
True
