"""Benchmarks for configuration merging on the runnable invocation path."""

import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from langchain_core.runnables.config import RunnableConfig, merge_configs


@pytest.mark.parametrize(
    ("base", "incoming"),
    [
        pytest.param({}, {}, id="empty"),
        pytest.param(
            {"tags": ["parent"], "metadata": {"user": "a"}},
            {"tags": ["child"], "metadata": {"request": "b"}},
            id="flat-metadata",
        ),
        pytest.param(
            {"metadata": {"lc_versions": {"core": "1"}}},
            {"metadata": {"lc_versions": {"partner": "2"}}},
            id="package-versions",
        ),
    ],
)
@pytest.mark.benchmark
def test_merge_configs(
    benchmark: BenchmarkFixture, base: RunnableConfig, incoming: RunnableConfig
) -> None:
    benchmark(merge_configs, base, incoming)
