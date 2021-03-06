from src.neuro.inter_area_connection import InterAreaConnection
from src.neuro.neural_area import NeuralArea
from src.neuro.neural_pattern import NeuralPattern
from src.neuro.patterns_connection import PatternsConnection


class Container:

    def __init__(self):
        self.network = None
        self.areas = []
        self.connections = []
        self.zones = []
        self.pattern_connections = []

    def add_area(self, area):
        self.areas.append(area)

    def add_connection(self, source: NeuralArea, target: NeuralPattern) -> InterAreaConnection:
        connections = [c for c in self.connections if c.source == source and c.target == target]
        assert len(connections) == 0, f'Connection between {source} and {target} already exists'
        conn = InterAreaConnection(source=source, target=target)
        self.connections.append(conn)
        conn.on_adding()
        return conn

    def add_patterns_connection(self, connection: PatternsConnection) -> None:
        connections = [c for c in self.pattern_connections if
                       c.source == connection.source and c.target == connection.target]
        assert len(connections) == 0, f'Connection between {connection.source} and {connection.target} already exists'
        self.pattern_connections.append(connection)
