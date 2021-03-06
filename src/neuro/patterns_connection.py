from src.neuro.neural_pattern import NeuralPattern


class PatternsConnection:

    def __init__(self,
                 source: NeuralPattern,
                 target: NeuralPattern,
                 agent,
                 tick: int = 0,
                 weight: float = 1.0,
                 dope_value: int = 0,
                 ):
        self.source = source
        self.target = target
        self.weight = weight
        self.agent = agent
        self.tick = tick
        self.dope_value = dope_value

    @classmethod
    def add(cls, source, target, agent, **kwargs) -> 'PatternsConnection':
        connection = cls(source, target, agent, **kwargs)
        agent.container.add_patterns_connection(connection)
        return connection
