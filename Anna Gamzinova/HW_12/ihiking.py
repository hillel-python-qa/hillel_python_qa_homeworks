from abc import abstractmethod, ABC


class IHiking:
    @abstractmethod
    def set_destination(self):
        pass

    @abstractmethod
    def hike_up(self):
        pass

    @abstractmethod
    def take_picture(self):
        print("Say Cheeese!")

    @abstractmethod
    def lunch_break(self):
        pass
