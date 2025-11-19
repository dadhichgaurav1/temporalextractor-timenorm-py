"""
Comprehensive example demonstrating the complete timenorm-py API.
"""
import datetime
from timenorm import (
    TemporalParser,
    Interval,
    Period,
    Last,
    Next,
    This,
    DAY,
    WEEK,
    MONTH,
)


def main():
    print("=" * 80)
    print("TIMENORM-PY: Complete API Demonstration")
    print("=" * 80)
    print()

    # ==================================================================================
    # PART 1: High-Level Parser API
    # ==================================================================================
    print("PART 1: High-Level Unified Parser API")
    print("=" * 80)
    print()

    # Example 1: Simple parsing
    print("1. Basic Text Parsing")
    print("-" * 80)
    parser = TemporalParser()
    anchor = Interval.of(2024, 11, 19)
    
    text = "I saw her last week"
    print(f"Text: '{text}'")
    print(f"Anchor: {anchor}")
    
    # Note: Returns empty without model, but API works
    results = parser.parse(text, anchor=anchor)
    print(f"Results: {results}")
    print("Note: Requires TensorFlow model for actual temporal expression detection")
    print()

    # Example 2: Using default anchor (today)
    print("2. Parsing with Default Anchor (Today)")
    print("-" * 80)
    results = parser.parse("See you next Tuesday")
    print(f"Text: 'See you next Tuesday'")
    print(f"Anchor: (defaults to today)")
    print(f"Results: {results}")
    print()

    # Example 3: Batch processing
    print("3. Batch Processing Multiple Texts")
    print("-" * 80)
    text = "Monday meeting. Tuesday lunch. Wednesday presentation."
    spans = [(0, 15), (16, 29), (30, 53)]
    
    print(f"Text: '{text}'")
    print(f"Spans: {spans}")
    
    results = parser.parse_batch(text, spans, anchor=anchor)
    print(f"Results: {len(results)} batches")
    for i, batch_result in enumerate(results):
        print(f"  Batch {i+1}: {batch_result}")
    print()

    # Example 4: File parsing
    print("4. Parsing from File")
    print("-" * 80)
    import tempfile
    from pathlib import Path
    
    # Create temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("The meeting was scheduled for last Friday.")
        temp_file = Path(f.name)
    
    try:
        results = parser.parse_file(temp_file, anchor=anchor)
        print(f"File: {temp_file.name}")
        print(f"Content: 'The meeting was scheduled for last Friday.'")
        print(f"Results: {results}")
    finally:
        temp_file.unlink()
    print()

    # Example 5: Context manager
    print("5. Using Context Manager for Resource Cleanup")
    print("-" * 80)
    with TemporalParser() as parser:
        results = parser.parse("next month", anchor=anchor)
        print(f"Text: 'next month'")
        print(f"Results: {results}")
        print("Parser automatically cleaned up on exit")
    print()

    # ==================================================================================
    # PART 2: Low-Level Temporal Algebra
    # ==================================================================================
    print()
    print("PART 2: Low-Level Temporal Algebra (Direct Construction)")
    print("=" * 80)
    print()

    # Example 6: Creating intervals
    print("6. Creating Intervals")
    print("-" * 80)
    year_2024 = Interval.of(2024)
    march = Interval.of(202, 3)
    march_15 = Interval.of(2024, 3, 15)
    
    print(f"Year 2024: {year_2024}")
    print(f"March 2024: {march}")
    print(f"March 15, 2024: {march_15}")
    print()

    # Example 7: Period arithmetic
    print("7. Period Arithmetic")
    print("-" * 80)
    three_months = Period(MONTH, 3)
    start = datetime.datetime(2024, 1, 1)
    interval = start + three_months
    
    print(f"3 months from {start.date()}: {interval}")
    print(f"  Start: {interval.start}")
    print(f"  End: {interval.end}")
    print()

    #Example 8: Temporal operators
    print("8. Temporal Operators")
    print("-" * 80)
    anchor_date = Interval.of(2024, 11, 19)
    
    # Last week
    last_week = Last(anchor_date, Period(DAY, 7))
    print(f"Last week from {anchor_date}:")
    print(f"  {last_week}")
    print(f"  Start: {last_week.start}")
    print(f"  End: {last_week.end}")
    print()
    
    # Next 3 weeks
    next_weeks = Next(anchor_date, Period(WEEK, 3))
    print(f"Next 3 weeks from {anchor_date}:")
    print(f"  {next_weeks}")
    print(f"  Start: {next_weeks.start}")
    print(f"  End: {next_weeks.end}")
    print()

    # ==================================================================================
    # PART 3: XML Parsing (Anafora Format)
    # ==================================================================================
    print()
    print("PART 3: XML Parsing (Anafora Format)")
    print("=" * 80)
    print()

    print("9. Parsing Anafora XML Annotations")
    print("-" * 80)
    
    import xml.etree.ElementTree as ET
    from timenorm import from_xml
    
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
                    <Value>2</Value>
                </properties>
            </entity>
        </annotations>
    </data>
    """
    
    elem = ET.fromstring(xml_str)
    anchor = Interval.of(2024, 11, 19)
    results = from_xml(elem, known_intervals={(None, None): anchor})
    
    print("XML representing 'last 2 weeks':")
    print(f"Anchor: {anchor}")
    print(f"Parsed result: {results[0]}")
    print(f"  Start: {results[0].start}")
    print(f"  End: {results[0].end}")
    print()

    # ==================================================================================
    # Summary
    # ==================================================================================
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print()
    print("✅ High-Level API:")
    print("   - TemporalParser for simple text parsing")
    print("   - File and batch processing support")
    print("   - Automatic anchor time management")
    print()
    print("✅ Low-Level API:")
    print("   - Direct construction of temporal expressions")
    print("   - Operators: Last, Next, Before, After, This, Between, Nth")
    print("   - Period arithmetic with datetime integration")
    print()
    print("✅ XML Support:")
    print("   - Anafora XML format parsing")
    print("   - Full operator and entity type support")
    print()
    print("📝 Note: Neural network inference requires TensorFlow model")
    print("   The API and infrastructure are ready - just add the model!")
    print()
    print("=" * 80)


if __name__ == "__main__":
    main()
