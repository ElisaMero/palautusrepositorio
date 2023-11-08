from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella

        cont = toml.loads(content)

        return Project(cont["tool"]["poetry"]["name"], cont["tool"]["poetry"]["description"], cont["tool"]["poetry"]["license"], cont["tool"]["poetry"]["authors"], cont["tool"]["poetry"]["dependencies"], cont["tool"]["poetry"]["group"]["dev"]["dependencies"])
