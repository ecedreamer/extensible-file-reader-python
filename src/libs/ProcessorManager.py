import json
from importlib import import_module
from pathlib import Path

from libs.ProcessorInterface import ProcessorInterface


class PluginManager:
    plugins = {}

    def load_plugins(self):
        self.discover_plugins()
        return self.plugins

    @staticmethod
    def __read_manifest(manifest_path: str, key: str) -> str:
        with open(manifest_path) as file:
            content = json.load(file)
        return content.get(key)

    def discover_plugins(self):
        plugin_folder_str = 'src/pluggable_readers'
        plugin_folder = Path(plugin_folder_str)
        plugin_module_str = ".".join(plugin_folder_str.split("/"))
        for item in plugin_folder.iterdir():
            if item.is_dir() and not item.name.startswith("_"):
                manifest_path = f"{plugin_folder}/{item.name}/manifest.json"
                plugin_script = self.__read_manifest(manifest_path, key="plugin_script")
                version = self.__read_manifest(manifest_path, key="version")
                plugin_script = plugin_script.split(".")[0]
                script_path = f"{plugin_module_str}.{item.name}.{plugin_script}"
                module = import_module(name=script_path, package=plugin_module_str)
                for name in dir(module):
                    obj = getattr(module, name)
                    if isinstance(obj, type) and issubclass(obj, ProcessorInterface) and obj != ProcessorInterface:
                        self.plugins[item.name] = {"reader": obj, "version": version}
