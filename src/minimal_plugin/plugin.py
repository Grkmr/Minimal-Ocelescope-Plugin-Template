from typing import Annotated

from ocelescope import OCEL, OCELAnnotation, Plugin, PluginInput, Resource, plugin_method


class MinimalResource(Resource):
    label = "Minimal Resource"
    description = "A minimal resource"

    def visualize(self):
        pass


class Input(PluginInput):
    pass


class MinimalPlugin(Plugin):
    label = "Minimal Plugin"
    description = "A ocelescope plugin"
    version = "0.1.0"

    @plugin_method(label="Example Method", description="An example plugin method")
    def example(
        self,
        ocel: Annotated[OCEL, OCELAnnotation(label="Event Log")],
        input: Input,
    ) -> MinimalResource:
        return MinimalResource()
