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

def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    expected_output = '["Artist(Name:Korn, Genre:Metal)","Artist(Name:Pantera, Genre:Metal)","Artist(Name:Type O Negative, Genre:Metal)","Artist(Name:Pentatonix, Genre:Pop)"]'
    actual_output = response.data.decode('utf-8').strip()
    assert expected_output == actual_output

def test_post_artist(web_client):
    response = web_client.post('/artists', data={'name':'Wild nothing','genre':'Indie'})
    assert response.status_code == 200

    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    expected_output = '["Artist(Name:Korn, Genre:Metal)","Artist(Name:Pantera, Genre:Metal)","Artist(Name:Type O Negative, Genre:Metal)","Artist(Name:Pentatonix, Genre:Pop)","Artist(Name:Wild nothing, Genre:Indie)"]'
    actual_output = get_response.data.decode('utf-8').strip()
    assert expected_output == actual_output