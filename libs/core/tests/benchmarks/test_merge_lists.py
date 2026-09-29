"""Measure streaming updates to lists of content blocks."""

import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from langchain_core.utils._merge import merge_lists


@pytest.mark.parametrize("block_count", [10, 1000])
@pytest.mark.parametrize("position", ["first", "last", "missing"])
@pytest.mark.benchmark
def test_merge_lists(
    benchmark: BenchmarkFixture, block_count: int, position: str
) -> None:
    blocks = [{"index": i, "text": "a"} for i in range(block_count)]
    index = {"first": 0, "last": block_count - 1, "missing": block_count}[position]
    incoming = [{"index": index, "text": "b"}]

    benchmark(merge_lists, blocks, incoming)
