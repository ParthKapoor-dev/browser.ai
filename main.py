import asyncio
from browser_use import Agent, Browser, ChatGoogle
from dotenv import load_dotenv

load_dotenv()

# Connect to your existing Chrome browser
browser = Browser(
    executable_path='/usr/sbin/chromium',
    user_data_dir='~/.config/chromium',
    profile_directory='Default',
)

llm = ChatGoogle(model='gemini-flash-latest')

agent = Agent(
    task='Visit https://duckduckgo.com and search for "browser-use founders"',
    browser=browser,
	llm=llm
)
async def main():
	await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
