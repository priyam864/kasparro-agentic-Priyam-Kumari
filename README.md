# 🧠 Multi-Agent Content Generation System

A modular, agent-based automation system that transforms structured product data into multiple machine-readable content pages using a clean orchestration pipeline.



## 📌 Problem Statement

The goal of this project is to design and implement a **modular multi-agent system** that consumes a fixed, structured product dataset and automatically generates categorized, machine-readable content pages.

The system must:

* Operate **without external data sources**
* Demonstrate **clear agent boundaries**
* Use **reusable content logic blocks**
* Follow a well-defined **orchestration flow**

This project focuses on **system design and automation**, not domain knowledge or content creativity.



## 💡 Solution Overview

The solution follows an **orchestrator-driven multi-agent architecture**, where each agent is responsible for a single, well-defined task.

An orchestrator coordinates the execution of these agents in a pipeline to transform raw product data into structured JSON outputs such as:

* FAQ Page
* Product Description Page
* Product Comparison Page

The system emphasizes:

* **Modularity**
* **Reusability**
* **Separation of concerns**
* **Clear data flow**

All content generation is **rule-based and template-driven**, ensuring deterministic and machine-readable outputs.



## 🔍 Scope & Assumptions

### Scope

* Processes only the provided product dataset
* Generates content automatically using agents and templates
* Outputs strictly structured **JSON files**
* Includes a **fictional product** for comparison purposes

### Assumptions

* No external APIs, LLMs, or research are used
* All content accuracy is derived solely from input data
* Designed for extensibility but implemented for a single product scenario



## 🏗️ System Design (Core Focus)

### Overall Architecture

The system follows an **orchestrator-controlled pipeline** where agents pass structured data sequentially.

```
Product Data
   ↓
DataParserAgent
   ↓
QuestionGenerationAgent
   ↓
FictionalProductAgent
   ↓
Templates (FAQ / Product / Comparison)
   ↓
JSON Outputs
```

---

### Agent Responsibilities

**DataParserAgent**
Parses raw product input into a clean internal data model.

**QuestionGenerationAgent**
Generates categorized user questions (Informational, Usage, Safety, Purchase, Suitability).

**FictionalProductAgent**
Creates a structured fictional product to enable comparison without external data.

**Orchestrator**
Coordinates execution order, manages data flow between agents, and writes final outputs.

Each agent is:

* Independent
* Stateless
* Single-responsibility



### Content Logic Blocks

Reusable content logic blocks are implemented as **pure functions**.
They extract or format specific product attributes such as:

* Benefits
* Usage instructions
* Safety information

Characteristics:

* No side effects
* No shared/global state
* Reusable across templates

---

### Template System

Templates define **output structure**, not logic.

Implemented templates:

* FAQ Template
* Product Page Template
* Comparison Page Template

Templates assemble agent outputs and logic blocks into structured JSON documents.



### Orchestration Flow

The orchestrator executes the following sequence:

1. Parse raw product data
2. Generate categorized questions
3. Generate fictional comparison product
4. Render FAQ page
5. Render product page
6. Render comparison page
7. Save all outputs as JSON files

This flow ensures clarity, maintainability, and extensibility.



## 📄 Output Files

The system generates the following machine-readable outputs:

* `outputs/faq.json`
* `outputs/product_page.json`
* `outputs/comparison_page.json`

Each file follows a clean and consistent JSON schema.

---

## 📊 Optional Flow Representation

### Sequence Flow

```
Orchestrator → DataParserAgent → Parsed Product
Orchestrator → QuestionGenerationAgent → Questions
Orchestrator → FictionalProductAgent → Product B
Orchestrator → Templates → JSON Outputs
```

---

## ✅ Conclusion

This project demonstrates a clean, modular implementation of an **agentic automation system**.
By separating agents, logic blocks, templates, and orchestration, the system remains easy to understand, test, and extend while fully satisfying the assignment requirements.

---

## 🚀 How to Run

```bash
python -m agents.orchestrator
```


