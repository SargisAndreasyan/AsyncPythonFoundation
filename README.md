# Async Python Mini-Guide

This project is a mini-guide for asynchronous Python (`asyncio`).  
It contains working examples, drafts, and experiments demonstrating key concepts like concurrency, queues, locks, semaphores, task cancellation, and error handling.

---

## Project Structure
```
├── README.md # This file
├── basics # Theory and basic notes (planned)
├── drafts # Drafts and experiments
│ ├── await_way.py # Using await
│ ├── collback.py # Callback-style example
│ ├── create_task_way.py # Using create_task for parallel execution
│ ├── download_queue.py # Async downloading with a queue
│ ├── event_loop.py # Working with the event loop
│ ├── final_stepik_project.py# Final course project
│ ├── gather.py # Using gather for multiple tasks
│ ├── gather_return.py # gather with return_exceptions
│ ├── lock_balance_withdraw.py # Lock for synchronizing operations
│ ├── lock_sync.py # Lock examples
│ ├── lost_task.py # Lost task scenarios
│ ├── main.py # Example main scripts
│ ├── restorant_with_3.py # Restaurant concurrency example
│ ├── semaphore_01.py # Semaphore example
│ ├── semaphore_02.py
│ ├── semaphore_as_lock.py
│ ├── task_group.py
│ ├── timeout.py
│ ├── try_except_02.py
│ └── try_except_async.py
└── examples # Clean working examples
├── 01_basic_asyncio.py
├── 02_asyncio_queues.py
├── 03_lock.py
├── 04_semaphore_lock.py
├── 05_task_cancellation.py
└── 06_pipeline_example.py
```

---

## Description

- **basics/** – planned folder for notes and theory about `asyncio`  
- **drafts/** – experimental scripts, testing different approaches and patterns  
- **examples/** – clean, working examples that can be run directly  

Each file in `examples/` demonstrates a key concept of asynchronous programming:

1. **01_basic_asyncio.py** – basic async/await usage  
2. **02_asyncio_queues.py** – queues and producer/consumer pattern  
3. **03_lock.py** – using Lock to synchronize shared resources  
4. **04_semaphore_lock.py** – semaphore controlling concurrency  
5. **05_task_cancellation.py** – cancelling long-running tasks  
6. **06_pipeline_example.py** – full pipeline: generator → workers → aggregator  