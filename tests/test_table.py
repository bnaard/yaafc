import polars as pl
import pytest

from yaafc.ui.table import TableState, table


@pytest.fixture(autouse=True)
def reset_table_state():
    # Reset TableState before each test
    TableState.data = pl.DataFrame({
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["New York", "Los Angeles", "Chicago"],
    })
    yield


def test_table_renders_headers_and_rows():
    comp = table()
    columns = TableState.data.columns
    rows = TableState.data.rows(named=True)
    # Check that all headers are present
    for col in columns:
        assert col in str(comp)
    # Check that all cell values are present
    for row in rows:
        for col in columns:
            assert str(row[col]) in str(comp)


def test_table_updates_on_dataframe_change():
    new_df = pl.DataFrame({"A": [1, 2], "B": [3, 4]})
    TableState.set_data(new_df)
    comp = table()
    assert "A" in str(comp) and "B" in str(comp)
    assert "1" in str(comp) and "4" in str(comp)


def test_table_empty_dataframe():
    TableState.set_data(pl.DataFrame({}))
    comp = table()
    # Should render no headers or rows
    assert "column_header_cell" not in str(comp)
    assert "table.cell" not in str(comp)


def test_table_non_string_values():
    df = pl.DataFrame(
        {"Num": [1, None, 3.5], "Bool": [True, False, None]}, schema={"Num": pl.Float64, "Bool": pl.Boolean}
    )
    TableState.set_data(df)
    comp = table()
    assert "1.0" in str(comp)
    assert "3.5" in str(comp)
    # Reflex/JS renders booleans as 'true'/'false' (lowercase)
    assert "true" in str(comp)
    assert "false" in str(comp)


def test_table_invalid_dataframe():
    # Failure case: set_data with non-DataFrame should raise TypeError
    with pytest.raises(TypeError):
        TableState.set_data(None)
