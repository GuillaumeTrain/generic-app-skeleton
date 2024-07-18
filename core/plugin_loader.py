import importlib
import os
import time


class PluginBase:
    def __init__(self, classname, name, version, author="", website="", description=""):
        self.classname = classname
        self.name = name
        self.version = version
        self.description = description
        self.author = author
        self.website = website

    def start(self):
        raise NotImplementedError


def load_plugins(splashscreen,plugin_folder="plugins"):
    plugins = {}
    #count the number of plugins
    plugin_count = len([filename for filename in os.listdir(plugin_folder) if filename.endswith(".py")])
    #set the progress bar range to the number of plugins
    splashscreen.progressBar.setRange(0, plugin_count)
    #set the progress bar value to 0
    splashscreen.progressBar.setValue(0)
    progress_value = 0
    #iterate over the files in the plugins folder
    for filename in os.listdir(plugin_folder):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            splashscreen.update_progress(value=progress_value, plugin_name=module_name)
            module = importlib.import_module(f"{plugin_folder}.{module_name}")
            plugin_class = getattr(module, "Plugin")
            print(plugin_class)
            plugin_instance = plugin_class()

            #store plugin classname , name, version, author, website, description into the plugins dictionary
            plugins[plugin_instance.classname] = {"name": plugin_instance.name,
                                                  "version": plugin_instance.version,
                                                  "author": plugin_instance.author,
                                                  "website": plugin_instance.website,
                                                  "description": plugin_instance.description,
                                                  "instance": plugin_instance}
            #update the progress bar value
            print(plugin_instance.name)


            wait_time = 500
            time.sleep(wait_time / 100)
            progress_value = splashscreen.progressBar.value() + 1
            splashscreen.update_progress(value=progress_value, plugin_name=plugin_instance.name)

    return plugins
