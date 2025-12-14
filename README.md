# Browser.AI

Browser.AI is a powerful browser automation tool that leverages the capabilities of [browser-use.com](httpss://browser-use.com) to automate web tasks using natural language instructions. This project provides a simple and intuitive way to control a web browser with plain English commands, making web automation more accessible and flexible.

## Features

*   **Natural Language Control:**  Instead of writing complex scripts, you can provide instructions in plain English to automate browser actions.
*   **AI-Powered Automation:** Utilizes AI agents and Large Language Models (LLMs) to understand and execute your commands.
*   **Flexible and Adaptable:**  Can handle dynamic and complex web applications, as it's not reliant on rigid selectors.
*   **Playwright Integration:**  Powered by Playwright for robust and reliable browser control.

## Getting Started

### Prerequisites

*   Python 3.7+
*   An API key from [browser-use.com](httpss://browser-use.com)

### Installation

1.  Clone this repository:
    ```bash
    git clone https://github.com/your-username/browser.ai.git
    cd browser.ai
    ```

2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Set up your `browser-use.com` API key. You can do this by setting an environment variable:
    ```bash
    export BROWSER_USE_API_KEY='your-api-key'
    ```

## Usage

To run the browser automation, execute the `main.py` script with your natural language command as an argument:

```bash
python main.py "Go to google.com and search for 'browser automation tools'"
```

The script will then launch a browser and perform the actions you've specified.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
