from dataclasses import dataclass
from .t_end_event import TEndEvent

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class EndEvent(TEndEvent):
    class Meta:
        name = "endEvent"
        namespace = "http://www.omg.org/spec/BPMN/20100524/MODEL"
