class Anime:
    def __init__(self, title, total_episodes, watched_episodes, status, rating):
        self.title = title
        self.total_episodes = total_episodes
        self.watched_episodes = watched_episodes
        self.status = status  # Watching, Completed, On Hold, Dropped, Plan to Watch
        self.rating = rating  # 1-10 atau bisa None

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Episodes: {self.watched_episodes}/{self.total_episodes}\n"
                f"Status: {self.status}\n"
                f"Rating: {self.rating}")