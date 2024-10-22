class Album:
    def __init__(self, title, release_year,artist_id, id=None):
        self.artist_id = artist_id
        self.title = title
        self.release_year = release_year
        self.id = id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Album(Title:{self.title}, Release year:{self.release_year}, Artist ID:{self.artist_id})"
    
    def is_valid(self):
        if self.title == None or self.title == "":
            return False
        if self.release_year == None or self.release_year == "":
            return False
        if self.artist_id == None:
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.title == None or self.title == "":
            errors.append("Title can't be blank")
        if self.release_year == None or self.release_year == "":
            errors.append("Release year can't be blank")
        if self.artist_id == None or self.artist_id == "":
            errors.append("Artist name can't be blank and must start with a capital")
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)