"""
Example demonstrating the neural parser (with stub implementation).

Note: This example shows the API structure. The actual neural network inference
is not yet implemented - you need to provide the TensorFlow model file.
"""
import datetime
from timenorm import Interval, from_xml, TemporalNeuralParser
import xml.etree.ElementTree as ET


def main():
    print("=" * 70)
    print("Timenorm-Py Neural Parser API Example")
    print("=" * 70)
    print()

    # Example 1: Basic parser initialization
    print("1. Initialize Parser")
    print("-" * 70)
    parser = TemporalNeuralParser()
    print(f"Parser created: {parser}")
    print("Note: TensorFlow model will only be loaded when needed")
    print()

    # Example 2: Using context manager
    print("2. Context Manager Usage")
    print("-" * 70)
    with TemporalNeuralParser() as parser:
        print(f"Parser in context: {parser}")
        print("Automatically cleaned up on exit")
    print()

    # Example 3: Parsing from Anafora XML
    print("3. Parse from Anafora XML")
    print("-" * 70)
    xml_str = """
    <data>
        <annotations>
            <entity>
                <id>1@id</id>
                <span>0,4</span>
                <type>Year</type>
                <properties>
                    <Value>2024</Value>
                </properties>
            </entity>
        </annotations>
    </data>
    """
    
    elem = ET.fromstring(xml_str)
    results = from_xml(elem)
    print(f"Parsed {len(results)} temporal expressions from XML")
    for result in results:
        print(f"  - {result}")
    print()

    # Example 4: More complex XML - Last operator
    print("4. Complex Expression - 'last week'")
    print("-" * 70)
    xml_str = """
    <data>
        <annotations>
            <entity>
                <id>1@id</id>
                <span>0,9</span>
                <type>Last</type>
                <properties>
                    <Interval-Type>DocTime</Interval-Type>
                    <Period>2@id</Period>
                    <Semantics>Interval-Not-Included</Semantics>
                </properties>
            </entity>
            <entity>
                <id>2@id</id>
                <span>5,9</span>
                <type>Period</type>
                <properties>
                    <Type>Weeks</Type>
                    <Number>3@id</Number>
                </properties>
            </entity>
            <entity>
                <id>3@id</id>
                <span>5,6</span>
                <type>Number</type>
                <properties>
                    <Value>1</Value>
                </properties>
            </entity>
        </annotations>
    </data>
    """
    
    elem = ET.fromstring(xml_str)
    anchor = Interval.of(2024, 11, 19)
    results = from_xml(elem, known_intervals={(None, None): anchor})
    
    print(f"Anchor time: {anchor}")
    print(f"Parsed {len(results)} expressions:")
    for result in results:
        print(f"  Expression: {result}")
        if hasattr(result, 'start') and hasattr(result, 'end'):
            print(f"    Start: {result.start}")
            print(f"    End: {result.end}")
    print()

    # Example 5: What full parsing would look like (when model is available)
    print("5. Full Parsing API (stub)")
    print("-" * 70)
    text = "I saw her last week and will meet her next Tuesday."
    anchor = Interval.of(2024, 11, 19)
    
    print(f"Text: '{text}'")
    print(f"Anchor: {anchor}")
    print()
    print("When the TensorFlow model is available, you would call:")
    print("  results = parser.parse(text, anchor=anchor)")
    print("  for expr in results:")
    print("      print(f'{expr.text}: {expr.interval}')")
    print()
    print("Currently returns empty results (model inference not implemented)")
    results = parser.parse(text, anchor=anchor)
    print(f"Results: {results}")
    print()

    print("=" * 70)
    print("Phase 2 Complete! Neural parser infrastructure ready.")
    print("Next: Add TensorFlow model for full temporal expression parsing.")
    print("=" * 70)


if __name__ == "__main__":
    main()
