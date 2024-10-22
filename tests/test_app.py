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

def test_post_album(web_client):
    response = web_client.post('/albums', data={'title':'Voyage','release_year':'2022','artist_id':'2'})
    assert response.status_code == 200

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

def test_get_artists_loads(page, test_web_address):
    page.goto(f"http://{test_web_address}/artists")
    expect(page).to_have_title('Artists')
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Artists")

def test_post_artist(web_client):
    response = web_client.post('/artists', data={'name':'Wild nothing','genre':'Indie'})
    assert response.status_code == 200