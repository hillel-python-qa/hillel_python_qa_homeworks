class MobileDevice:
    def __init__(self, operation_system: str, version_of_os: float, vendor: str,
                 level_of_battery: float, types_of_mobiles_apps: str):
        self.__operation_system = operation_system
        self.__version_of_os = version_of_os
        self.__vendor = vendor
        self.__level_of_battery = level_of_battery
        self.__types_of_mobile_apps = types_of_mobiles_apps

    @property
    def operation_system(self):
        return self.__operation_system

    @operation_system.setter
    def operation_system(self, operation_system="Android" or "iOS"):
        if operation_system:
            self.__operation_system = operation_system
        else:
            raise ValueError("You should not leave this field empty!")

    @property
    def version_of_os(self):
        return self.__version_of_os

    @version_of_os.setter
    def version_of_os(self, version_of_os):
        if version_of_os > 0:
            self.__version_of_os = version_of_os
        else:
            raise ValueError("You should enter a valid version of OS")

    @property
    def vendor(self):
        return self.__vendor

    @vendor.setter
    def vendor(self, vendor):
        if vendor:
            self.__vendor = vendor
        else:
            raise ValueError("This field should not be empty")

    @property
    def level_of_battery(self):
        return self.__level_of_battery

    @level_of_battery.setter
    def level_of_battery(self, level_of_battery):
        if level_of_battery >= 0:
            self.__level_of_battery = level_of_battery
        else:
            raise ValueError("This field should not be empty or have minus values")

    @property
    def types_of_mobile_apps(self):
        return self.__types_of_mobile_apps

    @types_of_mobile_apps.setter
    def types_of_mobile_apps(self, types_of_mobile_apps):
        if types_of_mobile_apps:
            self.__types_of_mobile_apps = types_of_mobile_apps
        else:
            raise ValueError("This field should not be empty")

    def __str__(self):
        output = f'{self.__class__.__name__}:{{\n' \
                 f'\toperation_system: {self.__operation_system}\n' \
                 f'\tversion_of_os: {self.__version_of_os}\n' \
                 f'\tvendor: {self.__vendor}\n' \
                 f'\tlevel_of_battery: {self.__level_of_battery}\n' \
                 f'\ttypes_of_mobile_apps: {self.__types_of_mobile_apps}'
        return output


if __name__ == '__main__':
    mobile_device = MobileDevice(operation_system="iOS", version_of_os=16.0, vendor="Apple",
                                 level_of_battery=75, types_of_mobiles_apps="Native")
    print(mobile_device)
