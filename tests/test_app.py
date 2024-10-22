from playwright.sync_api import Page, expect



def test_get_emoji(page, test_web_address): 
    page.goto(f"http://{test_web_address}/emoji")
    strong_tag = page.locator("strong")
    expect(strong_tag).to_have_text(":)")

def test_get_goodbye(page, test_web_address):
    page.goto(f"http://{test_web_address}/goodbye")
    strong_tag = page.locator("strong")
    expect(strong_tag).to_have_text("Bye!")

def test_get_greet(page, test_web_address):
    page.goto(f"http://{test_web_address}/greet")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Hello None!")