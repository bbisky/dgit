class Repository():
    """
    wrap git.Repo for django templates
    """
    def __init__(self, path, description, last_change):
        self.path = path
        self.description = description
        self.last_change = last_change
        
    def __unicode__(self):
        return self.description