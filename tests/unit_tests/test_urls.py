import pytest


class TestURLs:
    def test_homepage(self, client):
        """Testing rendering of the home page."""
        response = client.get("/")
        assert b"Welcome to my website !" in response.data

    def test_summary(self, client):
        """Testing rendering of the summary page."""
        response = client.get("/summary")
        assert b"Coding Languages" in response.data

    def test_projects(self, client):
        """Testing rendering of the projects page."""
        response = client.get("/projects")
        assert b"Links" in response.data

    def test_about_me(self, client):
        """Testing rendering of the about me page."""
        response = client.get("/about_me")
        assert b"software developer" in response.data
