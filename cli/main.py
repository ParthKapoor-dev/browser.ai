import argparse
from core.agent import run_agent

def main():
    """
    The main entry point for the browser.ai CLI.
    """
    parser = argparse.ArgumentParser(
        description="A CLI tool to automate browser actions with AI."
    )
    parser.add_argument(
        "prompt",
        nargs="?",
        default=None,
        help="The prompt for the browser agent.",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Run in interactive mode.",
    )
    args = parser.parse_args()

    if args.interactive:
        print("Entering interactive mode...")
        while True:
            try:
                prompt = input(">>> ")
                if prompt.lower() in ["exit", "quit"]:
                    break
                run_agent(prompt)
            except KeyboardInterrupt:
                break
        print("Exiting interactive mode.")
    elif args.prompt:
        run_agent(args.prompt)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
