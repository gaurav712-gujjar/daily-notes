# Python logging module

**Category:** Python  
**Date:** 2026-10-08 (morning)

---

# Python Logging Module

The `logging` module provides a flexible framework for emitting log messages from Python programs. Unlike simple `print` statements, it supports multiple severity levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`), configurable output destinations (console, files, sockets), and runtime control over which messages are recorded.

### Why use it?
- **Production‑ready diagnostics**: Logs can be routed to rotating files or external systems without changing code.
- **Granular control**: Adjust logging verbosity via configuration, enabling detailed debugging in development while keeping production logs succinct.
- **Structured information**: Include timestamps, module names, and custom fields, facilitating automated log analysis and monitoring.

### Quick Example
```python
import logging

# Basic configuration: INFO level to console, simple format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s: %(message)s',
)

logger = logging.getLogger('my_app')

def divide(a, b):
    logger.debug(f'Attempting division: {a}/{b}')
    try:
        result = a / b
    except ZeroDivisionError:
        logger.error('Division by zero!')
        raise
    else:
        logger.info('Division succeeded')
        return result

# Only INFO and above will appear (DEBUG is suppressed)
print(divide(10, 2))
```
In this snippet, `logger.debug` is ignored because the logger’s level is set to `INFO`. Changing `level=logging.DEBUG` would reveal the detailed trace, demonstrating how the same code can serve both development and production needs without modification.
