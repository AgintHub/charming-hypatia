import os
import asyncio
import functools
import inspect
import json
import sys
from typing import Dict, Any, List, Callable, Coroutine, Union, Optional

from code.analyze_market_structure import analyze_market_structure
from code.backtest_trading_signals import backtest_trading_signals
from code.build_signal_generation_model import build_signal_generation_model
from code.calculate_performance_metrics import calculate_performance_metrics
from code.calculate_statistical_metrics import calculate_statistical_metrics
from code.collect_historical_future_data import collect_historical_future_data
from code.compile_strategy_documentation import compile_strategy_documentation
from code.create_liquidity_control_rules import create_liquidity_control_rules
from code.define_strategy_framework import define_strategy_framework
from code.design_position_sizing_rules import design_position_sizing_rules
from code.feature_engineering import feature_engineering
from code.identify_risk_factors import identify_risk_factors
from code.model_regression_based_strategy import model_regression_based_strategy
from code.optimize_model_parameters import optimize_model_parameters
from code.process_historical_data import process_historical_data
from code.validate_overfitting_risk import validate_overfitting_risk

# Get async mode from environment variable or default to False
ASYNC_MODE = os.environ.get('ASYNC_MODE', '').lower() in ('true', '1', 'yes', 'y')

def make_async(func):
    """Convert a synchronous function to an asynchronous function.

    If the function is already asynchronous, return it unchanged.
    If the function is synchronous, wrap it in an async function.
    """
    # If it's already a coroutine function, return it as is
    if inspect.iscoroutinefunction(func):
        return func

    # Otherwise, wrap it as an async function
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return async_wrapper

analyze_market_structure_async = make_async(analyze_market_structure)
backtest_trading_signals_async = make_async(backtest_trading_signals)
build_signal_generation_model_async = make_async(build_signal_generation_model)
calculate_performance_metrics_async = make_async(calculate_performance_metrics)
calculate_statistical_metrics_async = make_async(calculate_statistical_metrics)
collect_historical_future_data_async = make_async(collect_historical_future_data)
compile_strategy_documentation_async = make_async(compile_strategy_documentation)
create_liquidity_control_rules_async = make_async(create_liquidity_control_rules)
define_strategy_framework_async = make_async(define_strategy_framework)
design_position_sizing_rules_async = make_async(design_position_sizing_rules)
feature_engineering_async = make_async(feature_engineering)
identify_risk_factors_async = make_async(identify_risk_factors)
model_regression_based_strategy_async = make_async(model_regression_based_strategy)
optimize_model_parameters_async = make_async(optimize_model_parameters)
process_historical_data_async = make_async(process_historical_data)
validate_overfitting_risk_async = make_async(validate_overfitting_risk)

async def run_workflow(user_input: str) -> Dict[str, Any]:
    """Execute the workflow by running each level in the topological sort.

    Args:
        user_input: The input string for the workflow

    Returns:
        Dict containing all results keyed by node name
    """
    # Store results for each node
    results = {}

    # Level 0: collect_historical_future_data, define_strategy_framework, identify_risk_factors
    async def run_collect_historical_future_data():
        # Call the async version of collect_historical_future_data with results from dependencies
        return await collect_historical_future_data_async(user_input)

    async def run_define_strategy_framework():
        # Call the async version of define_strategy_framework with results from dependencies
        return await define_strategy_framework_async(user_input)

    async def run_identify_risk_factors():
        # Call the async version of identify_risk_factors with results from dependencies
        return await identify_risk_factors_async(user_input)

    # Run level 0 nodes in parallel
    level_0_results = await asyncio.gather(run_collect_historical_future_data(), run_define_strategy_framework(), run_identify_risk_factors())
    results['collect_historical_future_data'] = level_0_results[0]
    results['define_strategy_framework'] = level_0_results[1]
    results['identify_risk_factors'] = level_0_results[2]

    # Level 1: process_historical_data
    async def run_process_historical_data():
        # Call the async version of process_historical_data with results from dependencies
        return await process_historical_data_async(results['collect_historical_future_data'])

    # Run level 1 nodes in parallel
    results['process_historical_data'] = await run_process_historical_data()

    # Level 2: feature_engineering, calculate_statistical_metrics
    async def run_feature_engineering():
        # Call the async version of feature_engineering with results from dependencies
        return await feature_engineering_async(results['process_historical_data'], results['identify_risk_factors'])

    async def run_calculate_statistical_metrics():
        # Call the async version of calculate_statistical_metrics with results from dependencies
        return await calculate_statistical_metrics_async(results['process_historical_data'])

    # Run level 2 nodes in parallel
    level_2_results = await asyncio.gather(run_feature_engineering(), run_calculate_statistical_metrics())
    results['feature_engineering'] = level_2_results[0]
    results['calculate_statistical_metrics'] = level_2_results[1]

    # Level 3: analyze_market_structure
    async def run_analyze_market_structure():
        # Call the async version of analyze_market_structure with results from dependencies
        return await analyze_market_structure_async(results['process_historical_data'], results['calculate_statistical_metrics'])

    # Run level 3 nodes in parallel
    results['analyze_market_structure'] = await run_analyze_market_structure()

    # Level 4: build_signal_generation_model, create_liquidity_control_rules, model_regression_based_strategy
    async def run_build_signal_generation_model():
        # Call the async version of build_signal_generation_model with results from dependencies
        return await build_signal_generation_model_async(results['feature_engineering'], results['define_strategy_framework'], results['analyze_market_structure'])

    async def run_create_liquidity_control_rules():
        # Call the async version of create_liquidity_control_rules with results from dependencies
        return await create_liquidity_control_rules_async(results['define_strategy_framework'], results['analyze_market_structure'])

    async def run_model_regression_based_strategy():
        # Call the async version of model_regression_based_strategy with results from dependencies
        return await model_regression_based_strategy_async(results['calculate_statistical_metrics'], results['feature_engineering'], results['analyze_market_structure'])

    # Run level 4 nodes in parallel
    level_4_results = await asyncio.gather(run_build_signal_generation_model(), run_create_liquidity_control_rules(), run_model_regression_based_strategy())
    results['build_signal_generation_model'] = level_4_results[0]
    results['create_liquidity_control_rules'] = level_4_results[1]
    results['model_regression_based_strategy'] = level_4_results[2]

    # Level 5: design_position_sizing_rules, backtest_trading_signals
    async def run_design_position_sizing_rules():
        # Call the async version of design_position_sizing_rules with results from dependencies
        return await design_position_sizing_rules_async(results['calculate_statistical_metrics'], results['create_liquidity_control_rules'])

    async def run_backtest_trading_signals():
        # Call the async version of backtest_trading_signals with results from dependencies
        return await backtest_trading_signals_async(results['build_signal_generation_model'], results['model_regression_based_strategy'], results['create_liquidity_control_rules'])

    # Run level 5 nodes in parallel
    level_5_results = await asyncio.gather(run_design_position_sizing_rules(), run_backtest_trading_signals())
    results['design_position_sizing_rules'] = level_5_results[0]
    results['backtest_trading_signals'] = level_5_results[1]

    # Level 6: optimize_model_parameters
    async def run_optimize_model_parameters():
        # Call the async version of optimize_model_parameters with results from dependencies
        return await optimize_model_parameters_async(results['backtest_trading_signals'])

    # Run level 6 nodes in parallel
    results['optimize_model_parameters'] = await run_optimize_model_parameters()

    # Level 7: validate_overfitting_risk, calculate_performance_metrics
    async def run_validate_overfitting_risk():
        # Call the async version of validate_overfitting_risk with results from dependencies
        return await validate_overfitting_risk_async(results['optimize_model_parameters'])

    async def run_calculate_performance_metrics():
        # Call the async version of calculate_performance_metrics with results from dependencies
        return await calculate_performance_metrics_async(results['backtest_trading_signals'], results['optimize_model_parameters'])

    # Run level 7 nodes in parallel
    level_7_results = await asyncio.gather(run_validate_overfitting_risk(), run_calculate_performance_metrics())
    results['validate_overfitting_risk'] = level_7_results[0]
    results['calculate_performance_metrics'] = level_7_results[1]

    # Level 8: compile_strategy_documentation
    async def run_compile_strategy_documentation():
        # Call the async version of compile_strategy_documentation with results from dependencies
        return await compile_strategy_documentation_async(results['calculate_performance_metrics'], results['define_strategy_framework'])

    # Run level 8 nodes in parallel
    results['compile_strategy_documentation'] = await run_compile_strategy_documentation()

    # Return all results
    return results

def run_workflow_sync(user_input: str) -> Dict[str, Any]:
    """Synchronous wrapper around the async workflow execution."""
    return asyncio.run(run_workflow(user_input))

def main():
    """Main entry point.

    Handles arguments in the following priority:
    1. Command-line argument (sys.argv[1])
    2. If no argument, uses empty string as input but displays a warning.
    """
    # Get user input from command line or use empty string
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    else:
        # No input provided - display help message but continue with empty string
        print('Warning: No input provided. Using empty string as input.')
        print('For better results, provide an input argument:')
        print(f'  python {os.path.basename(__file__)} "your input text here"')
        print('Or use a file as input:')
        print(f'  python {os.path.basename(__file__)} "$(cat input.txt)"')
        user_input = ""

    print(f'Running workflow with input: {user_input}')

    # Run the workflow
    results = run_workflow_sync(user_input)

    # Print results
    try:
        # Convert results to JSON
        json_results = json.dumps(results, indent=2, default=str)
        print(json_results)
    except (TypeError, ValueError) as e:
        print(f'Results could not be converted to JSON: {e}')
        print(f'Raw results: {results}')

    return results

if __name__ == '__main__':
    main()
