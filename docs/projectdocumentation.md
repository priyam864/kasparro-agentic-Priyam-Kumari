# 🧠 Multi-Agent Content Generation System (CrewAI)

A **framework-based, agentic automation system** built using **CrewAI** that generates structured, machine-readable content from product data using **real LLM-backed agents**, task orchestration, and schema validation.



## 📌 Problem Statement

The objective of this assignment is to design and implement a **true multi-agent content generation system** that:

* Uses a **real agentic framework** (CrewAI)
* Employs **LLM-backed autonomous agents**
* Avoids **hardcoded or rule-based outputs**
* Produces **validated, machine-readable JSON**
* Demonstrates **clean system design and orchestration**

The focus is on **agent autonomy, orchestration quality, and robustness**, not content creativity.

---

## 💡 Solution Overview

This project implements a **CrewAI-orchestrated multi-agent system** where independent agents collaborate to analyze product data and generate structured FAQ content.

Each agent is responsible for a **single, well-defined task**, while CrewAI manages:

* Task sequencing
* Context propagation between agents
* Execution control
* Output validation

The system generates a **schema-validated JSON FAQ page** containing **at least 15 FAQs**, fully compliant with assignment constraints.

---

## 🏗️ System Architecture

The system follows a **single authoritative CrewAI pipeline**:

```
Product Data
   ↓
Product Analyst Agent
   ↓
FAQ Generator Agent
   ↓
Content Structuring Agent
   ↓
Pydantic Schema Validation
   ↓
JSON Output (faq.json)
```

⚠️ **Important**:
This repository contains **only one implementation** — the CrewAI-based system.
All legacy, non-framework, hardcoded, or wrapper implementations have been **fully removed**.

---

## 🤖 Agents & Responsibilities

### 🧩 Product Analyst Agent

* Analyzes structured product input
* Builds a semantic understanding of:

  * Purpose
  * Ingredients
  * Benefits
  * Usage
  * Side effects
  * Target users
  * Price
* Uses **LLM reasoning**
* No hardcoded logic

---

### ❓ FAQ Generator Agent

* Generates **≥15 user-focused FAQs**
* Answers are strictly grounded in analyzed product data
* No external data or hallucinated content
* Uses **LLM-based reasoning**

---

### 🧱 Content Structuring Agent

* Converts generated FAQs into structured JSON
* Enforces correctness via **Pydantic schema**
* Rejects invalid or incomplete outputs

---

## 📐 Schema Validation

Final output is validated using **Pydantic**, ensuring:

* Required fields are present
* Correct data types
* Minimum FAQ count (≥15) is enforced
* No malformed JSON is produced

Schema validation is a **hard constraint**, not optional.

---

## 📄 Output Artifact

Generated file:

```
outputs/faq.json
```

Contents:

* `product_name`
* Array of **at least 15 FAQs**
* Each FAQ contains:

  * `question`
  * `answer`

The output is **fully machine-readable and production-ready**.

---

## ⚙️ Orchestration & Execution

* Agents are executed via **CrewAI Tasks**
* Tasks define:

  * Objective
  * Expected output
  * Validation constraints
* CrewAI handles:

  * Agent execution order
  * Context sharing
  * Failure handling

There is **no manual orchestration** or sequential scripting.

---

## 🚀 How to Run

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Set environment variable

```bash
OPENAI_API_KEY=your_api_key_here
```

### 3️⃣ Run the system

```bash
python run_crewai.py
```

---

## 🧠 Technologies Used

* **Python 3.12**
* **CrewAI** — multi-agent orchestration framework
* **OpenAI API** — LLM-powered agent reasoning
* **Pydantic** — schema validation
* **dotenv** — environment configuration
* **JSON** — structured output format

---

| Requirement                 | Status   |
| --------------------------- | -------- |
| Multi-agent framework       | ✅ CrewAI |
| Real LLM usage              | ✅        |
| No hardcoded outputs        | ✅        |
| No fake / wrapper agents    | ✅        |
| Single authoritative system | ✅        |
| ≥15 FAQs enforced           | ✅        |
| Schema validation           | ✅        |
| Machine-readable output     | ✅        |
| Clear orchestration         | ✅        |

---

## 🏁 Conclusion

This project demonstrates a **clean, production-grade agentic system** built using CrewAI.

By combining:

* Autonomous LLM-backed agents
* Framework-based orchestration
* Schema-validated outputs
