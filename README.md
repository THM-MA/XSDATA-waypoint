# xsdata-waypoint
Testcase for XSDATA "Unknown property waypoint" parser error.

# Install testdata
    git clone https://github.com/THM-MA/XSDATA-waypoint.git
    cd XSDATA-waypoint
    python -m venv venv
    pip install git+https://github.com/tefra/xsdata@master#egg=xsdata[cli,lxml]

# Generate dataclasses
    xsdata .\schemas\BPMN20.xsd --package .\models --structure-style clusters --relative-imports

# Run test program
    python bpmn_test_parser.py

# Error message

    File "c:\Users\Thomas\Desktop\XSDATA-waypoint\venv\lib\site-packages\xsdata\formats\dataclass\parsers\nodes\element.py", line 344, in child
        raise ParserError(f"Unknown property {self.meta.qname}:{qname}")
    xsdata.exceptions.ParserError: Unknown property {http://www.omg.org/spec/BPMN/20100524/DI}BPMNEdge:{http://www.omg.org/spec/DD/20100524/DI}waypoint

Pay attention to the **BPMN** and **DD** difference within the namespaces.

# Error description
The XS schema contains an element named BPMNEdge that has a child element named waypoint:

    <bpmndi:BPMNEdge id="Flow_02wrji7_di" bpmnElement="Flow_02wrji7">
        <di:waypoint x="208" y="117" />
        <di:waypoint x="270" y="117" />
    </bpmndi:BPMNEdge>

Both elments belong to different namespaces:

    xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" # BPMN  
    xmlns:di="http://www.omg.org/spec/DD/20100524/DI"       # DD

![error](https://github.com/THM-MA/xsdata-waypoint/blob/main/images/waypoint.png)

*waypoint* is a class variable of class *Edge*. Class *LabeledEdge* inherits from *Edge*. Class *Bpmnedge* inherits from *LabeledEdge*. 

![class diagram](https://github.com/THM-MA/xsdata-waypoint/blob/main/images/class-diagram.png)

While parsing the XML file the XmlParser assignes the namespace of the parent elment (*BPMNEdge*) to the child element (*waypoint*). Instead the parser should pull the namespace from correct namespace of class *Edge*. 

# Debugging the error message
The error can be located in class xsdata.formats.dataclass.models.builders.XmlMetaBuilder, method build

    class_vars = self.build_vars(
        clazz,
        namespace, # Wrong namespace of Bpmnedge is assigned here!
        element_name_generator,
        attribute_name_generator,
    )

# Full example
The file [example.xml](https://github.com/THM-MA/XSDATA-waypoint/blob/main/example.xml) contains a full example of a BPMN diagram that we try to parse using XSDATA:

![BPMN example](https://github.com/THM-MA/xsdata-waypoint/blob/main/images/example_bpmn.png)

Any help is highly appreciated.

Thanks
Thomas