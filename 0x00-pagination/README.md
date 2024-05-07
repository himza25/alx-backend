# Pagination Project

This project contains a set of solutions to various pagination challenges. Each task demonstrates different aspects of pagination using the popular baby names dataset.

## Tasks

### 0. Simple Helper Function
**Objective:**  
Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

**Task Details:**
- Returns a tuple containing the start and end indexes corresponding to the given page parameters.
- Page numbers are 1-indexed.

**Files:**
- `0-simple_helper_function.py`

### 1. Simple Pagination
**Objective:**  
Implement a `Server` class that provides simple pagination of the baby names dataset.

**Task Details:**
- Implement a `get_page` method that takes two integer arguments: `page` and `page_size`.
- Ensure both arguments are integers greater than `0`.
- Use `index_range` to find the correct indexes and return the appropriate page.
- If out of range, return an empty list.

**Files:**
- `1-simple_pagination.py`

### 2. Hypermedia Pagination
**Objective:**  
Implement a `get_hyper` method in the `Server` class for hypermedia pagination.

**Task Details:**
- Takes the same arguments as `get_page`.
- Returns a dictionary containing:
  - `page_size`: length of the returned dataset page
  - `page`: the current page number
  - `data`: the dataset page
  - `next_page`: number of the next page, or `None`
  - `prev_page`: number of the previous page, or `None`
  - `total_pages`: total number of pages in the dataset

**Files:**
- `2-hypermedia_pagination.py`

### 3. Deletion-Resilient Hypermedia Pagination
**Objective:**  
Implement a `get_hyper_index` method to ensure rows aren't missed even if they are removed between queries.

**Task Details:**
- Takes two integer arguments `index` and `page_size` with default values of `None` and `10`, respectively.
- Returns a dictionary containing:
  - `index`: current starting index of the returned page
  - `next_index`: the next index to query with
  - `page_size`: current page size
  - `data`: the actual page of the dataset
- Use `assert` to verify that `index` is within a valid range.
- If rows are removed, ensure the user still receives consistent results.

**Files:**
- `3-hypermedia_del_pagination.py`
