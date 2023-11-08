class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def get_authors(self):
        output = ""
        for a in self.authors:
            output += f"- {a}\n"
        return output

    def get_dependencies(self):
        output = ""
        for i in self.dependencies:
            output += f"- {i}\n"
        return output

    def get_dev_dependencies(self):
        output = ""
        for i in self.dev_dependencies:
            output += f"- {i}\n"
        return output

    def __str__(self):
        authorss = self.get_authors()
        dependenciess = self.get_dependencies()
        dev_dependenciess = self.get_dev_dependencies()
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\nAuthors: \n{authorss}"
            f"\nDependencies: \n{dependenciess}"
            f"\nDevelopment dependencies: \n{dev_dependenciess}"
        )
