from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def find_hardware(hardware_name):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                return hardware

    @staticmethod
    def find_software(software_name):
        for software in System._software:
            if software.name == software_name:
                return software

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_hardware(hardware_name)

        if not hardware:
            return "Hardware does not exist"

        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_software)
        System._software.append(new_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.find_hardware(hardware_name)

        if not hardware:
            return "Hardware does not exist"

        new_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_software)
        System._software.append(new_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.find_hardware(hardware_name)
        software = System.find_software(software_name)

        if not hardware or not software:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        total_memory_consumption_software = sum([m.memory_consumption for m in System._software])
        total_memory_consumption_hardware = sum([m.memory for m in System._hardware])
        total_capacity_consumption_software = sum([c.capacity_consumption for c in System._software])
        total_capacity_consumption_hardware = sum([c.capacity for c in System._hardware])

        result = "System Analysis\n" \
                 f"Hardware Components: {len(System._hardware)}\n" \
                 f"Software Components: {len(System._software)}\n" \
                 f"Total Operational Memory: {total_memory_consumption_software} / {total_memory_consumption_hardware}\n" \
                 f"Total Capacity Taken: {total_capacity_consumption_software} / {total_capacity_consumption_hardware}"

        return result

    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            result += str(hardware)

        return result.strip()


