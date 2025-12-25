# Multi-Agent Content Generation System

---

## 1. Problem Statement

The objective of this project is to design and implement a modular, agent-based automation system that consumes a fixed, structured product dataset and automatically generates multiple categorized, machine-readable content pages.  
The system must operate without any external data sources and demonstrate clean system design, clear agent boundaries, reusable logic blocks, and an orchestrated execution flow.

---

## 2. Solution Overview

This project implements a multi-agent architecture where each agent is responsible for a single, well-defined task.  
An orchestrator coordinates these agents in a pipeline to transform raw product data into structured JSON content pages such as an FAQ page, a product description page, and a comparison page.

The solution focuses on:
- modularity
- reusability
- clarity of data flow
- separation of concerns

The entire system is rule-based and template-driven, emphasizing system design rather than content creativity.

---

## 3. Scope & Assumptions

### Scope
- The system processes only the provided product dataset.
- All content is generated automatically through agents and templates.
- Outputs are strictly machine-readable JSON files.
- A fictional product is generated internally for comparison purposes.

### Assumptions
- No external APIs or research are allowed.
- Content accuracy is derived only from the given input data.
- The system is designed for extensibility but implemented for a single product use case.

---

## 4. System Design (Most Important Section)

### 4.1 Overall Architecture

The system follows an **orchestrator-driven, multi-agent pipeline architecture**.  
Each agent performs a single responsibility and passes its output forward in the pipeline.

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

### 4.2 Agent Responsibilities

**DataParserAgent**  
Parses raw product input into a clean internal representation used across the system.

**QuestionGenerationAgent**  
Generates categorized user questions (Informational, Usage, Safety, Purchase, Suitability).

**FictionalProductAgent**  
Generates a structured fictional product to enable comparison without external data.

**Orchestrator**  
Controls execution order, manages data flow between agents, and writes final JSON outputs.

Each agent is independent, stateless, and has clearly defined input and output.

---

### 4.3 Content Logic Blocks

Reusable content logic blocks are implemented as pure functions.  
They extract or format specific aspects of product data such as benefits, usage instructions, and safety information.

These blocks:
- contain no side effects
- do not depend on global state
- can be reused across multiple templates

---

### 4.4 Template System

Templates define the **structure of final outputs**, not the logic itself.

Implemented templates include:
- FAQ Template
- Product Page Template
- Comparison Page Template

Each template consumes agent outputs and logic blocks to assemble structured JSON pages.

---

### 4.5 Orchestration Flow

The orchestrator executes the system in the following order:

1. Parse raw product data
2. Generate categorized questions
3. Generate fictional comparison product
4. Render FAQ page
5. Render product page
6. Render comparison page
7. Save all outputs as JSON files

This pipeline ensures clarity, maintainability, and easy extensibility.

---

## 5. Optional Diagrams & Flow Representation

### Sequence Flow (Textual)

```

Orchestrator → DataParserAgent → Parsed Product
Orchestrator → QuestionGenerationAgent → Questions
Orchestrator → FictionalProductAgent → Product B
Orchestrator → Templates → JSON Outputs

```

---

## 6. Conclusion

This project demonstrates a clean, modular implementation of an agentic automation system.  
By separating agents, logic blocks, templates, and orchestration, the system remains easy to understand, test, and extend while fulfilling all assignment requirements.
```
