import yaml

class settings:
    @staticmethod
    def get():
        with open('data.yml') as file:
            token = yaml.safe_load(file)
        return token