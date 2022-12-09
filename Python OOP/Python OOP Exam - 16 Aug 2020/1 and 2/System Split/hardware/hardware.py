from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        # TODO check the calculation if it works correct
        if self.capacity >= software.capacity_consumption and self.memory >= software.memory_consumption:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    def __str__(self):
        result = ''
        total_memory_software = sum([m.memory_consumption for m in self.software_components])
        total_capacity_software = sum([m.capacity_consumption for m in self.software_components])

        result += f"Hardware Component - {self.name}\n" \
                  f"Express Software Components: {len([s for s in self.software_components if s.__class__.__name__ == 'ExpressSoftware'])}\n" \
                  f"Light Software Components: {len([s for s in self.software_components if s.__class__.__name__ == 'LightSoftware'])}\n" \
                  f"Memory Usage: {total_memory_software} / {self.memory}\n" \
                  f"Capacity Usage: {total_capacity_software} / {self.capacity}\n" \
                  f"Type: {self.hardware_type}\n" \
                  f"Software Components: {', '.join([s.name for s in self.software_components]) if self.software_components else 'None'}\n"

        return result
