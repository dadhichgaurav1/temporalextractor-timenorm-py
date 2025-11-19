"""
Example demonstrating the timenorm-py temporal expression library.

This shows how to use the core types and operators to represent and manipulate
temporal expressions.
"""
import datetime
from timenorm import (
    Interval,
    Period,
    Repeating,
    Last,
    Next,
    This,
    Between,
    Year,
    DAY,
    WEEK,
    MONTH,
    YEAR,
)


def main():
    print("=" * 70)
    print("Timenorm-Py Examples")
    print("=" * 70)
    print()

    # Example 1: Simple intervals
    print("1. Creating Intervals")
    print("-" * 70)
    year_2024 = Interval.of(2024)
    print(f"Year 2024: {year_2024}")
    print(f"  Start: {year_2024.start}")
    print(f"  End: {year_2024.end}")
    print()

    march_2024 = Interval.of(2024, 3)
    print(f"March 2024: {march_2024}")
    print()

    march_15 = Interval.of(2024, 3, 15)
    print(f"March 15, 2024: {march_15}")
    print()

    # Example 2: Periods
    print("2. Working with Periods")
    print("-" * 70)
    three_months = Period(MONTH, 3)
    start = datetime.datetime(2024, 1, 1)
    interval = start + three_months
    print(f"3 months starting from {start.date()}: {interval}")
    print()

    one_week = Period(WEEK, 1)
    end = datetime.datetime(2024, 3, 15)
    interval = end - one_week
    print(f"1 week ending at {end.date()}: {interval}")
    print()

    # Example 3: Repeating intervals
    print("3. Repeating Intervals")
    print("-" * 70)
    # Tuesday = 1 in dateutil (Monday=0)
    tuesday = Repeating(DAY, WEEK, value=1)
    anchor = datetime.datetime(2024, 11, 15)  # Friday
    next_tuesday = anchor + tuesday
    print(f"Next Tuesday after {anchor.date()}: {next_tuesday}")
    print()

    last_tuesday = anchor - tuesday
    print(f"Last Tuesday before {anchor.date()}: {last_tuesday}")
    print()

    # Example 4: Last operator
    print("4. Last Operator - 'last 7 days'")
    print("-" * 70)
    anchor_interval = Interval.of(2024, 11, 15)
    last_week = Last(anchor_interval, Period(DAY, 7))
    print(f"Anchor: {anchor_interval}")
    print(f"Last 7 days: {last_week}")
    print(f"  Start: {last_week.start}")
    print(f"  End: {last_week.end}")
    print()

    # Example 5: Next operator
    print("5. Next Operator - 'next 3 weeks'")
    print("-" * 70)
    next_weeks = Next(anchor_interval, Period(WEEK, 3))
    print(f"Anchor: {anchor_interval}")
    print(f"Next 3 weeks: {next_weeks}")
    print()

    # Example 6: This operator
    print("6. This Operator - 'this January'")
    print("-" * 70)
    november = Interval.of(2024, 11, 10)
    january = Repeating(MONTH, YEAR, value=1)
    this_january = This(november, january)
    print(f"Spoken in: {november}")
    print(f"'This January': {this_january}")
    print()

    # Example 7: Between operator
    print("7. Between Operator - 'from Monday to Friday'")
    print("-" * 70)
    monday = Interval.of(2024, 11, 18)
    friday = Interval.of(2024, 11, 22)
    between = Between(monday, friday, start_included=True, end_included=True)
    print(f"Monday: {monday}")
    print(f"Friday: {friday}")
    print(f"Between (inclusive): {between}")
    print()

    # Example 8: Complex expression - "since last year"
    print("8. Complex Expression - 'since last year'")
    print("-" * 70)
    doc_time = Interval.of(2019, 5, 30)
    last_year_start = Year(2018)
    since_last_year = Between(last_year_start, doc_time)
    print(f"Document time: {doc_time}")
    print(f"'Since last year': {since_last_year}")
    print(f"  Start: {since_last_year.start}")
    print(f"  End: {since_last_year.end}")
    print()

    print("=" * 70)
    print("Phase 1 Complete! Core types working correctly.")
    print("=" * 70)


if __name__ == "__main__":
    main()
