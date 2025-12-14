import asyncio
from browser_use import Agent, Browser, ChatGoogle
from dotenv import load_dotenv

def run_agent(task: str):
    """
    Initializes and runs the browser automation agent.
    """
    load_dotenv()

    # Connect to your existing Chrome browser
    browser = Browser(
        executable_path='/usr/sbin/chromium',
        user_data_dir='~/.config/chromium',
        profile_directory='Default',
    )

    llm = ChatGoogle(model='gemini-flash-latest')

    agent = Agent(
        task=task,
        browser=browser,
        llm=llm
    )
    asyncio.run(agent.run())
