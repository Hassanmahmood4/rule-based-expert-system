from collections import defaultdict, deque

class FactBase:
    def __init__(self):
        self._facts = set()
        self._sources = defaultdict(list)

    def add(self, fact, source=None):
        if fact not in self._facts:
            self._facts.add(fact)
            if source:
                self._sources[fact].append(source)
            return True
        return False

    def has(self, fact):
        return fact in self._facts

    def all(self):
        return set(self._facts)

    def sources(self, fact):
        return self._sources.get(fact, [])

class Rule:
    def __init__(self, rid, conditions, conclusion, priority=0):
        self.rid = rid
        self.conditions = set(conditions)
        self.conclusion = conclusion
        self.priority = priority

    def applicable(self, facts):
        return self.conditions.issubset(facts)

class InferenceEngine:
    def __init__(self, rules):
        self.rules = sorted(rules, key=lambda r: r.priority, reverse=True)
        self.trace = []
        self.fired = set()

    def forward(self, factbase):
        agenda = deque(self.rules)
        progress = True
        while progress:
            progress = False
            for rule in list(agenda):
                if rule.rid in self.fired:
                    continue
                if rule.applicable(factbase.all()) and not factbase.has(rule.conclusion):
                    added = factbase.add(rule.conclusion, source=rule.rid)
                    if added:
                        self.fired.add(rule.rid)
                        self.trace.append((rule.rid, tuple(rule.conditions), rule.conclusion))
                        progress = True

    def explanation(self):
        lines = []
        for rid, conds, concl in self.trace:
            lines.append(f"[{rid}] IF {', '.join(sorted(conds))} THEN {concl}")
        return lines

class KnowledgeBase:
    def __init__(self):
        self.rules = []

    def load_rules(self):
        self.rules.extend([
            Rule("R1", ["fever", "cough"], "flu", priority=2),
            Rule("R2", ["flu", "body_ache"], "severe_flu", priority=3),
            Rule("R3", ["sneezing", "runny_nose"], "common_cold", priority=1),
            Rule("R4", ["flu"], "rest_recommended", priority=1),
            Rule("R5", ["severe_flu"], "doctor_visit_required", priority=4),
            Rule("R6", ["fever", "rash"], "measles_suspected", priority=5),
            Rule("R7", ["measles_suspected"], "isolation_required", priority=3),
            Rule("R8", ["flu", "shortness_of_breath"], "complication_risk", priority=4),
        ])

    def get_rules(self):
        return list(self.rules)

class ExpertSystemApp:
    def __init__(self):
        self.kb = KnowledgeBase()
        self.kb.load_rules()
        self.fb = FactBase()
        self.engine = InferenceEngine(self.kb.get_rules())

    def run(self, user_facts):
        for f in user_facts:
            self.fb.add(f, source="USER")
        self.engine.forward(self.fb)
        return self.fb.all(), self.engine.explanation(), self.fb._sources

if __name__ == "__main__":
    print("Enter symptoms (comma separated):")
    data = input().strip().lower()
    inputs = [x.strip() for x in data.split(",") if x.strip()]
    app = ExpertSystemApp()
    facts, trace, sources = app.run(inputs)

    print("\n--- Inference Trace ---")
    for t in trace:
        print(t)

    print("\n--- Final Facts ---")
    for f in sorted(facts):
        print("-", f)

    print("\n--- Provenance ---")
    for k, v in sources.items():
        print(f"{k}: {v}")