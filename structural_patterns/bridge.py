from abc import ABC, abstractmethod

# The "abstraction" defines the interface for the "control"
# part of the two class hierarchies. It maintains a reference
# to an object of the "implementation" hierarchy and delegates
# all of the real work to this object.
class RemoteControl:
    def __init__(self, device) -> None:
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        self.device.volume = self.device.volume - 10
    
    def volume_up(self):
        self.device.volume = self.device.volume + 10
    
    def channel_down(self):
        self.device.channel = self.device.channel - 1

    def channel_up(self):
        self.device.channel = self.device.channel + 1


class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.volume = 0


# The "implementation" interface declares methods common to all
# concrete implementation classes. It doesn't have to match the
# abstraction's interface. In fact, the two interfaces can be
# entirely different. Typically the implementation interface
# provides only primitive operations, while the abstraction
# defines higher-level operations based on those primitives.
# There not interfaces in Python, for that reason we're using abstract class
class Device(ABC):
    def __init__(self):
        self.is_power_on = True
        self._volume = 50
        self._channel = 1

    @abstractmethod
    def is_enable(self):
        pass
    
    @abstractmethod
    def enable(self):
        pass
    
    @abstractmethod
    def disable(self):
        pass

    @abstractmethod
    def volume(self):
        pass
    
    @abstractmethod
    def channel(self):
        pass


class Tv(Device):
    def is_enable(self):
        return self.is_power_on
    
    def enable(self):
        self.is_power_on = True
    
    def disable(self):
        self.is_power_on = False

    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self, new_volume):
        self._volume = new_volume

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, new_channel):
        self._channel = new_channel


class Radio(Device):
    def is_enable(self):
        return self.is_power_on
    
    def enable(self):
        self.is_power_on = True
    
    def disable(self):
        self.is_power_on = False

    @property
    def volume(self):
        return self._volume
    
    @volume.setter
    def volume(self, new_volume):
        self._volume = new_volume

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, new_channel):
        self._channel = new_channel


if __name__ == '__main__':
    tv = Tv()
    advanced_remote_control = AdvancedRemoteControl(tv)
    print('Muting the TV') 
    advanced_remote_control.mute()

    radio = Radio()
    remote = RemoteControl(radio)
    print('Changing the radio station')
    remote.channel_down()
