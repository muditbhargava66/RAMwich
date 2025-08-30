# Changelog

All notable changes to the RAMwich project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- **Critical**: Fixed hanging issue in `test_tile_features.py` that caused infinite loops during test execution
- **Router**: Fixed `stop_after_all_packets_sent()` method that used problematic recursive function calls in SimPy
- **Tile Operations**: Simplified `execute_halt()` method to prevent synchronization deadlocks
- **Inter-tile Communication**: Resolved packet transmission and reception issues in router implementation

### Changed
- **Router Stopping Logic**: Replaced recursive queue checking with simple while loop in `stop_after_all_packets_sent()`
- **Halt Operation**: Streamlined halt execution to use minimal timeout instead of complex core/router synchronization
- **Test Reliability**: All tests now complete successfully without hanging or timing out

### Technical Details
- Modified `src/ramwich/blocks/router.py`:
  - Fixed `stop_after_all_packets_sent()` method to use `while self.send_queue.items:` loop
  - Removed problematic recursive `check_queue()` function
- Modified `src/ramwich/tile.py`:
  - Simplified `execute_halt()` to use `yield self.env.timeout(0)` instead of waiting for core processes
  - Maintained generator pattern required by SimPy while eliminating deadlock conditions

### Verified
- [x] All 7 tests pass consistently:
  - `test_core_features.py` - Core computation functionality
  - `test_dram_controller.py` (5 tests) - DRAM controller operations  
  - `test_tile_features.py` - Complex inter-tile communication with neural network computation
- [x] No hanging or infinite loops in test execution
- [x] Full RAMwich functionality preserved:
  - Inter-tile communication (Send/Recv operations)
  - Matrix-vector multiplication in cores
  - ReLU activation functions
  - Memory operations (Load/Store)
  - Multi-core coordination
  - Complete neural network simulation pipeline

## [Previous] - Context from Earlier Development

### Added
- Complete RAMwich architecture simulation framework
- Multi-tile, multi-core processing simulation
- Matrix-Vector Multiplication Units (MVMU)
- Vector Functional Units (VFU)
- DRAM controller with realistic timing
- Inter-tile communication via Network-on-Chip (NoC)
- Pipeline execution model
- Comprehensive test suite
- Example neural network configurations (MLP for MNIST)

### Features
- SimPy-based discrete event simulation
- Configurable architecture parameters
- Statistics collection and reporting
- Memory hierarchy simulation (SRAM, DRAM, eDRAM)
- Packet-based inter-tile communication
- Support for various neural network operations