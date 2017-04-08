from checks import AgentCheck

class SampleCheck(AgentCheck):
    def check(self, instance):
        self.gauge(1)

class SampleClass():
    def __init__(self):
        self._num = 0

    def get(self):
        return self._num

    def set(self, num):
        self._num = num
        return self._num
