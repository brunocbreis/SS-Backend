# resolve
class Resolve:
    def __init__(self) -> None:
        print("Got Resolve.")


# fusion methods
class Fusion:
    def GetResolve(self) -> Resolve:
        return Resolve()


# tool methods
class Tool:
    def __init__(self, id: str) -> None:
        self.id = id
        self._inputs = {}
        self._attrs = {}

    def __str__(self) -> str:
        try:
            name = self._attrs["TOOLS_Name"]
        except KeyError:
            name = f"instance of {self.id}"
        return name

    def SetAttrs(self, attrs: dict[str, str]) -> None:
        for key, value in attrs.items():
            self._attrs[key] = value
            print(f"Setting {key} to {value}")

    def SetInput(self, input_name: str, value: float | str | int) -> None:
        self._inputs[input_name] = value
        print(f"Setting {self} {input_name} to {value}")

    def GetInput(self, input_name: str) -> float | int | str:
        return self._inputs[input_name]

    def Delete(self) -> None:
        print(f"Deleting {self}")


# comp methods
class Comp:
    def AddTool(self, tool_id: str, x: int, y: int) -> Tool:
        return Tool(tool_id)

    @property
    def CurrentFrame(self):
        return CurrentFrame()


class Flow:
    def QueueSetPos(self, tool: Tool, x: int, y: int) -> None:
        print(f"Queuing {tool}'s position to be set to ({x}, {y}).")

    def FlushSetPosQueue(self) -> None:
        print("Flushing Set Pos Queue.\n")

    def SetPos(self, tool: Tool, x: int, y: int) -> None:
        print(f"Setting {tool}'s position to ({x}, {y}).")


class CurrentFrame:
    @property
    def FlowView(self) -> Flow:
        return Flow()

    def ViewOn(self, tool: Tool, view: int) -> None:
        print(f"Viewing {tool} on monitor number {view}")
