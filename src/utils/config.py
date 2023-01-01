from ruamel.yaml import YAML

import os


class Config:
    config_folder_name = "config"

    def __init__(self):
        self.config_dir = None
        self.config_base = "config"
        self.init_dir()
        self.get_config()

    def init_dir(self):
        cwd = os.path.dirname(os.path.abspath(__file__))
        project_home = os.path.abspath(os.path.join(cwd, "../../"))
        self.config_dir = os.path.abspath(os.path.join(project_home, self.config_folder_name))

    def get_config(self):
        self.log.i("*************************************************")
        if self.env.lower() == self.DEV.lower():
            self.apply_config(self.config_base + "_D.yaml")
        elif self.env.lower() == self.LOADTEST.lower():
            self.apply_config(self.config_base + "_T.yaml")
        elif self.env.lower() == self.QA.lower():
            self.apply_config(self.config_base + "_Q.yaml")
        elif self.env.lower() == self.PRODUCTION.lower():
            self.apply_config(self.config_base + "_P.yaml")
        elif self.env.lower() == self.LOCAL.lower():
            self.apply_config(self.config_base + "_L.yaml")
        else:
            print("Configuration not found for " + self.env)
            raise Exception("Environment configuration not found")
        self.log.i("*************************************************")

    def apply_config(self, config):
        self.log.i("Applying config from " + config)
        yaml = YAML()
        config_file = os.path.join(self.config_dir, config)
        self.log.i("Config file " + config_file)
        stream = open(os.path.abspath(config_file), 'r')
        config_dict = yaml.load(stream)
        self.log.d(config_dict)
        self.__dict__.update(**config_dict)
        self.make_data_dir()

    def make_data_dir(self):
        data_dir = os.path.join(self.config_dir, self.data_dir)
        self.log.i("Making data dir " + data_dir)
        os.makedirs(os.path.dirname(data_dir), exist_ok=True)