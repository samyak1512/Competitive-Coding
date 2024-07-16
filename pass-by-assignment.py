In Python, the distinction between passing by reference and passing by value isn't as explicit as in some other languages. Instead, Python uses a mechanism often referred to as "pass-by-object-reference" or "pass-by-assignment." Here's a detailed explanation of how it works:

1. **Passing Mutable Objects (e.g., lists, dictionaries)**:
   - When you pass a mutable object to a function, such as a list or a dictionary, you are passing a reference to the original object. 
   - Any modifications to the object within the function affect the original object outside the function.

   ```python
   def modify_list(lst):
       lst.append(1)

   my_list = []
   modify_list(my_list)
   print(my_list)  # Output: [1]
   ```

2. **Passing Immutable Objects (e.g., integers, strings, tuples)**:
   - When you pass an immutable object to a function, such as an integer, string, or tuple, you are still passing a reference to the object, but you cannot modify the original object itself because it is immutable.
   - If you reassign the variable within the function, it creates a new object in memory and does not affect the original object.

   ```python
   def modify_integer(x):
       x += 1

   my_int = 10
   modify_integer(my_int)
   print(my_int)  # Output: 10
   ```

3. **List Example: Passing by Reference**:
   - When a list is passed to a function, the reference to the list is passed, so changes made to the list inside the function will reflect outside the function.

   ```python
   def append_item(lst):
       lst.append('new item')

   my_list = ['item']
   append_item(my_list)
   print(my_list)  # Output: ['item', 'new item']
   ```

4. **Creating a New List: Simulating Pass-by-Value**:
   - If you want to avoid modifying the original list, you can create a new list by copying the original one.

   ```python
   def append_item(lst):
       new_lst = lst + ['new item']  # Creates a new list
       return new_lst

   my_list = ['item']
   new_list = append_item(my_list)
   print(my_list)  # Output: ['item']
   print(new_list)  # Output: ['item', 'new item']
   ```

In the code example you provided earlier, when you use `stack + ['L']` or `stack + ['R']`, a new list is created at each recursive step. This new list is a different object in memory, which means that the original `stack` is not modified:

```python
def dfs(node, stack, target):
    if not node:
        return None
    if node.val == target:
        return stack

    left_path = dfs(node.left, stack + ['L'], target)  # Creates a new list
    if left_path is not None:
        return left_path
    right_path = dfs(node.right, stack + ['R'], target)  # Creates a new list
    if right_path is not None:
        return right_path
    return None
```

In summary:
- **Mutable objects (like lists and dictionaries)** are passed by reference, so changes inside the function affect the original object.
- **Immutable objects (like integers, strings, and tuples)** are also passed by reference, but since they cannot be modified, reassigning them inside the function does not affect the original object.
- When you create a new object (like using `stack + ['L']`), you are creating a new reference, simulating a pass-by-value behavior.
