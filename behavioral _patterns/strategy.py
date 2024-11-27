from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    @abstractmethod
    def build_route(self, start_point, final_point):
        pass


class RoadStrategy(RouteStrategy):
    def build_route(self, start_point, final_point):
        print ('Road route: $$$ - ⏳️')


class PublicTransportStrategy(RouteStrategy):
    def build_route(self, start_point, final_point):
        print ('Public transport route: $$ - ⏳️⏳️')


class WalkingStrategy(RouteStrategy):
    def build_route(self, start_point, final_point):
        print ('Walking route: $ - ⏳️⏳️⏳️⏳️')


class Navigator:
    def __init__(self, route_strategy) -> None:
        self.route_strategy = route_strategy

    def set_strategy(self, route_strategy):
        self.route_strategy = route_strategy

    def build_route(self, start_point, final_point):
        return self.route_strategy.build_route(start_point, final_point)


if __name__ == "__main__":
    road_strategy = RoadStrategy()

    navigator = Navigator(road_strategy)
    navigator.build_route('353454.4', '423543.2')

    navigator.set_strategy(PublicTransportStrategy())
    navigator.build_route('353454.4', '423543.2')

    navigator.set_strategy(WalkingStrategy())
    navigator.build_route('353454.4', '423543.2')
