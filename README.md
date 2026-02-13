🧠 Rule-Based Expert System (Forward Chaining)

A modular, explainable rule-based expert system implemented in Python. The system performs
forward chaining over a knowledge base of if–then rules to infer conclusions from user-provided facts.
It includes conflict resolution (rule priorities), multi-step inference, and explainability via an inference trace and provenance.


🚀 Features
	•	🧩 Rule engine with if–then rules
	•	🔁 Forward chaining inference
	•	🧠 Multi-step reasoning (chained rules)
	•	⚖️ Conflict resolution using rule priorities
	•	🧾 Explainable AI: inference trace + provenance
	•	🔌 Modular architecture (Knowledge Base, Fact Base, Inference Engine)
	•	🧪 Extensible to other domains (medical, troubleshooting, recommendations)


🛠️ Tech Stack
	•	Language: Python
	•	Paradigm: Symbolic AI (Rule-Based Reasoning)
	•	Inference: Forward Chaining
	•	Design: Modular, explainable system components


📂 Project Structure

rule-based-expert-system/
├── code.py        
├── .gitignore
└── README.md


⚙️ How It Works

The system evaluates rules using:
\text{IF } \{\text{conditions}\} \subseteq \text{Facts} \Rightarrow \text{add Conclusion}
Rules fire iteratively until no new facts can be inferred. When multiple rules are applicable, priorities resolve conflicts. Each fired rule is logged to provide transparent reasoning.


▶️ Usage

python code.py

You’ll be prompted to enter facts (e.g., symptoms). The system outputs:
	•	The inference trace (which rules fired)
	•	The final inferred facts
	•	Provenance for conclusions

📌 Example

Input

fever, cough, body_ache

Output (excerpt)

[R1] IF cough, fever THEN flu
[R2] IF body_ache, flu THEN severe_flu
[R5] IF severe_flu THEN doctor_visit_required


📈 Complexity
	•	Worst-case time: O(R × F) per iteration (R = rules, F = facts)
	•	Space: O(F + R)
(Practical performance depends on rule selectivity and chaining depth.)


🔮 Extensions
	•	Load rules from JSON/YAML
	•	Add confidence scores to conclusions
	•	Build a web UI (Streamlit/FastAPI)
	•	Persist sessions and inference graphs
	•	Add backward chaining for goal-driven queries


👤 Author

Hassan Mahmood
GitHub: https://github.com/Hassanmahmood4

