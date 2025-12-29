# 🧠 Multi-Agent Content Generation System (CrewAI)

A framework-based, multi-agent content generation system built using **CrewAI** that transforms structured product data into validated, machine-readable JSON content through real LLM-backed agent collaboration.



## 📌 Problem Statement

The objective of this project is to design and implement a **framework-driven multi-agent system** that consumes structured product data and automatically generates categorized, machine-readable content.

The system must:

* Use a **real agentic framework** (CrewAI)
* Implement **LLM-backed autonomous agents**
* Enforce **schema validation**
* Follow a clear **orchestration pipeline**
* Avoid hardcoded or fake outputs

The focus is on **agent design, orchestration, and robustness**, rather than content creativity.

---

## 💡 Solution Overview

The solution is implemented using **CrewAI**, where multiple autonomous agents collaborate to analyze product data, generate content, and structure outputs.

Each agent performs a **single responsibility**, and a CrewAI orchestrator manages task execution, context passing, and output validation.

Generated outputs include:

* FAQ Page (≥15 FAQs)
* Structured JSON compliant with a Pydantic schema

The system emphasizes:

* Framework-based orchestration
* Agent autonomy
* Clear data flow
* Deterministic output validation

---

## 🧠 Technologies Used

* **Python 3.12**
* **CrewAI** – multi-agent orchestration framework
* **OpenAI API** – LLM-powered agent reasoning
* **Pydantic** – schema validation
* **dotenv** – environment configuration
* **JSON** – structured output format

---

## 🔍 Scope & Assumptions

### Scope

* Processes a fixed, structured product dataset
* Uses **LLM-backed agents** via CrewAI
* Generates **validated JSON outputs**
* Enforces minimum content constraints (e.g., FAQ count ≥ 15)

### Assumptions

* LLMs are used strictly within the provided product context
* No external web search or external data sources are used
* The system is designed for extensibility but demonstrated for a single product

---

## 🏗️ System Design (Core Focus)

### Overall Architecture

The system follows a **CrewAI-orchestrated multi-agent pipeline**:

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

---

### Agent Responsibilities

**Product Analyst Agent**
Analyzes structured product input and builds a clear internal understanding of:

* Purpose
* Ingredients
* Benefits
* Usage
* Side effects
* Target users
* Price

**FAQ Generator Agent**
Generates **≥15 user-focused FAQs** strictly grounded in the analyzed product data.

**Content Structuring Agent**
Transforms generated content into a **schema-compliant JSON structure**, enforcing correctness and completeness.

Each agent is:

* LLM-backed
* Autonomous
* Stateless
* Single-responsibility

---

## 🧩 Task-Oriented Orchestration

Tasks are defined explicitly using CrewAI’s `Task` abstraction:

* Product analysis task
* FAQ generation task
* Content structuring & validation task

CrewAI manages:

* Execution order
* Context propagation
* Error handling
* Agent-task coordination

---

## 📐 Schema Validation

Final outputs are validated using **Pydantic schemas**, ensuring:

* Required fields exist
* Data types are enforced
* Minimum FAQ count is satisfied

Invalid outputs are rejected automatically.

---

## 📄 Output Files

The system generates the following machine-readable output:

* `outputs/faq.json`

The output contains:

* `product_name`
* An array of **≥15 validated FAQs**
* Clean, structured JSON suitable for downstream systems

---

## 📊 Execution Flow (Textual)

```
CrewAI Orchestrator
   → Product Analyst Agent
   → FAQ Generator Agent
   → Content Structuring Agent
   → Schema Validation
   → JSON Output
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set environment variable

```bash
OPENAI_API_KEY=your_api_key_here
```

### 3. Run the system

```bash
python run_crewai.py
```

---

## ✅ Conclusion

This project demonstrates a **real agentic system** built with CrewAI, featuring:

* Autonomous LLM-backed agents
* Framework-based orchestration
* Schema-validated outputs
* Robust, non-hardcoded content generation




