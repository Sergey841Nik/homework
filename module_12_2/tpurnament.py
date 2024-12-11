class Runner:
    def __init__(self, name, speed=5) -> None:
        self.name: str = name
        self.distance: int = 0
        self.speed: int = speed

    def run(self) -> None:
        self.distance += self.speed * 2

    def walk(self) -> None:
        self.distance += self.speed

    def __str__(self) -> str:
        return self.name

    def __eq__(self, other) -> bool:
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance: int, *participants: Runner):
        self.full_distance: int = distance
        self.participants: list = list(participants)

    def start(self) -> dict:
        finishers: dict = {}
        place: int = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
                    # break

        return finishers
