from pathlib import Path
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.handlers import XmlEventHandler

# Models
from models.definitions import Definitions

filename = Path("example.xml").absolute()
parser = XmlParser(handler=XmlEventHandler)
definitions = parser.parse(str(filename), Definitions) # Unknown property waypoint
