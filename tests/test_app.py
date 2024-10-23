from playwright.sync_api import Page, expect

def test_get_albums_loads(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums")
    expect(page).to_have_title('Albums')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Albums")

def test_get_single_album_loads(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/1")
    expect(page).to_have_title('Album')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Vulgar display of power")

def test_post_album(page, test_web_address):
    page.goto(f"http://{test_web_address}/albums/new")
    expect(page).to_have_title('New Album')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("New Album")
    text_box = page.get_by_role("textbox", name="title")
    expect(text_box).to_be_editable()

def test_get_artists_loads(page, test_web_address):
    page.goto(f"http://{test_web_address}/artists")
    expect(page).to_have_title('Artists')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artists")

def test_get_single_artist_loads(page, test_web_address):
    page.goto(f"http://{test_web_address}/artists/1")
    expect(page).to_have_title('Artist')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Korn")

def test_post_artist(page, test_web_address):
    page.goto(f"http://{test_web_address}/artists/new")
    expect(page).to_have_title('New Artist')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("New Artist")
    text_box = page.get_by_role("textbox", name="name")
    expect(text_box).to_be_editable()