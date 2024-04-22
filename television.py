class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        function to set default status of tv to off, volume down,
        tv set to minimum channel, and unmuted
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        turns the tv off and on
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        mutes and unmutes the tv
        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False

    def channel_up(self) -> None:
        """
        increases the channel
        if max channel is reached, circles back to min channel
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel +=1

    def channel_down(self) -> None:
        """
        decreases the channel
        if min channel is reached, circles back to max channel
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -=1

    def volume_up(self) -> None:
        """
        turns volume up
        if tv is muted when called it will unmute the tv
        if max volume is reached, remains at max volume value
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                if self.__volume == Television.MAX_VOLUME:
                    self.__volume = Television.MAX_VOLUME
                else:
                    self.__volume += 1
            else:
                if self.__volume == Television.MAX_VOLUME:
                    self.__volume = Television.MAX_VOLUME
                else:
                    self.__volume += 1

    def volume_down(self) -> None:
        """
        decreases the volume
        if tv is muted when called, unmutes tv and decreases volume
        if min volume is reached, remains at minimum volume value
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                if self.__volume == Television.MIN_VOLUME:
                    self.__volume = Television.MIN_VOLUME
                else:
                    self.__volume -= 1
            else:
                if self.__volume == Television.MIN_VOLUME:
                    self.__volume = Television.MIN_VOLUME
                else:
                    self.__volume -= 1

    def __str__(self) -> str:
        """
        returns details of the tv's status
        :return: tv status.
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


