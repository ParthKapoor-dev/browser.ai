# AI Agent Overview

This document provides a high-level overview for AI agents to understand and contribute to the `browser.ai` project.

## Project Goal

The primary goal of `browser.ai` is to create a CLI tool that can automate browser actions based on natural language prompts. It aims to be a powerful and flexible tool for developers, testers, and anyone who wants to automate web-based tasks.

## Core Components

*   **`browser_ai/`**: The main Python package for the project.
    *   **`cli/`**: Contains the command-line interface code. This is the entry point for the user.
    *   **`agents/`**: This directory will contain different AI agents responsible for specific tasks (e.g., a planning agent, a browser interaction agent).
    *   **`core/`**:  This will house the core logic for browser automation, prompt processing, and state management.

## Getting Started

1.  **Understand the `main.py`:** This is the entry point of the application.
2.  **Explore the `cli/` directory:**  See how the CLI is structured and how it interacts with the user.
3.  **Look at the `ROADMAP.md`:** This will give you an idea of the project's direction.

## How to Contribute

1.  **Pick a task from the `ROADMAP.md`:** Start with a small, well-defined task.
2.  **Write code:** Follow the existing coding style and conventions.
3.  **Add tests:** Ensure that your changes are well-tested.
4.  **Update documentation:** If you add a new feature, update the relevant documentation.
