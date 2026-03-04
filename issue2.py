import sys, types, time

# stub external deps so the GUI module loads
mgr = types.ModuleType("manager")
ram_logging = types.ModuleType("ram_logging")
ram_logging.log_manager = types.SimpleNamespace(LogManager=types.SimpleNamespace(logger=types.SimpleNamespace(info=lambda *a, **k: None)))
mgr.ram_logging = ram_logging
sys.modules["manager"] = mgr
sys.modules["manager.ram_logging"] = ram_logging
sys.modules["manager.ram_logging.log_manager"] = ram_logging.log_manager
sys.modules["rclpy"] = types.SimpleNamespace()
sys.modules["websocket"] = types.SimpleNamespace(WebSocketApp=object)

sys.path.insert(0, "/Users/deveshmishra/Documents/jde/RoboticsAcademy/common/gui_interfaces")
from gui_interfaces.general.measuring_threading_gui import MeasuringThreadingGUI

class Demo(MeasuringThreadingGUI):
    def __init__(self):
        super().__init__(host="ws://ignore", freq=2)
        self.client = types.SimpleNamespace(send=lambda *a, **k: None)
        self.start()
    def run_websocket(self): # no real network
        while self.running:
            time.sleep(0.1)
    def get_real_time_factor(self):
        while self.running:
            time.sleep(0.1)
            self.real_time_factor = 1.0
    def update_gui(self):
        pass

if __name__ == "__main__":
    Demo()
    print("main thread finished. If the process stays running, non-daemon threads are blocking exit.")
