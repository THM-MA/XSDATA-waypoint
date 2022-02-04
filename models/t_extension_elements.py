from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.omg.org/spec/BPMN/20100524/MODEL"


@dataclass
class TExtensionElements:
    class Meta:
        name = "tExtensionElements"

    other_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        }
    )
