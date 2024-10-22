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

# def test_post_album(web_client):
#     response = web_client.post('/albums', data={'title':'Voyage','release_year':'2022','artist_id':'2'})
#     assert response.status_code == 200

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

def test_post_artist(web_client):
    response = web_client.post('/artists', data={'name':'Wild nothing','genre':'Indie'})
    assert response.status_code == 200